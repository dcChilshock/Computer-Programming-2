eggs = int(input("Enter number of eggs: "))
dozens = eggs // 12 
remainder = eggs % 12
price = 0


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
print("Number of eggs purchased: " + str(eggs))
costegg = price * dozens
priceR = (price / 12)
costR = priceR * remainder
totalcost = costegg + costR
print("The total cost of eggs purchased: " + str(totalcost))
