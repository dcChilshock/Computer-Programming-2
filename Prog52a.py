#lang 52 a - area and perimeter of a rectangular object
length = int(input("enter length: "))
width = int(input("enter width: "))
area = length * width
perimeter = (length * 2) + (width * 2)

print("Area =", area)#one way for doing 
print("Perimeter =" + str(perimeter)) #another way 3 
#run with "python FILENAME.py" in the shell