BINGHAM BANK APP

 
 Example usage:
savings = SavingsAccount(123, "Alice", 1000)
savings.deposit(5000)
print(savings.get_balance())  # Should reflect interest on deposit
savings.withdraw(800000)  # Should fail due to withdrawal limit
print(savings.get_balance())

current = CurrentAccount(124, "Bob", 2000)
current.deposit(500)
current.withdraw(3000)
print(current.get_balance())

child = ChildrensAccount(125, "Charlie", 500)
child.deposit(500)
child.withdraw(100)  # Should print a message indicating withdrawals are not allowed
print(child.get_balance())

student = StudentAccount(126, "David", 100)
student.deposit(60000)  # Should fail due to deposit limit
student.withdraw(2500)  # Should fail due to withdrawal limit
print(student.get_balance())

