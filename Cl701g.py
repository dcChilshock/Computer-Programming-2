#Cl701g.py
class Person:
  def __init__(self, fn, ln):
    self._first = fn
    self._last = ln

  def getName(self):
    return self._first + " " + self._last

class Student:
  def __init__(fn, ln, gpa):
    super().__init__(fn, ln)
    self.gpa = gpa

class Teacher:
  def __init__(fn, ln, numstu):
    super().__init__(fn,ln)
    self.numstu = numstu 

class Admin: 
  def __init__(fn, ln, favword):
    super().__init__(fn,ln)
    self.favword = favword

