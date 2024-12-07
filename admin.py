
from user import BankAccount

class Admin:
    def __init__(self):
        self.users = []
        self.bank_balance = 0
        self.total_loans = 0
        self.loan_feature_enabled = False


    def create_account(self, name, email, address, account_type):
        user = BankAccount(name, email, address, account_type)
        self.users.append(user)
        print(f"Account created successfully for {name} with account number {user.account_number}")

    def delete_account(self, account_number):
        user_to_delete = None
        for user in self.users:
            if user.account_number == account_number:
                user_to_delete = user
                break
        if user_to_delete:
            self.users.remove(user_to_delete)
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account not found.")

    def view_all_users(self):
        if self.users:
            for user in self.users:
                print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.balance}")
        else:
            print("No users found.")

    def check_bank_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total bank balance: {total_balance}")
        return total_balance

    def check_total_loans(self):
        total_loans = sum(user.loan_taken for user in self.users)
        print(f"Total loan amount: {total_loans}")
        return total_loans

    def toggle_loan_feature(self, status):
        self.loan_feature_enabled = status        
        if status:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")