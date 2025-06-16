# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")

import sys

def main():
    account = BankAccount(100) # Initial balance

    if len(sys.argv) > 2:
        print("Usage: python main-0.py <commands>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    if len(sys.argv) > 1:
        # Split command and amount
        command_parts = sys.argv[1].split(':')
        command = command_parts[0]
        amount = float(command_parts[1]) if len(command_parts) > 1 else 0

        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")
    else:
        print("No command provided.")

if __name__ == "__main__":
    main()
                            