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
rps=[rock,paper,scissors]
user=int(input("rock:0 paper:1 scissor:2  "))
computer=random.randint(0,2)
print(f" user chose: \n{rps[user]}\n computer chose: \n{rps[computer]}\n")
if user==computer:
 print("It's a draw")
elif user==0:
    if computer==1:
        print("You lose")
    else:
        print("You win!")
elif user==1:
    if computer==0:
        print("You win!")
    else:
        print("You lose")
elif user==2:
    if computer==1:
        print("You win!")
    else:
        print("You lose")

