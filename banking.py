# For transactions

class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

# for bank account related process

class BankAccount:
    def __init__(self,account_number,password):
        self.account_number = account_number
        self.password = password
        self.balance = 0
        self.transactions = []

    # for depositing amount to bank account

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit", amount))
            print(f"${amount} Successfully credited to Account. New balance is ${self.balance}")
        else:
            print("The given amount is not valid. Try a positive number.")

    # for withdrawing amount from bank account

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
            print(f"${amount} has been Successfully withdrawn. New balance is ${self.balance}")
        else:
            print("Insufficient fund or Invalid amount")

    # for checking balance

    def check_balance(self,):
        print(f"Your balance is ${self.balance}")

    # For transfer

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transactions.append(Transaction("Transfer " ,amount))
            recipient_account.transactions.append(Transaction("Received ",amount))
            print(f"Successfully transferred ${amount} to ${recipient_account.account_number}.")
        else:
            print("Insufficient Balance or Invalid amount.")

    # For viewing transactions

    def view_transactions(self):
        print(f"Transactions of {self.account_number}: ")
        for transaction in self.transactions:
            print(f"{transaction.type}: ${transaction.amount}")

# for account creation and login

class BankSystem:
    def __init__(self):
        self.accounts = {}

    # for account creation

    def create_account(self, account_number, password):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number,password)
            print(f"Account created Successfully for {account_number}")
        else:
            print("Account already exists.")

    # for logging in

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            print(f"Login Successful for {account_number}.")
            return account
        else:
            print("Login Failed. Check account number and password again.")
            return None

# Main Function
def Main():
    bank_system = BankSystem()

    while True:
        print("\nWelcome to Banking")
        print("1. Create an Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        # creating account
        if choice == '1':
            acc_num = input("Enter Account Number: ")
            pwd = input("Enter your Password: ")
            bank_system.create_account(acc_num, pwd)

        # Login
        elif choice == '2':
            acc_num = input("Enter Account Number: ")
            pwd = input("Enter your Password: ")
            account = bank_system.login(acc_num, pwd)

            # For selecting Deposit/ Withdraw/ Check balance
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transfer")
                    print("5. View Transactions")
                    print("6. Log out")
                    action = input("Choose an Action")

                    # for Deposit
                    if action == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)

                    # for Withdraw
                    elif action == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)

                    # for checking Balance
                    elif action == '3':
                        account.check_balance()

                    # For transfer
                    elif action == '4':
                        recipient_account_number = input("Enter recipient Account Number: ")
                        recipient_account = bank_system.accounts.get(recipient_account_number)
                        if recipient_account:
                            amount = float(input("Enter Amount to transfer: "))
                            account.transfer(amount, recipient_account)
                        else:
                            print("Recipient Account Does not Exist.")

                    # For viewing Transactions
                    elif action == '5':
                        account.view_transactions()

                    # For Log out
                    elif action == '6':
                        print("Logging Out.")
                        break

                    # For other Values
                    else:
                        print("Invalid Input. Please try again.")

        # For Exiting Bank System
        elif choice == '3':
            print("Exiting Banking System. ")
            break

        # For other choices
        else:
            print("Invalid choice. Try again.")

Main()





