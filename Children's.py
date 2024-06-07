class Childrensaccount(Account):
    def __init__(self, account_number, your_name, balance=0.0):
        super().__init__(account_number, your_name, balance)
        self.interest_rate = 0.007
    
    def deposit(self, amount):
        self.balance += amount
        interest_earned = amount * self.interest_rate
        self.balance += interest_earned
        return self.balance
    
    def withdraw(self, amount):
        print("Withdrawals are not allowed from Children's account")
        return self._balance

