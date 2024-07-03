## 3.2.0

- Add support for Python 3.9, 3.10
- Add wheels for Linux for Python 3.8, 3.9, 3.10
- Add instructions for installing in other platforms
- Automated publishing to PyPI via GitHub Actions
- Allow installing any modern `certifi`

## 3.1.0

- Fix SummaryLoad outputs to include "Low-Density Open Space", and exclude
  "Other Upland Areas"

## 3.0.0

- Official Release. No changes since `3.0.0-beta`.

## 3.0.0-beta

- **BREAKING** Drop support for Python 2.7
- Upgrade to Python 3.9
- Add `--json` flag to `run` which outputs the JSON model results to stdout.
  The JSON is sorted and formatted, and is stable enough for diffing.
- Add `pyproject.toml` for building wheel
- Update README with new build and publish instructions

## 2.0.0

- Official Release. No changes since `2.0.0-beta`.

## 2.0.0-beta

- Add "Low-Density Open Space" to Load outputs
- Remove "Other Upland Areas" from Load outputs
- Rename "Ld_Residential" to "Ld_Open_Space" in output GMS files

## 1.0.1

- Remove `bdist_wheel` as distribution because `linux` wheels are no longer
  supported by PyPI. See [PEP 513](https://www.python.org/dev/peps/pep-0513/)

## 1.0.0

- Includes major improvements by Drexel for refactoring the `CalcCN` and
  associated functions to reduce computation time. Accomplished by extracting
  code to a number of independent functions, vectorizing, and memoizing them.
  This results in an average speedup of 75% overall.
- **BREAKING** `parser` has been renamed to `Parser`
- **BREAKING** `run` now returns a tuple instead of a single value. The first
  value is a JSON of results, same as before. The second value is the internal
  model `z` which could be used to modularize the GMS writing in the future, as
  the JSON conversion currently done is lossy.
- `numba` is now a dependency, and must be installed prior to installing
  `gwlf-e`

## 0.6.3

- Add lower threshold to GrFlow to prevent double underflow.

## 0.6.2

- Set initial default for `AdjUrbanQTotal`
- Fix nitrogen/phosphorus conc transposition
- Handle input GMS file with no land cover
- Adjust low flow sediment value calculation and test

## 0.6.1

 - Updated commit history to include missing release commits (no code changes)

## 0.6.0

 - Used `AvSedYield` array to calculate Mean Low Flow Concentration.

## 0.5.0

- Added Unit field to SummaryLoads
- Separated out SummaryLoads and added Unit field

## 0.4.0

 - Added defaults to support input GMS files with missing stream data.
   **NOTE** The output may not be accurate for these files.

## 0.3.0

 - Removed unhelpful debug logging statements
 - Added GmsWriter to output GMS files
 - Added defaults to support loading MapShed data

## 0.2.0

 - Corrections to match VB version
 - Added sediment loads to model output
 - Added output unit tests

## 0.1.1

 - Registered project with PyPi

## 0.1.0

- Initial release
