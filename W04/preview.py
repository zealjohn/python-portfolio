# 載入與檢視資料表內容
import pandas as pd

df = pd.read_csv('students.csv')
# 語法範例：預覽前五筆資料
print(df.head())
# 自訂筆數：檢視前十筆
df.head(10)
