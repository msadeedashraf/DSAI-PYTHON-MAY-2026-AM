balance = 1000
transactions =  []
from datetime import datetime



def deposit(amount):
    global balance 
    balance += amount
    current_time = datetime.now()

    transaction = [
        current_time.strftime('%Y-%m-%d'), # date
        current_time.strftime('%I:%M:%S'), # time
        "Deposit",
        amount, # money in 
        0, # money out
        balance
        ]

    transactions.append(transaction)


    print(f"Deposited : {amount}")
    print(f"New Balance : {balance}")

def withdraw(amount):
    global balance 
    balance -= amount
    
    current_time = datetime.now()   
    
    transaction = [
        current_time.strftime('%Y-%m-%d'), # date
        current_time.strftime('%I:%M:%S'), # time
        "Withdrawal",
        0, # money in 
        amount, # money out
        balance
        ]

    transactions.append(transaction)

    print(f"Withdrawn : {amount}")
    print(f"New Balance : {balance}")

def showstatement():
    if (transactions) == 0: 
        print("No transaction to display.")
        return

    print("\n==============================================================")
    print("                    SADEED NATIONAL BANK")
    print("==============================================================")

    print(
        f"{'Date':<12}"
        f"{'Time':<12}"
        f"{'Description':<15}"
        f"{'Money In':>12}"
        f"{'Money Out':>12}"
        f"{'Balance':>12}"
    )

    print("-" * 75)

    # LOOP THROUGH LIST
    for i in transactions:

        print(
            f"{i[0]:<12}"
            f"{i[1]:<12}"
            f"{i[2]:<15}"
            f"${i[3]:>11.2f}"
            f"${i[4]:>11.2f}"
            f"${i[5]:>11.2f}"
        )

    print("-" * 75)
    print(f"{'Closing Balance':>63}: ${balance:.2f}")
    print(f"Your Remaning Balance is : {balance}")
    

def main():
    while True:
        print("===========Bank Account==============")
        print("1. Dposit")
        print("2. Withdraw")
        print("3. Show Statement")
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
            showstatement()


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



