students = ["Mark", "Paraj", "Abbay", "Zeemas", "Patricio", "Amro"]
# for i in students:
#     print(i)

for i in range(len(students)):
    print(students[i])

list1 = ["orange", "yellow", "red"]    
list2 = ["orange",  "red", "yellow"]    

print(list1==list2)

students.sort()

for i in range(len(students)):
    print(students[i])

students.reverse()

for i in range(len(students)):
    print(students[i])

students.append("Franke")
students.sort()

for i in range(len(students)):
    print(students[i])



transaction = "21132|mark|2000|sadeed|6471213213"
items = transaction.split('|')
for i in items:
    print(i)




"""
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
"""
# Can not deposit 0$
# Transaction Fee for withdrawal
# check withdrawal for negative balance
# Insufficient funds msg back to the user
# Print statement (later)



