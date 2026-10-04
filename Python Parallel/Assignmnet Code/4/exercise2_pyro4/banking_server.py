"""Pyro4 server for the Remote Banking & Wallet Service."""

import Pyro4


@Pyro4.expose
class BankAccountService:
    def __init__(self):
        self.balance = 1000.0
        self.transactions = ["Account opened with balance $1000.00"]

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "ERROR: Deposit amount must be greater than 0."

        self.balance += amount
        self.transactions.append(
            f"Deposited ${amount:.2f}; Balance: ${self.balance:.2f}"
        )
        return f"Deposit successful. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "ERROR: Withdrawal amount must be greater than 0."

        if amount > self.balance:
            return "ERROR: Insufficient funds."

        self.balance -= amount
        self.transactions.append(
            f"Withdrew ${amount:.2f}; Balance: ${self.balance:.2f}"
        )
        return f"Withdrawal successful. New balance: ${self.balance:.2f}"

    def get_statement(self):
        return list(self.transactions)


def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(BankAccountService())

    print("\nPYRO4 BANKING SERVER")
    print(f"Bank Service URI: {uri}")
    print("Keep this terminal running.")
    print("Start the client in another terminal and paste the URI above.\n")

    daemon.requestLoop()


if __name__ == "__main__":
    main()
