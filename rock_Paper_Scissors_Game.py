#Rock, Paper, Scissors Game
import random


def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

user = get_user_choice()
computer = get_computer_choice()

if user == computer:
    print(f"Both chose {user}. It's a tie!")
elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
    print(f"You chose {user}. Computer chose {computer}. You win!")
else:
    print(f"You chose {user}. Computer chose {computer}. Computer wins!")