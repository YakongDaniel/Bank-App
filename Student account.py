StudentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0):
        super().__init__(account_number, holder_name, balance)
        self.withdrawal_limit = 2000
        self.deposit_limit = 50000
    
    def deposit(self, amount):
        if amount > self.deposit_limit:
            print(f"Cannot deposit more than {self.deposit_limit} at a time")
        else:
            super().deposit(amount)
        return self._balance
    
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Cannot withdraw more than {self.withdrawal_limit}")
        else:
            super().withdraw(amount)
        return self._balance
