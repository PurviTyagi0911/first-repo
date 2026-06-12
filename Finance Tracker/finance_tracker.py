from transactions import Transactions
class FinanceTracker:
    def __init__(self):
     self.finance_tracker=[]
    def add_income(self,amount,category):
       self.amount=amount
       self.category=category

       FinanceTracker=Transactions(amount,"income",category) 
       self.finance_tracker.append(FinanceTracker)
       
    def add_expense(self,amount,category):
       self.amount=amount
       self.category=category
       FinanceTracker=Transactions(amount,"expense",category) 
       self.finance_tracker.append(FinanceTracker)
    def view_transactions(self):
       if len(self.finance_tracker)==0:
          print("no transactions")
          return
       
       for transaction in self.finance_tracker:
          transaction.display_details()
    def view_balance(self):
       balance=0
       for transaction in self.finance_tracker:
          if transaction.ttype=="income":
           balance+=transaction.amount
          elif transaction.ttype=="expense":
            balance-=transaction.amount 
       print(balance)           
          
         
