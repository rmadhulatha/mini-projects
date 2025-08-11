scissors = '''
    __________
___,    ______)___
            ______)
        __________)
        (_____)
----.___(___)
'''

rock = '''
    _________
____,   _____)
        (____)
        (_____)
        (_____)
----,___(____)
'''

paper = '''
    __________
___,    ______)____
           ________)
           ________)
           _______)
----.___________)
'''
import random
user_choice = input("What do you choose?")
print("You'r choice:", user_choice)
if user_choice == "rock":
    print(rock)
elif user_choice == "paper":
    print(paper)
elif user_choice == "scissors":
    print(scissors)

computer_choice = random.randint(0,2)
print(f"Computer chose:{computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_choice == "rock" and computer_choice == 2:
    print("You win!")
elif user_choice == "paper" and computer_choice == 0:
    print("You win!")
elif user_choice == "scissors" and computer_choice == 1:
    print("You win!")
elif user_choice == "rock" and computer_choice == 1:
    print("You lose!")
elif user_choice == "paper" and computer_choice == 2:
    print("You lose!")
elif user_choice == "scissors" and computer_choice == 0:
    print("You lose!")
elif user_choice == "rock" and computer_choice == 0:
    print("It's a tie!")
elif user_choice == "paper" and computer_choice == 1:
    print("It's a tie!")
elif user_choice == "scissors" and computer_choice == 2:
    print("It's a tie!")
    