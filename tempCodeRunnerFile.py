############################################################
# Name: Bhim Raj Rai
# Section: B.E First Electrical Engineering
# Student ID Number: 02230056
############################################################

# References:
# https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
# https://www.w3resource.com/python-exercises/class-exercises/python-class-real-life-problem-3.php
# https://youtu.be/3Jt60NWcchE?si=lytfhQ1x-kd9w5Gv
# https://youtu.be/BRssQPHZMrc?si=1NuJnKO_ASE3eGKK
# https://gist.github.com/Edgars-Duka/feae5c1fe986a5cf69ccd39b96619332
###########################################################################################################

# Solution

import random
import json
import os
import datetime

# Define Account Class
class Account:
    def __init__(self, account_number, password, account_type, balance=0.0):
        self.account_number = account_number  # Initialize account number
        self.password = password  # Initialize password
        self.account_type = account_type  # Initialize account type
        self.balance = balance  # Initialize balance
        self.statement = []  # Initialize account statement

    def deposit(self, amount):
        self.balance += amount  # Add the deposit amount to the balance
        self.statement.append(f"{datetime.datetime.now()} - Deposited: {amount}")  # Add to statement
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")  # Print message if withdrawal amount exceeds balance
        else:
            self.balance -= amount  # Subtract the withdrawal amount from the balance
            self.statement.append(f"{datetime.datetime.now()} - Withdrew: {amount}")  # Add to statement
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        return self.balance  # Return the current balance

    def update_password(self, new_password):
        self.password = new_password  # Update password
        print("Password updated successfully.")

    def print_statement(self):
        print("\nAccount Statement:")
        for entry in self.statement:
            print(entry)

# Define PersonalAccount Class
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0.0):
        super().__init__(account_number, password, "Personal", balance)  # Initialize with "Personal" account type

# Define BusinessAccount Class
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0.0):
        super().__init__(account_number, password, "Business", balance)  # Initialize with "Business" account type

# Helper functions to handle file operations
def load_accounts(filename="accounts.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)  # Load accounts from file if it exists
    return {}

def save_accounts(accounts, filename="accounts.txt"):
    with open(filename, "w") as file:
        json.dump(accounts, file, indent=4)  # Save accounts to file

# Generate a random account number
def generate_account_number():
    return str(random.randint(10000000, 99999999))  # Generate an 8-digit account number

# Generate a default password
def generate_default_password():
    return str(random.randint(1000, 9999))  # Generate a 4-digit default password

# Main banking application logic
class BankingApplication:
    def __init__(self):
        self.accounts = load_accounts()  # Load existing accounts from file

    def open_account(self, account_type):
        account_number = generate_account_number()  # Generate a new account number
        password = generate_default_password()  # Generate a new password
        if account_type == "Personal":
            account = PersonalAccount(account_number, password)  # Create a personal account
        elif account_type == "Business":
            account = BusinessAccount(account_number, password)  # Create a business account
        else:
            print("Invalid account type.")
            return
        
        self.accounts[account_number] = {
            "password": password,
            "account_type": account.account_type,
            "balance": account.balance,
            "statement": account.statement
        }
        save_accounts(self.accounts)  # Save the new account to file
        print(f"Account created successfully. Account Number: {account_number}, Password: {password}")

    def login(self, account_number, password):
        account_info = self.accounts.get(account_number)
        if account_info and account_info["password"] == password:
            if account_info["account_type"] == "Personal":
                account = PersonalAccount(account_number, password, account_info["balance"])
            elif account_info["account_type"] == "Business":
                account = BusinessAccount(account_number, password, account_info["balance"])
            account.statement = account_info.get("statement", [])
            return account
        print("Invalid account number or password.")
        return None

    def transfer_money(self, from_account, to_account_number, amount):
        if from_account.balance < amount:
            print("Insufficient funds.")
            return
        to_account_info = self.accounts.get(to_account_number)
        if not to_account_info:
            print("Receiving account does not exist.")
            return
        from_account.withdraw(amount)  # Withdraw the amount from the sender's account
        to_account_info["balance"] += amount  # Deposit the amount to the receiver's account
        from_account.statement.append(f"{datetime.datetime.now()} - Transferred: {amount} to {to_account_number}")
        self.accounts[to_account_number] = to_account_info  # Update the receiver's account info
        save_accounts(self.accounts)  # Save updated accounts to file
        print(f"Transferred {amount} to account {to_account_number}.")

    def delete_account(self, account):
        del self.accounts[account.account_number]  # Remove the account from the accounts dictionary
        save_accounts(self.accounts)  # Save updated accounts to file
        print(f"Account {account.account_number} deleted successfully.")

# Run the banking application
def main():
    app = BankingApplication()
    while True:
        print("\nBanking System")
        print("1. Open Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\n1. Personal Account\n2. Business Account")
            account_type = input("Select account type: ")
            if account_type == "1":
                app.open_account("Personal")
            elif account_type == "2":
                app.open_account("Business")
            else:
                print("Invalid account type.")
        elif choice == "2":
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = app.login(account_number, password)
            if account:
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Transfer Money")
                    print("5. Delete Account")
                    print("6. Update Password")
                    print("7. Print Statement")
                    print("8. Logout")
                    action = input("Enter your choice: ")
                    if action == "1":
                        print(f"Balance: {account.check_balance()}")
                    elif action == "2":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                        app.accounts[account.account_number]["balance"] = account.balance
                        save_accounts(app.accounts)
                    elif action == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                        app.accounts[account.account_number]["balance"] = account.balance
                        save_accounts(app.accounts)
                    elif action == "4":
                        to_account_number = input("Enter the account number to transfer to: ")
                        amount = float(input("Enter amount to transfer: "))
                        app.transfer_money(account, to_account_number, amount)
                        app.accounts[account.account_number]["balance"] = account.balance
                        save_accounts(app.accounts)
                    elif action == "5":
                        confirm = input("Are you sure you want to delete this account? (yes/no): ")
                        if confirm.lower() == "yes":
                            app.delete_account(account)
                            break
                    elif action == "6":
                        new_password = input("Enter new password: ")
                        account.update_password(new_password)
                        app.accounts[account.account_number]["password"] = new_password
                        save_accounts(app.accounts)
                    elif action == "7":
                        account.print_statement()
                    elif action == "8":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
