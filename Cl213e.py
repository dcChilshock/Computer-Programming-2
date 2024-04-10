class Cl213e:
  def __init__(self, age ):
    self.age = age
    self.TW = 0
    self.TF = 0
    self.FS = 0
    self.SE = 0
    self.E = 0
    self.Total = 0

  def calc(self):
    if self.age < 20:
      self.TW += 1
      self.Total += 1
    elif self.age >= 20 and self.age < 40:
      self.TF += 1
      self.Total += 1
    elif self.age >= 40 and self.age < 60:
      self.FS += 1
      self.Total += 1
    elif self.age >= 60 and self.age < 80:
      self.SE += 1
      self.Total += 1
    elif self.age > 80:
      self.E += 1
      self.Total += 1
    pass

  def __str__(self):
    return "Age: " + str(self.age) + " Distribution: "