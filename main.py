from finance_tracker import FinanceTracker
print(f'1 - Adding income \n2 - Adding expense \n3 - View transactions \n4 - View balance\n5 - Exit\n6 - Total Transactions\n7 - Total Expense\n8 - Search Category wise expense\n9 - Delete Transaction\n10 - View Highest expense Category')
Tracker=FinanceTracker()

while True:
    user_input=int(input("enter your input : "))

    if user_input==1:
     amount=int(input("enter amount : "))
     category=input("enter category : ")
     Tracker.add_income(amount, category)
     print("Amount of rupees",amount, "added successfully")
    elif user_input==2:
     amount=int(input("enter amount : "))
     category=input("enter category : ")
     Tracker.add_expense(amount,category)
     balance=int(Tracker.view_balance())
     if balance<0:
       print("transaction failed","invalid expense your current balance is",balance+amount)
       Tracker.trans_failed()
     else:
       print("Expense of rupees",amount, "added successfully")
    elif user_input==3:
     
     Tracker.view_transactions()
    elif user_input==4:
      print(Tracker.view_balance())
    elif user_input==5:
      break
    elif user_input==6:
      print("total transactions",Tracker.totalt())
    elif user_input==7:
      print(Tracker.texpenses()) 
    elif user_input==8:
     category=input("Enter category to search : ")
     print(Tracker.searchctg(category)) 
    elif user_input==9:
      num=int(input("Enter transaction number to delete : "))
      Tracker.delete_trans(num)
    elif user_input==10:

     print(Tracker.highest_expense())
    else:
      print('Invalid input')