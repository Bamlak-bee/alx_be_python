class BankAccount:
    def __init__(self,account_balance,initial_balance=0):
        self.account_balance = account_balance
        # self.intial_balance = initial_balance
        
    def deposit(self,amount):
        self.account_balance += amount    
        
    def withdraw(self,amount):
        if self.account_balance < amount:
            return False
        else:
            return True
        
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")




