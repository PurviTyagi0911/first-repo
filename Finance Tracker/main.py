from finance_tracker import FinanceTracker
print("1 for adding income")
Tracker=FinanceTracker()

while True:
    user_input=int(input("enter your input : "))

    if user_input==1:
     amount=int(input("enter amount : "))
     category=input("enter category : ")
     Tracker.add_income(amount,category)
     print("Amount of rupees",amount, "added successfully")
    elif user_input==2:
     amount=int(input("enter amount : "))
     category=input("enter category : ")
     Tracker.add_expense(amount,category)
     print("Expense of rupees",amount, "added successfully")
    elif user_input==3:
     Tracker.view_transactions()
    elif user_input==4:
      Tracker.view_balance()
     

