from finance_tracker import FinanceTracker
print(f'1 - Adding income \n2 - Adding expense \n3 - View transactions \n4 - View balance\n5 - Exit\n6 - Total Transactions\n7 - Total Expense\n8 - Search Category wise expense\n9 - Delete Transaction\n10 - View Highest expense Category\n11 - Clear transaction history\n12 - Search Transaction using Transaction ID\n13 - Show Statistics')
Tracker=FinanceTracker()

while True:
    try:
      user_input=int(input("enter your input : "))
    except ValueError:
      print('invalid value entered')
      continue

    if user_input==1:
     try:
      amount=int(input("enter amount : "))
      if amount <= 0:
        print("amount must be positive")
        continue
     except ValueError:
      print('invalid value entered')
      continue
     category=input("enter category : ")
     while category=='':
       print('invalid actegory')
       category=input('enter category :')
     Tracker.add_income(amount, category)
     print("Amount of rupees",amount, "added successfully")
    elif user_input==2:
     try:
      amount=int(input("enter amount : "))
      if amount <= 0:
         print("amount must be positive")
         continue
     except ValueError:
      print('invalid value entered')
      continue
     category=input("enter category : ")
     while category=='':
       print('invalid actegory')
       category=input('enter category :')
     Tracker.add_expense(amount,category)
     balance=int(Tracker.view_balance())
     if balance<0:
       print("transaction failed","invalid expense your current balance is",balance+amount)
       Tracker.trans_failed()
       Tracker.update_file()
      
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
      num=int(input("Enter transaction id to delete : "))
      Tracker.delete_trans(num)
    elif user_input==10:
     Tracker.highest_expense()
    elif user_input==11:
      Tracker.clear_his()
      Tracker.update_file()
      print('transaction history cleared')
    elif user_input==12:
      try:
       id=int(input('Enter transaction id : '))
      except ValueError:
        print('invalid input')
        continue
      Tracker.search_id(id)
    elif user_input==13:
      Tracker.view_statistics()
    else:
      print('Invalid input')