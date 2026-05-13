def add(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1*num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

# DRY Dont repeat yourself

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

elif choice == "1":
    a = float(input("Enter the first Number: "))
    b = float(input("Enter the second Number: "))
    print(f"Adding {a} and {b} = {add(a ,b)}");

elif choice == "2":
    a = float(input("Enter the first Number: "))
    b = float(input("Enter the second Number: "))
    print(f"Subtracting {a} and {b} = {subtract(a ,b)}");

elif choice == "3":
    a = float(input("Enter the first Number: "))
    b = float(input("Enter the second Number: "))
    print(f"Multiplying {a} and {b} = {multiply(a ,b)}");

elif choice == "4":
    a = float(input("Enter the first Number: "))
    b = float(input("Enter the second Number: "))
    print(f"Dividing {a} and {b} = {round(divide(a ,b),2)}");











