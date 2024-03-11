#cl285b 
class Salesperson:
  def __calc(self):
    if self.code == 5 or self.code == 8:
      if self.sales <= 5000:
        self.comm = self.sales * 0.075 
      else:
        self.comm = 5000 * 0.075 + (self.sales-5000) * 0.085
  def __init__(self, id, code, sales):
    self.id = id
    self.code = code
    self.sales = sales
    self.comm = 0