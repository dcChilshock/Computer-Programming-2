class Prog54c:
  def __init__(self, pi, radius):
    self.pi = pi
    self.radius = radius
    self.area = 0
    self.cir = 0
    self.end = 0

  def getarea(self):
    return self.pi * (self.radius ** 2)
    
  def getcircum(self):
    return 2 * self.pi * self.radius

  def calc(self):
    self.cir = self.getcircum()
    self.area  = self.getarea()

  def display(self):
    print("The outcomes are.")
    print(f"Radius:{self.radius}")
    print(f"Area: {self.area:.2f}")
    print(f"Circumfrence: {self.cir:.2f}")
    
    
  
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