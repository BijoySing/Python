class BankAccount:
    account_number = 100

    def __init__(self, name, email, address, account_type):
        BankAccount.account_number += 1 
        self.account_number = BankAccount.account_number 
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0 
        self.transaction_history = [] 
        self.loan_taken = 0  

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Withdrawal amount exceeded")
        elif self.balance == 0:
            print("Bank is bankrupt: No balance available to withdraw.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def show_transaction_history(self):
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions made yet.")

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += amount
            self.balance += amount
            self.transaction_history.append(f"Loan Taken: {amount}")
            print(f"Loan of {amount} taken. New balance: {self.balance}")
        else:
            print("Error: Loan limit exceeded. You can take a loan at most twice.")

    def transfer(self, amount, recipient_account):
        if amount > self.balance:
            print("Error: Insufficient balance.")
        elif recipient_account:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred {amount} to account {recipient_account.account_number}")
            recipient_account.transaction_history.append(f"Received {amount} from account {self.account_number}")
            print(f"Transferred {amount} to account {recipient_account.account_number}. New balance: {self.balance}")
        else:
            print("Error: Account does not exist")
