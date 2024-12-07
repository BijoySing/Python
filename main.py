
from user import BankAccount
from admin import Admin

def user_menu(user_account, admin):
    while True:
        print("\nUser Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            user_account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            user_account.withdraw(amount)
        elif choice == 3:
            user_account.check_balance()
        elif choice == 4:
            user_account.show_transaction_history()
        elif choice == 5:
            user_account.take_loan(admin)
        elif choice == 6:
            recipient_account_number = int(input("Enter recipient account number: "))
            recipient_account = None
            for account in admin.users:
                if account.account_number == recipient_account_number:
                    recipient_account = account
                    break
            amount = float(input("Enter amount to transfer: "))
            user_account.transfer(amount, recipient_account)
        elif choice == 7:
            break
        else:
            print("Invalid choice! Please try again.")

def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. View All Users")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loans")
        print("6. Toggle Loan Feature")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter account type (Savings/Current): ")
            admin.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account number to delete: "))
            admin.delete_account(account_number)
        elif choice == 3:
            admin.view_all_users()
        elif choice == 4:
            admin.check_bank_balance()
        elif choice == 5:
            admin.check_total_loans()
        elif choice == 6:
            print("1. Enable")
            print("2. Disable")
            status = int(input("Enter status: "))
            if status == 1:
                admin.toggle_loan_feature(True)
            elif status == 2:
                admin.toggle_loan_feature(False)
        elif choice == 7:
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    admin = Admin()
    admin.create_account("Joy", "joy@email.com", "Dhaka", "Savings")
    admin.create_account("Ajoy", "ajoy@email.com", "Sylhet", "Current")


    while True:
        print("\nMain Menu:")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            account_number = int(input("Enter account number: "))
            user_account = None
            for account in admin.users:
                if account.account_number == account_number:
                    user_account = account
                    break
            if user_account:
                user_menu(user_account, admin)
            else:
                print("Account not found.")
        elif choice == 2:
            print("Admin Login:")
            admin_menu(admin)
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please try again.")
