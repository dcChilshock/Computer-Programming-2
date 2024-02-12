from calcfunctions import *


def doSomething():
  print("Hello, world!")
def printnums():
  x = 0 
  while x < 10:
    print("x", x)
    x += 1
def main():  
  doSomething()
  printnums()
  a = add(1, 2)
  q, r = divmod2(5, 10)
  print(q, r)
  pass
if __name__ == "__main__":
  main()
