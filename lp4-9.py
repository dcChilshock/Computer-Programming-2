import random

rnd = random.randint(1,20)
guess = int(input("Enter your guess 1-20, player: "))
print("Computers Number: " + str(rnd))
print("Players Number: " + str(guess)) 
if rnd == guess:
  print("You won")
else:
  print("Better luck next time loser.")
  