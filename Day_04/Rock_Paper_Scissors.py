import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")


# -------------------------

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

game_choice = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_choice_pic = game_choice[user_choice]
print(user_choice_pic)

print("Computer Chose:")
computer_choice_number = random.randint(0,2)
computer_choice = game_choice[computer_choice_number]
print(computer_choice)

if user_choice == computer_choice_number:
    print("Your Match Draw")
elif user_choice == 0 and computer_choice_number == 1 or user_choice == 1 and computer_choice_number == 2 or user_choice == 2 and computer_choice_number == 0:
    print("You Lose")
elif user_choice == 0 and computer_choice_number == 2 or user_choice == 1 and computer_choice_number == 0 or user_choice == 2 and computer_choice_number == 1:
    print("You Win")


