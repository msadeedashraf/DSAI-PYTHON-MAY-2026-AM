# If you wana generate IBAN from a python package https://schwifty.readthedocs.io/en/latest/examples.html#generation
# OOPs Bank Account with Menu
#How to have multiple accounts
# Implement the list for holding transactions
# Implement inheritance (Saving and Chequing Account)
# Implement Overriding



import random
from datetime import datetime

class BankAccount:
    global bank_name 
    bank_name = "SADEED NATIONAL BANK"
    transactions = []          # LIST: stores all transaction dictionaries
    transaction_types = set()  # SET: stores unique transaction types only

    def __init__  (self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance        
        self.account_number = self.generate_iban()
        self.transactions = []
        self.creation_date = datetime.now()
        self.account_type = "Regular Account"
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
        user_balance =  input("Enter the inital deposit amount: ").strip()
        
        opening_balance =  float(user_balance) if user_balance else 0      

        
        account_type_choice = input("Enter the Account type")  
        print("\nSelect Account Type:")
        print("\n1. Saving Account")
        print("\n2. Chequing Account")


        if account_type_choice == "1":
            account = SavingsAccount(name,opening_balance)
        
        elif account_type_choice == "2":
            account = ChequingAccount(name,opening_balance)
        else:
            print(f"Invalid Choice. Creating a regular Bank Account.")
            account = BankAccount(name,opening_balance)

        print(f"\n Account created successfully!")
        print(f"{account.account_holder_name}'s account number is {account.account_number}")
        print(f"Account no is currently inactive. Please activate the account")

        return account


    def get_timstamp(self):
        current_time = datetime.now()

        timestamp = (
        current_time.strftime("%Y-%m-%d"), # Date part from the current date
        current_time.strftime("%I:%M:%S") # Time Part from the current date

            )
        return timestamp
        


    def deposit(self, amount):
        if self.is_active == False:
            return print(f"{self.account_holder_name}'s account is not active. \n Please contact the branch before the deposit")

        if amount <= 0:
            print("Deposit amount can not be equal to zero")
            return
        
        self.balance += amount

        timestamp = self.get_timstamp()

         # Dictionary
        transaction = {
        'type':'Deposit',
        'date':timestamp[0],
        'time': timestamp[1],
        'money_in': amount,
        'money_out':0,
        'balance': self.balance
        }
        
        self.transactions.append(transaction)

        print(f"Dposited : {amount} successfully." ) 
        print(f"New Balance for {self.account_holder_name} : {self.balance}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        
        self.balance -= amount

        timestamp = self.get_timstamp()
         # Dictionary
        transaction = {
            'type':'Withdrawal',
            'date':timestamp[0],
            'time': timestamp[1],
            'money_in': 0,
            'money_out':amount,
            'balance': self.balance
        }

        self.transactions.append(transaction)

        print(f"Withdraw : {amount}")
        print(f"New Balance is : {self.balance}")

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

        # =========================================================
    # FUNCTION: SHOW STATEMENT ON SCREEN
    # =========================================================
    def show_statement(self):
                
        if len(self.transactions) == 0:
            print("\nNo transactions to display.")
            return

        print("\n==============================================================")
        print(f"                     {bank_name}                               ")
        print("================================================================")

        print(
            f"{'Date':<12}"
            f"{'Time':<12}"
            f"{'Description':<15}"
            f"{'Money In':>12}"
            f"{'Money Out':>12}"
            f"{'Balance':>12}"
        )

        print("-" * 75)

        for transaction in self.transactions:
            print(
                f"{transaction['date']:<12}"
                f"{transaction['time']:<12}"
                f"{transaction['type']:<15}"
                f"${transaction['money_in']:>11.2f}"
                f"${transaction['money_out']:>11.2f}"
                f"${transaction['balance']:>11.2f}"
            )

        print("-" * 75)
        print(f"{'Closing Balance':>63}: ${self.balance:.2f}")


def find_account(accounts):
    account_number = input("Enter the account number")
    if account_number in accounts:
        return accounts[account_number]
    else:
        print("Account Not found, check your account number")
        return None

def list_allaccounts(accounts):
    if len(accounts) == 0:
        print(f"No account found")
        return
    
    print(f"\n===============ALL Accounts=============")
    for account_number, account in accounts.items():
        print(f"{account_number} | {account.account_holder_name} | {account.balance} | Active: {account.is_active} | Account Type: {account.account_type}")
    print(f"\n========================================")

    return

class SavingsAccount(BankAccount):
    def __init__(self, account_holder_name, balance, interest_rate=0.03):
        super().__init__(account_holder_name, balance)

        self.interest_rate = interest_rate
        self.account_type = "Savings Account"


    def add_interest(self):
        if not self.is_active:
            print("Account must be active before adding interest.")
            return
        
        interest = self.balance * self.interest_rate
        self.balance += interest

        timestamp = self.get_timstamp()
         # Dictionary
        transaction = {
            'type':'Iterest',
            'date':timestamp[0],
            'time': timestamp[1],
            'money_in': interest,
            'money_out':0,
            'balance': self.balance
        }

        self.transactions.append(transaction)

        print(f"Interest Added : {interest}")
        print(f"New Balance is : {self.balance}")



class ChequingAccount(BankAccount):
    def __init__(self, account_holder_name, balance, withdrwal_fee = 4):
        super().__init__(account_holder_name, balance)
        self.account_type = "Chequing Account"
        self.withdrawal_fee = withdrwal_fee
        

    def withdraw(self, amount):
        if not self.is_active:
            print("Account must be active before withdrawing")
            return
        
        total_amount = amount + self.withdrawal_fee
        
        if total_amount > self.balance:
            print("Insufficient funds")
            return
        
        self.balance -= total_amount

        timestamp = self.get_timstamp()
         # Dictionary
        transaction = {
            'type':'Withdrawal',
            'date':timestamp[0],
            'time': timestamp[1],
            'money_in': 0,
            'money_out':total_amount,
            'balance': self.balance
        }

        self.transactions.append(transaction)

        print(f"Withdraw : {amount} successfully")
        print(f"Fee applied : {self.withdrawal_fee}")
        print(f"New Balance for {self.account_holder_name} is {self.balance}")

    
    






def main():
    # account = None
    accounts = {} # to hold multiple accounts

    while True:
        print("\n=========== BANK ACCOUNT ==============")
        print("1. Open Account")       
        print("2. Activate the account")       
        print("3. Deactivate the account")               
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Show Balance")
        print("7. Show Acount Info")
        print("8. List all Accounts")
        print("9. Show Statement")
        print("10. Apply Interest")
        print("11. Quit")
        print("=======================================")

        choice = input("Select an option: ")
        
        
        if choice == "1":
            account = BankAccount.open_account()
            accounts[account.account_number] = account

        elif choice == "2":
        
            account = find_account(accounts)
            if account: 
                account.activate_account()
        
        elif choice == "3":
           
            account = find_account(accounts)
            if account: 
                account.de_activate_account()
        
        elif choice == "4":
          
            account = find_account(accounts)
            if account: 
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
            
        elif choice == "5":
           
            account = find_account(accounts)
            if account: 
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)

        elif choice == "6":
           
            account = find_account(accounts)
            if account: 
                account.check_balance()

        elif choice == "7":
            
            account = find_account(accounts)
            if account: 
                account.account_info()
                
        elif choice == "8":
            list_allaccounts(accounts)

        elif choice == "9":
            account = find_account(accounts)
            if account: 
                account.show_statement()

        elif choice == "10":
            account = find_account(accounts)
            if account: 
                if isinstance(account,SavingsAccount):
                   account.add_interest()
                else:
                    print("Interest can only be added to a Savings Account.")
                
        elif choice == "11":
            print("\nThank you for using our bank.")
            break

        else:
            print("\nInvalid option. Please try again.")


main()

