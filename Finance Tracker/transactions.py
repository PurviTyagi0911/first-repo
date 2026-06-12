class Transactions:
    def __init__(self,amount,ttype,category):
        self.amount=amount
        self.ttype=ttype
        self.category=category
    def display_details(self):
        print(self.ttype,"|",self.category,"|",self.amount)
         
