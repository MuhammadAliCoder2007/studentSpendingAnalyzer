import pandas as pd


df = pd.read_csv('student_expenses.csv')
df['date'] = pd.to_datetime(df['date'])

null_vals = df.isnull().sum()

total_spending = df['amount'].sum()
avg_transaction = df['amount'].mean()
biggest_spending = df['amount'].max()
biggest_item = df.loc[df['amount'].idxmax(), 'item']
category_total = df.groupby('category')['amount'].sum().sort_values(ascending=False)

biggest_spending_day = df.loc[df['amount'].idxmax(), 'date'].day_name()

df['is_weekend'] = df['date'].dt.day_of_week>=5

weekend_vs_weekday = df.groupby('is_weekend')['amount'].sum()   


# print(weekend_vs_weekday)
# print(df.head())
# print(null_vals)
# print(total_spending)
# print(avg_transaction)
# print(biggest_item)
# print(category_total)
# print(biggest_spending_day)