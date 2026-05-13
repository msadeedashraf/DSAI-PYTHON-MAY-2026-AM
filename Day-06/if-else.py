"""Locigal Operator"""

customer_name = input("Enter your name:")

credit_score = 680
monthly_income = 3500
existing_debt = 1000

has_guarantor = True
is_unemployed = False

# Loan Decision
if (
    (
        credit_score > 700 and
        monthly_income > 4000 and
        existing_debt < 2000
    )
    or has_guarantor
) and not is_unemployed:

    print(f"{customer_name} is APPROVED for the loan.")

else:
    print(f"{customer_name} is NOT approved.")

"""
credit_score = 720
monthly_income = 5000
existing_debt = 1500

has_guarantor = False
is_unemployed = False

# Loan Approval Logic
approved = (
    (
        credit_score > 700 and
        monthly_income > 4000 and
        existing_debt < 2000
    )
    or has_guarantor
) and not is_unemployed

# Result
print("Loan Approved:", approved)

"""


"""
score = 85
attendance = 80
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")
"""


"""
x = 11

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("10 or below.")
"""


"""
x = int(input("Enter the number of your choice: "))

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    elif ():
        print("but not above 20.")
    else:
        print("10 or below.")

"""


"""
x = int(input("Enter the number of your choice: "))

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("10 or below.")

"""
    
"""
temperature = 25
is_raining = True
is_weekend = False

if temperature > 20 and not is_raining or is_weekend:
    print("Great day for outdoor activities!")
else:
    print("Not a Great day for outdoor activities!")
"""

"""
age = 12
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
"""

"""
a = 200
b = 33
c = 100
if a > b or c > a:
    print("Both conditions are True")
else:
    print("At least one condition is False")
"""

"""
a = 200
b = 33
c = 100
if a > b and c > a:
    print("Both conditions are True")
else:
    print("At least one condition is False")
"""

"""
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
"""



"""
True and True = True
True and False = False
False and True = False
False and False = False

True OR True = True
True OR False = True
False OR True = True
False OR False = False

"""


"""
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")  
"""
