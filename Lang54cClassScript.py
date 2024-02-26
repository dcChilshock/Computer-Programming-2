class Prog54c:
  def __init__(self, pi, radius):
    self.pi = pi
    self.radius = radius
    self.end = 0

  def getarea(self):
    return pi * (radius ** 2)
    
  def getcircum(self):
    return 2 * pi * radius

  def calc(self):
    cir = getcircum(self)
    area  = getarea(self)

  def display(self):
    print("The outcomes are.")
    print("Radius: " + radius)
    print(f"Area: " + area)
    print(f"Circumfrence: " + cir)
    
    
  
def main():
  print("What is the radius of the circle?")
  radius = float(input("Radius? "))
  print()
  pi = 3.14159
  end = Prog54c(pi, radius)
  end.calc()
  end.display()
  pass

if __name__ == "__main__":
  main()