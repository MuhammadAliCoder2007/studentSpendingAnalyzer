import pandas as pd


df = pd.read_csv('student_expenses.csv')
df['date'] = pd.to_datetime(df['date'])

null_vals = df.isnull().sum()

total_spending = df['amount'].sum()
avg_transaction = df['amount'].mean()
biggest_spending = df['amount'].max()
biggest_item = df.loc[df['amount'].idxmax(), 'item']
category_total = df.groupby('category')['amount'].sum().sort_values(ascending=False)

# print(df.head())
# print(null_vals)
# print(total_spending)
# print(avg_transaction)
# print(biggest_item)
print(category_total)