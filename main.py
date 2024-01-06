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

User_hand = int(input("What do you chose ? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

game_images = [rock, paper, scissors]
if User_hand >= 3 or User_hand <= -1:
    print("Invalid choice you lose : (")
else:
    print(game_images[User_hand])

    Computer_hand = random.randint(0, 2)
    print("Computer chose")
    print(game_images[Computer_hand])
    if User_hand == Computer_hand:
        print("Draw")
    elif User_hand == 0 and Computer_hand == 2:
        print("You win :) ")
    elif User_hand == 2 and Computer_hand == 0:
        print("You lose :( ")
    elif User_hand < Computer_hand:
        print("You lose :( ")
    elif User_hand > Computer_hand:
        print("You win :) ")

