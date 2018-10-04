import pandas as pd

info = pd.read_excel("b37/height.xls", sheet_name='info')
height = pd.read_excel("b37/height.xls", sheet_name='height')
print(info.head())
print(height.head())