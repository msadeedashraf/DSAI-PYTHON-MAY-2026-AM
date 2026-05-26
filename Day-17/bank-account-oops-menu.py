# If you wana generate IBAN from a python package https://schwifty.readthedocs.io/en/latest/examples.html#generation
# OOPs Bank Account with Menu

import random
from datetime import datetime

class BankAccount:
    global bank_name 
    bank_name = "SADEED NATIONAL BANK"

    def __init__  (self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_number = self.generate_iban()
        self.creation_date = datetime.now()
        self.is_active = False


    def generate_iban(self):
        country_code = "CA"
        check_digits = str(random.randint(10, 99))
        bank_identifier = "BANK"
        account_number = str(random.randint(10000000, 99999999))
        return f"{country_code}{check_digits}{bank_identifier}{account_number}"
    
    def activate_account(self):
        self.is_active = True
        print(f"Account {self.account_number} is activated")


    def de_activate_account(self):
        self.is_active = False
        print(f"Account {self.account_number} is deactivated")

# cls @classmethod
    @classmethod
    def open_account(cls):
        print(f"Welcome to {bank_name}\n Let's open a new account.")
        
        name = input("Enter your Name: ")
        user_balance =  float(input("Enter the inital deposit amount: "))
        opening_balance =  user_balance if user_balance else 0

        account = cls(name, opening_balance)

        print(f"|n Account created successfully!")
        print(f"{account.account_holder_name}'s account number is {account.account_number}")
        print(f"Account no is currently inactive. Please activate the account")

        return account



        


    def deposit(self, amount):
        if self.is_active == False:
            return print(f"{self.account_holder_name}'s account is not active. \n Please contact the branch before the deposit")

        if amount <= 0:
            print("Deposit amount can not be equal to zero")
            return
        
        self.balance += amount

        print(f"Deposited : {amount}")
        print(f"New Balance : {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        
        fee = 2
        amount += fee 
        self.balance -= amount
        print(f"Withdraw: {amount}")
        print(f"New Balance : {self.balance}")

    def check_balance(self):
        print(f"Curent Balance of {self.account_holder_name} is {self.balance}")


    def account_info(self):
        print("\n========== ACCOUNT INFO ==========")
        print(f"Account Number      : {self.account_number}")
        print(f"Account Holder Name : {self.account_holder_name}")
        print(f"Balance             : ${self.balance:.2f}")
        print(f"Creation Date       : {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Account Active      : {self.is_active}")
        print("==================================")



# account1 = BankAccount("Mike", 2000)
# account2 = BankAccount("Paraj", 3000)

# account1.activate_account()
# account1.deposit(300)

# account1.withdraw(100)
# account1.account_info()


# account2.deposit(500)
# account2.withdraw(300)
# account2.withdraw(100)
# account2.account_info()



def main():
    account = None

    while True:
        print("\n=========== BANK ACCOUNT ==============")
        print("1. Open Account")       
        print("2. Activate the account")       
        print("3. Deactivate the account")               
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Show Balance")
        print("7. Show Acount Info")
        print("8. Quit")
        print("=======================================")

        choice = input("Select an option: ")
        
        
        if choice == "1":
            account = BankAccount.open_account()

        elif choice == "2":
            if account is None:
                print("Please open an account first")
            else:
                account.activate_account()
        
        elif choice == "3":
            if account is None:
                print("Please open an account first")
            else:
                account.de_activate_account()
        
        elif choice == "4":
            if account is None:
                print("Please open an account first")
            else:
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
            
        elif choice == "5":
            if account is None:
                print("Please open an account first")
            else:
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)

        elif choice == "6":
            if account is None:
                print("Please open an account first")
            else:
                account.check_balance()

        elif choice == "7":
            if account is None:
                print("Please open an account first")
            else:
                account.account_info()
                
        elif choice == "8":
            print("\nThank you for using our bank.")
            break

        else:
            print("\nInvalid option. Please try again.")


main()

