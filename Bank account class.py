class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

acc = BankAccount("Alice", 500)
acc.display()
acc.deposit(200)
acc.withdraw(100)
acc.display()
