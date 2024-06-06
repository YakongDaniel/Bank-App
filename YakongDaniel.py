Class Account:
    def __init__(self, account_number, your_name, balance=0.0):
        self._account_number = account_number
        self._your_name = your_name
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
        return self._balance
    
    def get_balance(self):
        return self._balance
