income = float(input("Enter your monthly income: "))
rent = float(input("Enter your monthly rent: "))
utilities = float(input("Enter your monthly utilities: "))
groceries = float(input("Enter your monthly groceries: "))
transport = float(input("Enter your monthly transport: "))

total_expenses = rent + utilities + groceries
remaining_money = income - total_expenses

print("Your total expenses are: $", format(total_expenses, ",.2f"))
print("Your remaining money is: $", format(remaining_money, ",.2f"))

if remaining_money < 200:
    print("Attention! Your remaining money is less than $200.Be careful with your spending.")