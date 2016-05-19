# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import csv
import json
import sys

input_file = sys.argv[1] if len(sys.argv) == 2 else 'input_4.output'

with open('compare-4_sum.dat', 'r') as expected:
    with open(input_file, 'r') as actual:
        with open('compare.csv', 'w') as comparison:

            expected_reader = csv.reader(expected)
            results_json = json.load(actual)
            writer = csv.writer(comparison)

            for i in range(13):
                row = expected_reader.next()
                if i == 0:
                    key = results_json['meta']
                    result_row = ['Title', key['NYrs'], key['NRur'], key['NUrb'], key['NLU'],
                                  'Unset', key['SedDelivRatio'], key['WxYrBeg'], key['WxYrEnd']]
                else:
                    key = results_json['monthly'][i - 1]
                    month = '%s (ours)' % row[0]
                    result_row = [month, key['AvPrecipitation'], key['AvEvapoTrans'], key['AvGroundWater'],
                                  key['AvRunoff'], key['AvStreamFlow'], key['AvPtSrcFlow'], key['AvTileDrain'], key['AvWithdrawal']]

                writer.writerow(row)
                writer.writerow(result_row)

                # Write the header for the monthly variables
                if (i == 0):
                    writer.writerow(['Month', 'AvPrecipitation', 'AvEvapoTrans', 'AvGroundWater', 'AvRunoff',
                                     'AvStreamFlow', 'AvPtSrcFlow', 'AvTileDrain', 'AvWithdrawal'])

                print(row)
                print(result_row)
