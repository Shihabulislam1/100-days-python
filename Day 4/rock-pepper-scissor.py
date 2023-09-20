import random as rd

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

game_images = [rock, paper, scissors]

u=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if u>=3 or u<0:
  print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(game_images[u])

    c=rd.randint(0,2)
    print("Computer chose:")
    print(game_images[c])

    if u==c:
       print("It's a draw")
    elif u==0 and c==2:
       print("You win")
    elif u==2 and c==0:
         print("You lose")
    elif u>c:
            print("You win")
    elif c>u:
            print("You lose")
    