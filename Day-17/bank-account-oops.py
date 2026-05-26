# If you wana generate IBAN from a python package https://schwifty.readthedocs.io/en/latest/examples.html#generation
import random
from datetime import datetime
class BankAccount:
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



account1 = BankAccount("Mike", 2000)
account2 = BankAccount("Paraj", 3000)

account1.activate_account()
account1.deposit(300)

account1.withdraw(100)
account1.account_info()


account2.deposit(500)
account2.withdraw(300)
account2.withdraw(100)
account2.account_info()





