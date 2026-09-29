class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            print("Deposit successful")
        else:
            print("Deposit amount must be greater than zero")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def check_balance(self):
        print("Current balance:", self.balance)

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)


def main():
    account_number = input("Enter account number: ")
    customer_name = input("Enter customer name: ")
    balance = float(input("Enter opening balance: "))

    account = BankAccount(account_number, customer_name, balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.deposit()
        elif choice == "2":
            account.withdraw()
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.display_details()
        elif choice == "5":
            print("Thank you")
            break
        else:
            print("Invalid choice")


main()