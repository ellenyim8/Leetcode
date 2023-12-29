# 2880 - select data
'''
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.
'''

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    id_101 = students[students['student_id'] == 101]
    name_age = id_101[["name", "age"]]
    return name_age
    

