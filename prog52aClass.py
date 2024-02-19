class Shape:
  #constructor; sets up class data 
  def __init__(self, length, width): #every class func starts with self then what ever comes after 
    self.length = length #these are stored in a way its easy to change them
    self.width = width 
    #extra variables need to be set up right here:
    self._area = 0 
    self._perim = 0 
    #means private variable cant really change it if your a user
    #also should only be called in the class
    # self._ = cannot be changed outside of the class
    # self. = can be chagned outside of the class
    # self.__ = cannot be changed
  #mutator/ setter : modifies class data
  def calculate(self):
    self._area = self.length * self.width 
    self._perim = 2 * self.length + 2 * self.width

  def setLength(self, length): #redudant
    self.length = length

  # accessors / getter : returns class data
  def getArea(self):
    return self._area
    
  def getPerimeter(self):
    return self._perim

def main():
  len = int(input("Enter Length: "))
  wid = int(input("Enter the Width: "))
  #make a new 'shape' object
  shape = Shape(len,wid) #when call shape constructor
  #potentiallt shape.setLength(5) changes length varaible
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perim:", shape.getPerimeter())
  pass

if __name__ == "__main__":
  main()
