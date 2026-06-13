from transactions import Transactions
class FinanceTracker:
    def __init__(self):
     self.finance_tracker=[]
     try:
        self.load_transactions()
     except FileNotFoundError:
        return 'file not found'
    def view_balance(self):
       balance=0
       for transaction in self.finance_tracker:
          if transaction.ttype=="income":
           balance+=transaction.amount
          elif transaction.ttype=="expense":
            balance-=transaction.amount 
       return balance     
    def add_income(self,amount,category):
       self.amount=amount
       self.category=category
       FinanceTracker=Transactions("income",category,amount) 
       self.finance_tracker.append(FinanceTracker)
       self.save_trans(FinanceTracker)
       
    def add_expense(self,amount,category):
       self.amount=amount
       self.category=category
       FinanceTracker=Transactions("expense",category,amount) 
       self.finance_tracker.append(FinanceTracker)
       self.save_trans(FinanceTracker)

    def trans_failed(self):
       self.finance_tracker.pop(-1)

    def view_transactions(self):
       if len(self.finance_tracker)==0:
          print("no transactions")
          return
       
       for transaction in self.finance_tracker:
          transaction.display_details()
    def totalt(self):
       return len(self.finance_tracker)      
    def incomesum(self):
       sumt=0
       for transaction in self.finance_tracker:
          if transaction.ttype=="income":
             sumt+=transaction.amount

       return sumt
    def texpenses(self):
       sumt=0
       for transaction in self.finance_tracker:
          if transaction.ttype=="expense":
             sumt+=transaction.amount
       if sumt==0:
          return 'No expenses found'
       else:
          return f'total expense ${sumt}'
    def searchctg(self,category):
       sumtctg=0
       for transaction in self.finance_tracker:
             if transaction.category==category.lower() and transaction.ttype=='expense':
               transaction.display_details() 
               sumtctg+=transaction.amount
       if sumtctg==0:
          return 'no expense with that category found'
       else: 
          return f'total expense on {category} is ${sumtctg}'        
    def delete_trans(self,num):
       if num-1 in range(len(self.finance_tracker)):
        self.finance_tracker.pop(num-1)
        print(f'transaction {num} deleted')   
       else:
          print('invalid transaction number')
       self.update_file()
    def highest_expense(self):
       dictctg={}
       
       for transaction in self.finance_tracker:
         if transaction.ttype=="expense":
          if transaction.category in dictctg:
           dictctg[transaction.category]+=transaction.amount
          else:
           dictctg[transaction.category]=transaction.amount
       if dictctg=={}:
          return 'No expense found'
       else:
        maxamn=max(dictctg.values())
        maxctg= [key for key, value in dictctg.items() if value == maxamn]
        return f'maximum expense on {maxctg} of ${maxamn}'
    def save_trans(self,transaction):
       with open('transactions.txt','a') as file:
          file.write(f'{transaction.ttype} | {transaction.category} | {transaction.amount}\n')
    def load_transactions(self):
       with open('transactions.txt','r') as file:
          for line in file:
             line=line.strip()
             if line=='':
                continue
             parts=line.split("|")
             transaction_type=parts[0].strip()
             transaction_category=parts[1].strip()
             amount=int(parts[2].strip())
             FinanceTracker=Transactions(transaction_type,transaction_category,amount)
             self.finance_tracker.append(FinanceTracker)
    def update_file(self):
       with open('transactions.txt','w') as file:
          for transaction in self.finance_tracker:
           file.write(f'{transaction.ttype} | {transaction.category} | {transaction.amount}\n')
          
    