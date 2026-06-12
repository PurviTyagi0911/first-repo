class Transactions:
    def __init__(self,ttype,category,amount):
        self.amount=amount
        self.ttype=ttype
        self.category=category
    def display_details(self):
        print(f"{self.ttype} | {self.category} | ${self.amount}")