#Cl213f.py

class Cl213f:
  def __init__(self, kwh):
    self.kwh = kwh
    self.cost = 0.0
    self.rcost = 0.0

  def calc(self):
    if self.kwh < 2000:
      self.cost += self.kwh * 0.07
      self.rcost = round(self.cost,3)
    elif self.kwh > 2000 and self.kwh < 8001:
      self.cost += (2000 * 0.07)
      self.kwh -= 2000
      self.cost += (self.kwh * 0.05)
      self.rcost = round(self.cost,3)
    elif self.kwh > 8000 and self.kwh < 10000:
      self.cost += (2000 * 0.07)
      self.kwh -= 2000
      self.cost += (6000 * 0.05)
      self.kwh -= 6000
      self.cost += (self.kwh * 0.04)
    elif self.kwh > 10000:
      self.cost += (2000 * 0.07)
      self.kwh -= 2000
      self.cost += (6000 * 0.05)
      self.kwh -= 6000
      self.cost += (self.kwh * 0.04)
      self.rcost = round(self.cost,3)
      
        
      
    pass
  
  def __str__(self):
    return f"The cost of {self.kwh} is " + str(self.rcost)
    
    