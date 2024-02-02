num1 = int(input("Input bigger number 1: "))
num2 = int(input("Input smaller number 2: "))
while num2 > 0:
  temp = num1 % num2 
  num1 = num2
  num2 = temp
print("The greatest common factor is: " + str(num1))