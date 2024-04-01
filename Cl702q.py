#Cl702q.py
class Vehicles:
  def __init__(self, name, tire):
    self.name = name
    self.tire = tire


class Car:
  def __init__(self, name, tire, money):
    super().__init__(name, tire)
    self.money = money
  
class Truck:
  def __init__(self, name, tire, miles):
    super().__init__(name, tire)
    self.miles = miles
    self.value = 50000
    
     

class Bus:
  def __init__(self, name, tire, city):
    super().__init__(name, tire)
    self.city = city

