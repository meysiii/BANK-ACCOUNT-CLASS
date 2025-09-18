# 🏦 Bank Account Management System (Python OOP)

Author : M.S.MEYSINTHA

A Python-based Bank Account simulation project built using Object-Oriented Programming (OOP) concepts.
This project demonstrates how a simple banking system works, including account creation, deposits, withdrawals, and balance inquiry.

It is an educational project to understand classes, objects, methods, and encapsulation in Python.

# 📌 Features

✅ Create a bank account with account holder details
✅ Deposit money into the account
✅ Withdraw money with balance validation
✅ Check account balance anytime
✅ Display account details (Name, Account Number, Balance)
✅ Beginner-friendly Python OOP example

# 📜 Code Example
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited {amount}. New Balance: {self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ Withdrawn {amount}. New Balance: {self.balance}")
            else:
                print("❌ Insufficient funds.")
        else:
            print("❌ Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"💰 Account Balance: {self.balance}")

    def account_details(self):
        print("\n📑 Account Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Example Usage
account = BankAccount("12345", "Meysintha", 1000)
account.account_details()
account.deposit(500)
account.withdraw(300)
account.display_balance()

# ▶️ Example Run
📑 Account Details:
Account Number: 12345
Account Holder: Meysintha
Balance: 1000

✅ Deposited 500. New Balance: 1500
✅ Withdrawn 300. New Balance: 1200
💰 Account Balance: 1200

# ⚡ How to Run

Clone this repository:

git clone https://github.com/your-username/bank-account-class.git
cd bank-account-class


# Run the program:

python bank_account.py

# output



# 🚀 Future Improvements

Add PIN-based authentication system

Support multiple user accounts in a single run

Maintain a transaction history log

Connect with a database (SQLite/MySQL) for persistent storage

Build a GUI version using Tkinter or PyQt
