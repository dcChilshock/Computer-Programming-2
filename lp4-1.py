copies = int(input("enter number of copies: "))
price = 0.0
#if copies > 0 and copies <= 99:
#  price = 0.30
#and on and on
if 0 < copies <= 99: #nicer syntax
  price = 0.30
elif 99 < copies <= 499:
  price = 0.28
elif 499 < copies <= 749:
  price = 0.27
elif 749 < copies <= 1000:
  price = 0.26
elif copies > 1000:
  price = 0.25
else:
  print("The Number of Copies is invalid, either a decimal or negative number.")
print("Price per copy is: $ " + str(price))
cost = price * copies 
print("The total cost is: " + str(cost)) 