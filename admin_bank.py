import uuid
from datetime import datetime

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, user):
        initial_balance = 10000
        self.accounts[account_number] = Account(account_number, user, initial_balance)

    def authenticate_user(self, account_number, pin):
        if account_number in self.accounts:
            return self.accounts[account_number].authenticate(pin)
        else:
            return False

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None

    def update_account(self, account_number, user):
        if account_number in self.accounts:
            self.accounts[account_number].update_user(user)
            return True
        else:
            return False

    def admin_interface(self):
        print("Welcome to Admin Interface")
        print("Total Number of Accounts:", len(self.accounts))
        for account_number, account in self.accounts.items():
            print("Account Number:", account_number)
            print("User Details:", account.user.__dict__)
            print("Balance:", account.balance)
            print("Transaction History:", account.transactions)
            print("")


class Account:
    def __init__(self, account_number, user, balance=10000):
        self.account_number = account_number
        self.user = user
        self.balance = balance
        self.transactions = []

    def authenticate(self, pin):
        return self.user.check_pin(pin)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((datetime.now(), 'Deposit', amount))

    def withdraw(self, amount):
        if self.balance - amount >= 2000:
            self.balance -= amount
            self.transactions.append((datetime.now(), 'Withdrawal', amount))
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def update_user(self, user):
        self.user = user


class User:
    def __init__(self, name, address, contact, pin):
        self.name = name
        self.address = address
        self.contact = contact
        self.pin = pin

    def check_pin(self, pin):
        return self.pin == pin

    def update_details(self, name=None, address=None, contact=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if contact:
            self.contact = contact


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Create Account")
        print("2. Login")
        print("3. Admin Interface")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            contact = input("Enter your contact number: ")
            pin = input("Enter your 4-digit PIN: ")

            account_number = input("Enter your desired account number: ")
            user = User(name, address, contact, pin)
            bank.create_account(account_number, user)
            print("Account created successfully!")

        elif choice == "2":
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            if bank.authenticate_user(account_number, pin):
                while True:
                    print("\nLogged in successfully!")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Update Details")
                    print("6. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        amount = float(input("Enter the amount to deposit: "))
                        bank.get_account(account_number).deposit(amount)
                        print("Deposit successful.")

                    elif user_choice == "2":
                        amount = float(input("Enter the amount to withdraw: "))
                        if bank.get_account(account_number).withdraw(amount):
                            print("Withdrawal successful.")
                        else:
                            print("Insufficient funds.")

                    elif user_choice == "3":
                        balance = bank.get_account(account_number).get_balance()
                        print("Your account balance is:", balance)

                    elif user_choice == "4":
                        history = bank.get_account(account_number).get_transaction_history()
                        print("Transaction History:")
                        for transaction in history:
                            print(transaction)

                    elif user_choice == "5":
                        name = input("Enter your updated name (press enter to skip): ")
                        address = input("Enter your updated address (press enter to skip): ")
                        contact = input("Enter your updated contact number (press enter to skip): ")
                        bank.get_account(account_number).user.update_details(name, address, contact)
                        print("Details updated successfully.")

                    elif user_choice == "6":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid account number or PIN.")

        elif choice == "3":
            admin_password = input("Enter admin password: ")
            if admin_password == "admin":
                bank.admin_interface()
            else:
                print("Incorrect admin password.")

        elif choice == "4":
            print("Thank you for using our banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
