#Importing the random module to generate computer's random choice
import random

# Define ASCII art for Rock, Paper and Scissors
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

# Store ASCII art in a list so it can be accessed using index
game_images = [rock, paper, scissors]

# Game Introduction
print("Welcome to Rock, Paper, Scissors!")
print("Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

# Ask user for input and convert it to an integer
user_choice = int(input("What do you choose (0, 1 or 2)\n"))
print("\n")

# Check if user's input is valid
if 0 > user_choice or user_choice >= 3:
  print("You typed an invalid number. You lose!")
else:

  # Print user's choice
  print(f"You chose:")
  print(game_images[user_choice])

  # Generate computer's random choice (0, 1 or 2)
  computer_choice = random.randint(0, 2)

  # Print computer's choice
  print(f"\nComputer chose:")
  print(game_images[computer_choice])

  # Determine game result (win, lose, or draw)
  if user_choice == computer_choice:
    print("It's a draw!")
  elif user_choice == 0 and computer_choice == 2:
    print("\nYou win!, Rock beats Scissors!")
  elif user_choice == 2 and computer_choice == 1:
    print("\nYou win!, Scissors beats Paper!")
  elif user_choice == 1 and computer_choice == 0:
    print("\nYou win!, Paper beats Rock!")
  else:
    print("\nYou lose!")
