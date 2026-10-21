import pandas as pd

df = pd.read_csv('messy_students.csv')

print(df.head(20))

df = df.drop_duplicates() #刪除重複
df['name'] = df['name'].str.strip()
print(df.head(20))

# 將乾淨的 DataFrame 匯出為新 CSV 檔
df.to_csv(
    "cleaned_students.csv",
    index=False
)
