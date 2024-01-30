eggs = int(input("Enter number of eggs: "))
dozens = eggs // 12 
remainder = eggs % 12
price = 0
priceR = price * (price / 12)

if 0 < dozens < 4:
  price = 0.50
elif 4 <= dozens < 6:
  price = 0.45
elif 6 <= dozens < 11:
  price = 0.40
elif dozens >= 12:
  price = 0.35
else:
  print("number of eggs is invalid:")

costegg = price * dozens
costR = priceR * remainder
totalcost = costegg + costR
print("Number of eggs purchased: " + str(eggs))
print("The total cost of eggs purchased: " + str(totalcost))
  