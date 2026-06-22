import pandas as pd
#importing padas

#loading data
df = pd.read_csv('student_expenses.csv')
df['date'] = pd.to_datetime(df['date'])

monthyBudget = 1500

null_vals = df.isnull().sum() #checking null vals

#checking spending
total_spending = df['amount'].sum()
avg_transaction = df['amount'].mean()
biggest_spending = df['amount'].max()
biggest_item = df.loc[df['amount'].idxmax(), 'item']

category_total = df.groupby('category')['amount'].sum().sort_values(ascending=False)    #doing category totals
food_total = category_total['Food']

biggest_spending_day = df.loc[df['amount'].idxmax(), 'date'].day_name() #fidning the biggest spending day

df['is_weekend'] = df['date'].dt.day_of_week>=5 #seprating weekend  from weekdays

weekend_vs_weekday = df.groupby('is_weekend')['amount'].sum()   #seprating weekend spendinf from weekdayas 

category_payment = df.groupby('payment_method')['amount'].sum()

# print(category_payment)

#all the print values

# print(weekend_vs_weekday)
# print(df.head())
# print(null_vals)
# print(total_spending)
# print(avg_transaction)
# print(biggest_item)
# print(category_total)
# print(biggest_spending_day)

precentage = (total_spending/monthyBudget)*100
if total_spending<=monthyBudget:
    print(f"Percentage of the budget used is {precentage:.2f} ")
    print(f"Budget left is {monthyBudget-total_spending:.2f}")
    print("GOOD JOB!")
else:
    print(f"Budget left is {monthyBudget-total_spending:.2f}")
    print("YOU ARE IN DEBT")

food_percentage = (food_total/monthyBudget)*100
print(f"YOU SPENT {food_percentage:.2f}% on food ")