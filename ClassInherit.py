class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sayHi(self):
    print("Hi")

class Cat(Animal):
  def __init__(self, name, age, sound, lives):
    super().__init__(name, age)
    self.sound = sound
    self.lives = lives

  def saySound(self):
    print(self.sound)

  def sayLives(self):
    print(self.lives)
#maybe add dog class with sound thing


cat = Cat("Billy", 5, "Meow", 7)
cat.sayHi()
cat.sayLives()
cat.saySound()

class Dog(Animal):
  def __init__(self, name, age, sound):
    super().__init__(name, age)
    self.sound = sound

  def saySound(self):
    print(self.sound)

dog = Dog("Sam", 7, "Bark")
dog.sayHi()
dog.saySound()