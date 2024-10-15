# Banking-system-using-Python
This is a mini project on Banking system programmed using python language.

INTRODUCTION

The Bank Account Management System is a simple, text-based software designed to help users manage their bank accounts, perform transactions such as deposits, withdrawals, and transfers, and keep track of their account balance and transaction history. This system is developed in Python and is a great demonstration of basic object-oriented programming concepts such as classes, objects, methods, and inheritance.

Objectives
The primary objectives of this project are:

To allow users to create and manage their bank accounts.
To enable users to log into their accounts securely using their account number and password.
To facilitate transactions like deposits, withdrawals, and transfers between accounts.
To provide users with the ability to view their account balance and transaction history.
Features
The system provides the following functionalities:

Account Creation: Users can create a new bank account by providing a unique account number and a password. This information is stored in the system and is used for future logins.

Login System: Users can log into their accounts using their account number and password. Once authenticated, they gain access to the functionalities related to their account.

Deposit: Users can deposit any positive amount into their account. The system validates that the deposit amount is positive and then adds it to the user’s balance.

Withdraw: Users can withdraw funds from their account as long as the amount requested does not exceed their current balance. The system validates the withdrawal amount to ensure it is within the available balance.

Balance Check: Users can check their current balance at any time during the session.

Transfer: Users can transfer money from their account to another account in the system. The transfer is only processed if the sender has enough funds and the recipient account exists.

Transaction History: The system records each transaction (deposit, withdrawal, and transfer) and provides the user with a detailed history of their transactions.

Logout: Users can securely log out of the system after completing their transactions.

Classes and Methods
The system has two main classes:

1. Transaction Class
Purpose: This class is responsible for storing the details of each transaction made by the user.
Attributes:
type: Type of transaction (Deposit, Withdrawal, Transfer, Received).
amount: Amount involved in the transaction.
2. BankAccount Class
Purpose: This class represents a user's bank account, storing the account number, password, balance, and the history of transactions.
Attributes:
account_number: Unique identifier for the account.
password: A string used for authentication.
balance: The current balance of the account.
transactions: A list to store all the transactions related to the account.
Methods:
deposit(amount): Allows the user to deposit money into the account.
withdraw(amount): Enables the user to withdraw money if they have sufficient balance.
check_balance(): Displays the current balance of the account.
transfer(amount, recipient_account): Facilitates the transfer of money between two accounts.
view_transactions(): Displays the transaction history of the account.
3. BankSystem Class
Purpose: This class manages the collection of all bank accounts and handles the account creation and login process.

Attributes:

accounts: A dictionary to store all accounts with the account number as the key.
Methods:

create_account(account_number, password): Creates a new bank account and stores it in the system.
login(account_number, password): Authenticates the user by verifying the account number and password.
Flow of the System
When the program is executed, the user is prompted to either create a new account or log in to an existing account.
After logging in, the user can perform several actions like depositing funds, withdrawing funds, transferring funds, checking the account balance, or viewing their transaction history.
The user can log out after completing their operations, and the session ends when they choose to exit.
System Testing
The system was tested with various scenarios to ensure that each function behaves as expected:

Account Creation: Multiple accounts were created with unique account numbers and passwords. Attempts to create duplicate accounts were rejected.
Login: Login attempts with incorrect account numbers or passwords were correctly denied.
Deposit & Withdraw: The system successfully updated balances and handled deposits and withdrawals, including edge cases like depositing/withdrawing zero or negative amounts.
Transfers: Transfers between accounts worked as expected, updating both sender’s and recipient’s balances.
Transaction History: The system correctly displayed the transaction history for each account.
Conclusion
This Bank Account Management System successfully implements core banking functionalities such as account creation, deposits, withdrawals, transfers, and transaction tracking in a simple and efficient manner. It is a good demonstration of object-oriented programming and provides a clear view of how banking systems handle account-related operations.

Future Enhancements
Some potential improvements to this project include:

Adding encryption for passwords to enhance security.
Introducing account types (e.g., savings, current) with specific rules.
Implementing a GUI for a more user-friendly interface.
Connecting the system to a database for persistent data storage.

