def add(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1*num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    if num2 == 0 :
        return "Errot: Cannot divide by zero"
    return num1/num2

# DRY Dont repeat yourself
while True:
    print("===============================")
    print("       Simple Calulator"        )
    print("===============================")
    print("         1. Add                ")
    print("         2. Subtract           ")
    print("         3. Multiply           ")
    print("         4. Divide             ")
    print("         0. Quit               ")
    print("===============================")

    choice = input("Choose an option 0 - 4 : ")

    if choice == "0":
        print("Claulator Closed.")
        print("Thankyou for using the world's best calculator")
        break
    
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        print("select correct option to continue from the menu")
        continue

    a = float(input("Enter the first Number: "))
    b = float(input("Enter the second Number: "))

    
    if choice == "1":
        print(f"Adding {a} and {b} = {add(a ,b)}");

    elif choice == "2":
        print(f"Subtracting {a} and {b} = {subtract(a ,b)}");

    elif choice == "3":
        print(f"Multiplying {a} and {b} = {multiply(a ,b)}");

    elif choice == "4":
        print(f"Dividing {a} and {b} = {round(divide(a ,b),2)}");

# Fix the divide problem
# Menu problem, present use with an option to continue (c) or quit (q) the calculator
# Convert the menu into a function of its own









