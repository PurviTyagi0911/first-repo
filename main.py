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
     balance=int(Tracker.view_balance())
     if balance<amount:
       print("transaction failed","invalid expense your current balance is",balance)
       Tracker.trans_failed()
     else:
       Tracker.add_expense(amount,category)
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