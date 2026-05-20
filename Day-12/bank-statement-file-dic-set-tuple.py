balance = 1000
transactions =  []
overdraft = 150
from datetime import datetime

FILE_NAME = 'bank_statement.txt'

print(datetime.now())





def deposit(amount):
    global balance 
    if amount == 0:
        print("Deposit amount can not be equal to zero")
        return


    balance += amount

    # TUPLE
    # Tuple are fixed/unchangeable
    timestamp = (

        datetime.now().strftime('%Y-%m-%d'),
        datetime.now().strftime('%I:%M:%S')

    )

    # Dictionary 
    transaction = {
        "type": "Deposit",
        "money_in": amount,
        "money_out": 0,
        "date" :  timestamp[0],
        "time" : timestamp[1],
        "balance" : balance
    }

    transactions.append(transaction)


    print(f"Deposited : {amount}")
    print(f"New Balance : {balance}")

def withdraw(amount):
    global balance 
    
    if amount > balance + overdraft:
        print("Insufficient funds")
        return
    
    fee = 2
    amount += fee 


    balance -= amount


     # TUPLE
    # Tuple are fixed/unchangeable
    timestamp = (

        datetime.now().strftime('%Y-%m-%d'),
        datetime.now().strftime('%I:%M:%S')

    )

    # current_time = datetime.now()

    # Dictionary 
    transaction = {
        "type": "Deposit",
        "money_in": 0,
        "money_out": amount,
        "date" :  timestamp[0],
        "time" : timestamp[1],
        "balance" : balance
    }

    
    transactions.append(transaction)

    print(f"Withdrawn : {amount-fee}")
    print(f"New Balance : {balance}")


def create_statement():
    if (transactions) == 0: 
        print("No transaction to display.")
        return

    file_path = f"D:\\CBC\\DSAI-Jan-2026-AM\\05-Python\\DSAI-PYTHON-MAY-2026-AM\\Day-11\\statements\\{FILE_NAME}"

    # print(file_path)

    with open(file_path, "w") as file:

            file.write("============================================================\n")
            file.write("                    SADEED NATIONAL BANK\n")
            file.write("============================================================\n")
            file.write("Account Holder : Student Demo Account\n")
            file.write("Account Number : **** **** **** 1234\n")
            file.write(f"Statement Date : {datetime.now()}\n")
            file.write("Currency       : CAD\n")
            file.write("============================================================\n\n")

            file.write(
                f"{'Date':<12}"
                f"{'Time':<12}"
                f"{'Description':<15}"
                f"{'Money In':>12}"
                f"{'Money Out':>12}"
                f"{'Balance':>12}\n"
            )

            file.write("-" * 75 + "\n")

            for transaction in transactions:

                file.write(
                    f"{transaction["date"]:<12}"
                    f"{transaction["time"]:<12}"
                    f"{transaction["type"]:<15}"
                    f"${transaction["money_in"]:>11.2f}"
                    f"${transaction["money_out"]:>11.2f}"
                    f"${transaction["balance"]:>11.2f}\n"
                )

            file.write("-" * 75 + "\n")
            file.write(f"{'Closing Balance':>63}: ${balance:.2f}\n")
            file.write("============================================================\n")

            print("\nStatement created successfully.")
            print(f"Saved At: {file_path}")



def read_statment():
    
    try:
        with open(FILE_NAME, 'r') as file:
            print("\n")
            print(file.read())
    except FileNotFoundError:
        print("\n Statement file not found.")


    


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
    for transaction in transactions:

        print(
            f"{transaction["date"]:<12}"
            f"{transaction["time"]:<12}"
            f"{transaction["type"]:<15}"
            f"${transaction["money_in"]:>11.2f}"
            f"${transaction["money_out"]:>11.2f}"
            f"${transaction["balance"]:>11.2f}\n"
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
        print("5. Read Statement")
        print("6. Create Statement")
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

        elif choice == "5":
            read_statment()

        elif choice == "6":
            create_statement()

            

        elif choice == "4":
            print("Thank you for using our bank")
            break
        else:
            print("Invalid option, Please try again.")


main()

# Implemented 
# Can not deposit 0$
# Transaction Fee for withdrawal
# check withdrawal for negative balance (apply overdraft as well)
# Insufficient funds msg back to the user



