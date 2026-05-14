balance = 1000

def deposit(amount):
    global balance 
    balance += amount

    print(f"Deposited : {amount}")
    print(f"New Balance : {balance}")

def withdraw(amount):
    global balance 
    balance -= amount

    print(f"Withdrawn : {amount}")
    print(f"New Balance : {balance}")

def showbalance():
    print(f"Your Remaning Balance is : {balance}")
    

def main():
    while True:
        print("===========Bank Account==============")
        print("1. Dposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("4. Quit")
        print("=====================================")

        choice = input("Slect the option")

        if choice == "1":
            d = float(input("Enter the amount to be deposited: "))
            deposit(d)

        elif choice == "2":
            w = float(input("Enter the amount to be withdrawn: "))
            withdraw(w)

        elif choice == "3":
            showbalance()


        elif choice == "4":
            print("Thank you for using our bank")
            break
        else:
            print("Invalid option, Please try again.")


main()

# Can not deposit 0$
# Transaction Fee for withdrawal
# check withdrawal for negative balance
# Insufficient funds msg back to the user
# Print statement (later)



