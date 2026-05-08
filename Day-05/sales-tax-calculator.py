product_name = input("Enter product name : ")
price = float(input("Enter the product price : "))

tax_rate = 0.15
tax_amount = price * tax_rate
final_price = price + tax_amount

print("================================")
print("Receipt")
print("================================")
print("Product:", product_name)
print("Original Price: $", price)
print("Tax: $", tax_amount)
print("Final Price: $", final_price)