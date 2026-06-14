class Transactions:
    def __init__(self,transaction_id,ttype,category,amount):
        self.amount=amount
        self.transaction_id=transaction_id
        self.ttype=ttype
        self.category=category
    def display_details(self):
        print(f"{self.transaction_id} | {self.ttype} | {self.category} | ${self.amount}")