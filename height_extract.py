import numpy as np
import pandas as pd
from datetime import date

def calculate_age(x):
    return x['date_of_visit'].year - x['date_born'].year - ((x['date_of_visit'].month, x['date_of_visit'].day) < (x['date_born'].month, x['date_born'].day))

info = pd.read_excel("b37/height.xls", sheet_name='info')
height = pd.read_excel("b37/height.xls", sheet_name='height')
# print(info.columns)
# print(height.columns)

merge_info = pd.merge(info, height, on = 'study_no')
merge_info['age'] = merge_info.apply(calculate_age, axis=1)
print(merge_info.head())
# merge_info.to_csv('data/rawdata.csv',columns=['study_no','sex','height','date_born','date_of_visit','age'], index = 0)
merge_info.to_csv('data/rawdata.csv',columns=['study_no','sex','height','age'], index = 0)