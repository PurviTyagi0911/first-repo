from transactions import Transactions
class FinanceTracker:
    def __init__(self):
     self.finance_tracker=[]
     self.next_id=1
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
       transaction=Transactions(self.next_id,"income",category,amount) 
       self.finance_tracker.append(transaction)
       self.save_trans(transaction)
       self.next_id+=1
    def clear_his(self):
       self.finance_tracker.clear()
       with open('transactions.txt','w') as file:
          file.write('')
       self.next_id=1
    def add_expense(self,amount,category):
       self.amount=amount
       self.category=category     
       transaction=Transactions(self.next_id,"expense",category,amount) 
       self.finance_tracker.append(transaction)
       self.save_trans(transaction)
       self.next_id+=1
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
       if category.strip()=='':
          print('invalid category')     
       search_key = category.lower()
       for transaction in self.finance_tracker:
             if transaction.category.lower() == search_key and transaction.ttype=='expense':
               transaction.display_details() 
               sumtctg+=transaction.amount
       if sumtctg==0:
          return 'no expense with that category found'
       else: 
          return f'total expense on {category} is ${sumtctg}'   
    def delete_trans(self,transaction_id):
       for index, transaction in enumerate((self.finance_tracker)):
        if transaction.transaction_id==transaction_id:
          self.finance_tracker.pop(index)
          print(f'transaction {transaction_id} deleted')
          break
       else:
          print('invalid transaction number')
       self.update_file()
    def highest_expense(self):
       dictctg={}
       for transaction in self.finance_tracker:
         if transaction.ttype=="expense":
          if transaction.category.lower() in dictctg:
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
          
          file.write(f'{transaction.transaction_id} | {transaction.ttype} | {transaction.category} | {transaction.amount}\n')
    def load_transactions(self):
       max_id = 0
       with open('transactions.txt','r') as file:
          for line in file:
             line = line.strip()
             if line == '':
                continue
             parts = [part.strip() for part in line.split('|')]
             if len(parts) == 4:
                transaction_id = int(parts[0])
                transaction_type = parts[1]
                transaction_category = parts[2]
                amount = int(parts[3])
             elif len(parts) == 3:
                transaction_id = max_id + 1
                transaction_type = parts[0]
                transaction_category = parts[1]
                amount = int(parts[2])
             else:
                continue
             transaction = Transactions(transaction_id, transaction_type, transaction_category, amount)
             self.finance_tracker.append(transaction)
             max_id = max(max_id, transaction_id)
       self.next_id = max_id + 1 if max_id else 1
    def update_file(self):
       with open('transactions.txt','w') as file:
          for transaction in self.finance_tracker:
           file.write(f'{transaction.transaction_id} | {transaction.ttype} | {transaction.category} | {transaction.amount}\n')
          
    