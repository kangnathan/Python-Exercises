print("ROCK PAPER SCISSORS")
from random import randint
num = randint(1,3)

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

if num == 1:
    computer_move = "Rock"
elif num == 2:
    computer_move = "Paper"
elif num == 3:
    computer_move = "Scissors"

print("Select you move:")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")

player_move = input("Enter Your Move: ")

while player_move not in ["1", "2", "3"]:
    player_move = input("Enter Your Move: ")

if player_move == "1":
    x = "Rock"
if player_move == "2":
    x = "Paper"
if player_move == "3":
    x = "Scissors"

print("YOUR MOVE IS: ")
if player_move == "1":
    print(rock)
elif player_move == "2":
    print(paper)
elif player_move == "3":
    print(scissors)

print("COMPUTER MOVE IS: ")
if computer_move == "Rock":
    print(rock)
elif computer_move == "Paper":
    print(paper)
elif computer_move == "Scissors":
    print(scissors)

if player_move == "1" and computer_move == "Rock":
    print("YOU ARE TIED")
elif player_move == "2" and computer_move == "Paper":
    print("YOU ARE TIED")
elif player_move == "3" and computer_move == "Scissors":
    print("YOU ARE TIED")
elif player_move == "3" and computer_move == "Scissors":
    print("YOU WIN!!")
elif player_move == "2" and computer_move == "Paper":
    print("YOU WIN!!")
elif player_move == "3" and computer_move == "Paper":
    print("YOU WIN!!")
elif player_move == "2" and computer_move == "Rock":
    print("YOU WIN!!")
elif player_move == "1" and computer_move == "Scissors":
    print("YOU WIN!!")
else:
    print("YOU LOSE")





    

       