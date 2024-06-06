#YakongDaniel
class Account:
    def __init__(self, account_number, your_name, balance=0.0):
        self._account_number = account_number
        self._holder_name = your_name
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

#JOYDOO
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

#samarimaryYP
class CurrentAccount(Account):
    def __init__(self, account_number, your_name, balance=0.0):
        super().__init__(account_number, your_name, balance)

# Kersedoo
class ChildrensAccount(Account):
    def __init__(self, account_number, your_name, balance=0.0):
        super().__init__(account_number, your_name, balance)
        self.interest_rate = 0.007
    
    def deposit(self, amount):
        self._balance += amount
        self._balance += amount * self.interest_rate
        return self._balance
    
    def withdraw(self, amount):
        print("Withdrawals are not allowed from Children's account")
        return self._balance

# David Afolabi
class StudentAccount(Account):
    def __init__(self, account_number, your_name, balance=0.0):
        super().__init__(account_number, your_name, balance)
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
