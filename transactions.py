class Transactions:
    def __init__(self,transaction_id,ttype,category,amount):
        self.amount=amount
        self.transaction_id=transaction_id
        self.ttype=ttype
        self.category=category
    def display_details(self):
        print(f"{self.transaction_id:<5}"
              f"{self.ttype:<10}"
              f"{self.category:<15}"
              f"${self.amount}")