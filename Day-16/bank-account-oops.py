class BankAccount:
    def __init__  (self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount == 0:
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


account1 = BankAccount("Mike", 2000)
account2 = BankAccount("Paraj", 3000)

account1.check_balance()
account1.deposit(100)

account2.check_balance()
account2.deposit(300)
account2.withdraw(50)
account2.check_balance()






