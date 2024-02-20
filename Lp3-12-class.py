class ClLP312:
  def __init__(self, food, clothing, entertainment, rent):
    self.food = food
    self.clothing = clothing 
    self.entertainment = entertainment
    self.rent = rent 
    self._budget = 0
    self._percents = [0]*4 #same as [0,0,0,0]

  def __percent(self, number):
    return round((number/self._budget) * 100, 2)

  def calculate(self):
    self._budget = self.food + self.clothing + self.entertainment + self.rent
    self._percents[0] = self.__percent(self.food)
    self._percents[1] = self.__percent(self.clothing)
    self._percents[2] = self.__percent(self.entertainment)
    self._percents[3] = self.__percent(self.rent)

  def display(self):#or display
    print("Category\t\tBudget")
    print(f"food\t\t\t{self._percents[0]}%")
    print(f"clothing\t\t{self._percents[1]}%")
    print(f"Entertainment\t{self._percents[2]}%")
    print(f"Rent\t\t\t{self._percents[3]}%")
    print(f"total amount spent: ${self._budget:.2f}")
  
      

def main():
  print("enter Amount spent last month on the following items: \n")
  food = float(input("food: $"))
  clothing = float(input("clothing: $"))
  entertainment = float(input("entertainment: $"))
  rent = float(input("rent: $"))
  print()
#make a new clLp32 object pass in the numbers to the constructor 

  budget = ClLP312(food, clothing, entertainment, rent)
  budget.calculate()
  budget.display()
  
  
  pass

if __name__ == "__main__":
  main()
