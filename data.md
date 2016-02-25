#### MapShed gSSURGO Data Procedure

##### Available Water Storage Capacity
This is a straight join from `MapunitRaster_CONUS_30m` to the `muaggatt` table on the field `aws0100wta` as described in the gSSURGO documentation.

General Steps:
* In ArcMap, load the gSSURGO GeoDatabase
* Add MapunitRaster_CONUS_30 to the map
* In Geoprocessing toolbox, use the Data Management > Joins > Join Field tool
  * Input Table: `MapUnitRaster`, Input Join Field: `mukey`, Join Table: `muggatt`, Output Join Field: `mukey`
  * Join Fields: `aws0100wta`

After Join completes:
* Enable Spatial Analyst extension
* Spatial Analyst > Reclass > `Lookup`
  * Input Raster: `MapUnitRaster`, Lookup Field: `1aws0100wta`, Output Raster: `your destination`
  
##### Soil Texture
Soil texture has a more complicated set of relationships between the raster mukey and the value we want.  In the gSSURGO GDB, the tables that we need are:
* component
* chorizon
* chtexturegrp
* ctexture
and can be gotten with this set of relationships:

* `mukey` → component.`mukey`
  * For `mukey`, take component with highest `comppct_r` → `cokey`
    * If "highest" is a tie, just pick one
* `cokey` → chorizon.`cokey`
  * For {cokey}, take horizon with `hzdept_r == 0` → `chkey`
* `chkey` → chtexturegrp.`chkey`
  * → `chtgkey`
* `chtgkey` → `texcl`
* `texcl` → integer map for rasterization

In practice, after extracting those tables from the GDB into the `ssurgo-map-unit` DB on LR16, the sql query is:
```sql
/* 
Select the cokey for each mukey with the highest comppct_r .
For that cokey, grab the horizon at depth 0 to get a texture group for that horizon.
For that chtgkey, grab the texture key for the representitive material for that component (rvindicato = Yes)
For that chtgkey, grab the texcl (or lieutex if blank) for the corresponding row
*/

SELECT distinct 
	row_number() over (order by mukey) as OBJECTID, 
	m.mukey, m.cokey, h.chkey, tg.chtgkey, (t.texcl + t.lieutex) as type
FROM 
	(SELECT distinct 
		(select TOP 1 c1.mukey from component c1 where c1.mukey = c.mukey order by c1.comppct_r DESC ) as mukey,
		(select TOP 1 c2.cokey from component c2 where c2.mukey = c.mukey order by c2.comppct_r DESC ) as cokey
	FROM component c) m 
		LEFT OUTER JOIN dbo.chorizon h ON (h.cokey = m.cokey)
		JOIN chtexturegrp tg ON (h.chkey = tg.chkey AND tg.rvindicator = 'Yes')
		JOIN chtexture t ON (t.chtgkey = tg.chtgkey)
```

* These textures then get mapped to integers that we can rasterize
* Follow steps above for `Join` and `Lookup` to create output raster

##### Soil k-Factor (erodability)
kfactor is also produced in the same manner as soil texture, above, but with the following relationships:

* `mukey` → component.`mukey`
  * For `mukey`, take all components `cokey`s with `comppct_r`
* `cokey` → `chorizon.cokey`
  * For `cokey`, take horizon with `hzdept_r == 0`
* Weighted Average on `kwfact` by `comppct_r` per component of `mukey`
  * Averaged `kwfact` -->

With the same tables exported above, this query is used to produce the values for the mukey raster:

```sql
SELECT 
	c.mukey, 
	convert(decimal(7,5), (SUM(c.comppct_r * kwfact) / SUM(c.comppct_r + 0.0000001))) AS kfactor 
INTO soil_kfactor
FROM component c 
	LEFT OUTER JOIN chorizon h ON (c.cokey = h.cokey)
WHERE hzdept_r = '0'
GROUP BY c.mukey
ORDER BY mukey
```

Again, this needs the `Join` and `Lookup` steps as the rest to produce a final output.


##### General Notes
Use `ogr2ogr` to extract attribute tables from a GDB:
```bash
ogr2ogr -f CSV chtexturegrp.csv ~/usb/passport/gSSURGO_CONUS_30m.gdb chtexturegrp
```

To filter out records that won't be needed in the final queries, you can use the `-where` argument:
```bash
ogr2ogr -where "hzdept_r=0" -f CSV ~/usb/passport/gSSURGO_CONUS_30m.gdb chorizon
```
