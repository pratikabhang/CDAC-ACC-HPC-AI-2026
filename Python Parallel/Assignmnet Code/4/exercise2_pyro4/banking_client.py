"""Interactive Pyro4 client for the Remote Banking & Wallet Service."""

import Pyro4


def print_menu():
    print("\n" + "=" * 50)
    print("PYRO4 REMOTE BANKING SERVICE (CLI)")
    print("=" * 50)
    print("1. Check Current Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction Statement")
    print("5. Exit Application")
    print("-" * 50)


def main():
    uri = input("Enter Bank Service URI (or paste from server): ").strip()
    bank = Pyro4.Proxy(uri)

    try:
        while True:
            print_menu()
            choice = input("Enter your choice [1-5]: ").strip()

            try:
                if choice == "1":
                    print(f"Current Balance: ${bank.get_balance():,.2f}")

                elif choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    print(bank.deposit(amount))

                elif choice == "3":
                    amount = float(input("Enter withdrawal amount: "))
                    print(bank.withdraw(amount))

                elif choice == "4":
                    statement = bank.get_statement()
                    print("\nTRANSACTION STATEMENT")
                    if not statement:
                        print("No transactions found.")
                    else:
                        for number, transaction in enumerate(statement, 1):
                            print(f"{number}. {transaction}")

                elif choice == "5":
                    print("Thank you for using the Remote Banking Service.")
                    break

                else:
                    print("Invalid choice. Please select 1-5.")

            except ValueError:
                print("Invalid number. Please enter a valid numeric amount.")

    except Pyro4.errors.CommunicationError:
        print("ERROR: Could not communicate with the Pyro4 server.")
    finally:
        bank._pyroRelease()


if __name__ == "__main__":
    main()
