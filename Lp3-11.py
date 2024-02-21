class clLp311:
  def __init__(self, design, code, debug, test):
    self.design = design
    self.code = code
    self.debug = debug
    self.test = test
    self.total = 0
    self._percents = [0]*4 #same as [0,0,0,0]
  
  def __percent(self, number):
    return round((number/self.total) * 100, 2)
  def calc(self):
    self.total = self.design + self.code + self.debug + self.test
    self._percents[0] = self.__percent(self.design)
    self._percents[1] = self.__percent(self.code)
    self._percents[2] = self.__percent(self.debug)
    self._percents[3] = self.__percent(self.test)

  def display(self):
    print(f"Tasks\t\tTime")
    print(f"Designing\t\t{self._percents[0]}%")
    print(f"Coding\t\t{self._percents[1]}%")
    print(f"debugging\t\t{self._percents[2]}%")
    print(f"testing\t\t{self._percents[3]}%")
    print(f"total amount spent: ${self.total:.2f}")
def main():
  print("enter the amount of time spent on these tasks \n")
  design = float(input("Designing>"))
  code = float(input("Coding>"))
  debug = float(input("Debugging>"))
  test = float(input("Testing>"))
  print()

  total = clLp311(design, code, debug, test)
  total.calc()
  total.display()
  pass

if __name__ == "__main__":
  main()