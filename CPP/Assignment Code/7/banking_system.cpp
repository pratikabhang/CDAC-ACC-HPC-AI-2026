#include <iostream>
#include <string>
#include <exception>
using namespace std;

class AccountException : public exception
{
private:
    string message;

public:
    AccountException(const string &msg) : message(msg) {}

    const char *what() const noexcept override
    {
        return message.c_str();
    }
};

class Account
{
public:
    int accountNo;
    string name;
    double balance;

    Account(int accountNo, string name, double balance)
    {
        if (accountNo <= 0)
            throw AccountException("Invalid Account Number");

        if (balance < 0)
            throw AccountException("Balance cannot be negative");

        this->accountNo = accountNo;
        this->name = name;
        this->balance = balance;
    }

    virtual ~Account() = default;

    void deposit(double amount)
    {
        if (amount <= 0)
            throw AccountException("Deposit amount must be greater than zero");

        balance += amount;
        cout << "Deposit successful\n";
    }

    virtual void withdraw(double amount) = 0;

    virtual void displayAccountDetails()
    {
        cout << "\nAccount No : " << accountNo;
        cout << "\nName : " << name;
        cout << "\nBalance : " << balance << endl;
    }
};

class SavingsAccount : public Account
{
private:
    double interestRate;

public:
    SavingsAccount(int accountNo, string name, double balance, double interestRate)
        : Account(accountNo, name, balance)
    {
        this->interestRate = interestRate;
    }

    void withdraw(double amount) override
    {
        if (amount <= 0)
            throw AccountException("Withdraw amount must be greater than zero");

        if (amount > balance)
            throw AccountException("Withdrawal amount is greater than available balance");

        if (balance - amount < 500)
            throw AccountException("Savings Account must maintain minimum balance of 500");

        balance -= amount;
        cout << "Savings Account withdrawal successful\n";
    }

    void displayAccountDetails() override
    {
        cout << "\nAccount Type : Savings Account";
        Account::displayAccountDetails();
        cout << "Interest Rate : " << interestRate << "%\n";
    }
};

class CurrentAccount : public Account
{
private:
    double maintenanceFee;

public:
    CurrentAccount(int accountNo, string name, double balance, double maintenanceFee)
        : Account(accountNo, name, balance)
    {
        this->maintenanceFee = maintenanceFee;
    }

    void withdraw(double amount) override
    {
        if (amount <= 0)
            throw AccountException("Withdraw amount must be greater than zero");

        if (amount > balance)
            throw AccountException("Withdrawal amount is greater than available balance");

        balance -= amount;
        cout << "Current Account withdrawal successful\n";
    }

    void displayAccountDetails() override
    {
        cout << "\nAccount Type : Current Account";
        Account::displayAccountDetails();
        cout << "Maintenance Fee : " << maintenanceFee << "\n";
    }
};

int main()
{
    Account *accounts[10] = {nullptr};
    int count = 0;
    int choice;

    do
    {
        cout << "\n===== BANKING MANAGEMENT SYSTEM =====";
        cout << "\n1. Create Account";
        cout << "\n2. Deposit";
        cout << "\n3. Withdraw";
        cout << "\n4. Display All Accounts";
        cout << "\n5. Exit";
        cout << "\nEnter choice: ";
        cin >> choice;

        try
        {
            switch (choice)
            {
            case 1:
            {
                if (count >= 10)
                    throw AccountException("Cannot create more than 10 accounts");

                int accountNo, type;
                string name;
                double balance;

                cout << "Enter Account Number: ";
                cin >> accountNo;

                if (accountNo <= 0)
                    throw AccountException("Invalid Account Number");

                for (int i = 0; i < count; i++)
                {
                    if (accounts[i]->accountNo == accountNo)
                        throw AccountException("Account number already exists");
                }

                cout << "Enter Customer Name: ";
                cin >> name;

                cout << "Enter Initial Balance: ";
                cin >> balance;

                if (balance < 0)
                    throw AccountException("Balance cannot be negative");

                cout << "\n1. Savings Account";
                cout << "\n2. Current Account";
                cout << "\nEnter Account Type: ";
                cin >> type;

                if (type == 1)
                {
                    if (balance < 500)
                        throw AccountException("Savings Account must maintain minimum balance of 500");

                    double interestRate;
                    cout << "Enter Interest Rate (%): ";
                    cin >> interestRate;

                    if (interestRate < 0)
                        throw AccountException("Interest rate cannot be negative");

                    accounts[count] = new SavingsAccount(accountNo, name, balance, interestRate);
                    cout << "\nSavings Account created successfully\n";
                    count++;
                }
                else if (type == 2)
                {
                    double maintenanceFee;
                    cout << "Enter Maintenance Fee: ";
                    cin >> maintenanceFee;

                    if (maintenanceFee < 0)
                        throw AccountException("Maintenance fee cannot be negative");

                    accounts[count] = new CurrentAccount(accountNo, name, balance, maintenanceFee);
                    cout << "\nCurrent Account created successfully\n";
                    count++;
                }
                else
                {
                    throw AccountException("Invalid Account Type");
                }
                break;
            }

            case 2:
            {
                int accountNo;
                double amount;

                cout << "Enter Account Number: ";
                cin >> accountNo;

                cout << "Enter Deposit Amount: ";
                cin >> amount;

                int found = 0;
                for (int i = 0; i < count; i++)
                {
                    if (accounts[i]->accountNo == accountNo)
                    {
                        accounts[i]->deposit(amount);
                        found = 1;
                        break;
                    }
                }

                if (!found)
                    throw AccountException("Account not found");
                break;
            }

            case 3:
            {
                int accountNo;
                double amount;

                cout << "Enter Account Number: ";
                cin >> accountNo;

                cout << "Enter Withdrawal Amount: ";
                cin >> amount;

                int found = 0;
                for (int i = 0; i < count; i++)
                {
                    if (accounts[i]->accountNo == accountNo)
                    {
                        accounts[i]->withdraw(amount);
                        found = 1;
                        break;
                    }
                }

                if (!found)
                    throw AccountException("Account not found");
                break;
            }

            case 4:
            {
                if (count == 0)
                {
                    cout << "No accounts available\n";
                }
                else
                {
                    for (int i = 0; i < count; i++)
                    {
                        accounts[i]->displayAccountDetails();
                    }
                }
                break;
            }

            case 5:
                cout << "Thank you for using Banking Management System!\n";
                break;

            default:
                throw AccountException("Invalid choice");
            }
        }
        catch (const AccountException &e)
        {
            cout << "\nError: " << e.what() << endl;
        }
        catch (const exception &e)
        {
            cout << "\nError: " << e.what() << endl;
        }

    } while (choice != 5);

    for (int i = 0; i < count; i++)
    {
        delete accounts[i];
    }

    return 0;
}