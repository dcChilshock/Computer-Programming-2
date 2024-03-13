#Cl213f.py

class Cl213f:
  def __init__(self, kwh):
    self.kwh = kwh
    self.cost = 0.0

  def calc(self):
    if kwh < 2000:
     cost += kwh * 0.07
    elif kwh > 2000 and kwh < 8001:
      cost += (2000 * 0.07)
      kwh -= 2000
      cost += (kwh * 0.05)
    elif kwh > 10000:
      cost += (2000 * 0.07)
      kwh -= 2000
      cost += (6000 * 0.05)
      kwh -= 6000
      cost += (kwh * 0.04)
        
      
    pass
  
  def __str__(self):
    return f"The cost of {self.kwh} is"
    
    