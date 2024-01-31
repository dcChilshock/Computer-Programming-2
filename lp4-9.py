import random

rnd = random.randint(1,20)
guess = int(input("Enter your guess 1-20, player: "))
if rnd == guess:
  print("You won, the secret number was: " + str(rnd) + " and your guess was: " + str(guess))