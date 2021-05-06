import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player >= 0 and player <= 2:
  print(images[player])

  print("Computer chose:")
  computer = random.randint(0, 2)
  print(images[computer])

  if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You win")
  elif (player == 2 and computer == 0) or (player == 0 and computer == 1) or (player == 1 and computer == 2):
    print("You lose")
  else:
    print("It's a draw")

else:
  print("Invalid selection")
