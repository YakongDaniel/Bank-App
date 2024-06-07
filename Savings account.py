class SavingsAccount(Account):
    def __init__(self, account_number, your_name, balance=0.0):
        super().__init__(account_number, your_name, balance)
        self.interest_rate = 0.005
        self.withdrawal_limit = 700000
    
    def deposit(self, amount):
        self._balance += amount
        self._balance += amount * self.interest_rate
        return self._balance
    
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Cannot withdraw more than {self.withdrawal_limit}")
        else:
            super().withdraw(amount)
        return self._balance
