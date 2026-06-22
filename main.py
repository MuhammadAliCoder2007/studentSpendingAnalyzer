import pandas as pd


df = pd.read_csv('student_expenses.csv')
df['date'] = pd.to_datetime(df['date'])

null_vals = df.isnull().sum()

# print(df.head())
print(null_vals)