# 2878- get size of dataframe
'''
DataFrame players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

[number of rows, number of columns]

'''

import pandas as pd

def getDataframeSize(players):
    res = []
    row = len(players)
    col = len(players.columns)
    res.append(row)
    res.append(col)
    return res

