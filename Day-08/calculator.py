def add(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1*num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

a = float(input("Enter the first Number: "))
b = float(input("Enter the second Number: "))

print(f"Adding {a} and {b} = {add(a ,b)}");
print(f"Subtracting {a} and {b} = {subtract(a ,b)}");
print(f"Multiplying {a} and {b} = {multiply(a ,b)}");
print(f"Dividing {a} and {b} = {round(divide(a ,b),2)}");


