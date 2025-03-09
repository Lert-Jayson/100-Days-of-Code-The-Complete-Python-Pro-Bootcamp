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
---'    ____)____
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

rockpaperscissors = [rock, paper, scissors]

user_input = input("What do you choose ? Type 0 for rock, 1 for paper and 2 for scissors: \n")

if user_input.isdigit() and int(user_input) in [0, 1, 2]:
    user_ans = rockpaperscissors[int(user_input)]
    print("You choose: ", user_ans)
    
    computer_ans = rockpaperscissors[random.randint(0, 2)]
    print(f"Computer Choose: {computer_ans}")
    if user_ans == computer_ans:
        print("Its a Tie")
    elif (user_ans == rock and computer_ans == scissors) or \
        (user_ans == scissors and computer_ans == paper) or \
        (user_ans == paper and computer_ans == rock):
        print("You Win!")
    else: print("You Lose!")
    
else: print("Invalid input! Please enter only 0, 1, or 2.")