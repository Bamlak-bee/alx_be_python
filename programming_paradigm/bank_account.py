class BankAccount:
    def __init__(self,account_balance=0):
        self.accountnce = account_balance
        
    def deposit(amount):
        account_balance += amount    
        
    def withdraw(amount):
        if account_balance < amount:
            return False
        else:
            return True
        
        
    def display_balance():
        print(f"Current balance is: {account_balance}")

