"""
I had an opportunity to attend the Microsoft AI and ML day, and one of 
the activities we did was to code the rock_paper_scissor game using 
copilot. 
"""

import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_comp_choice(user_history):
    if not user_history:
        return random.choice(["rock", "paper", "scissors"])
    most_common_user_choice = max(set(user_history), key=user_history.count)
    counter_choice = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }
    return counter_choice[most_common_user_choice]

def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "tie"
    elif (user_choice == "rock" and ai_choice == "scissors") or \
         (user_choice == "paper" and ai_choice == "rock") or \
         (user_choice == "scissors" and ai_choice == "paper"):
        return "user"
    else:
        return "comp"

def play_game():
    user_history = []
    scores = {"user": 0, "comp": 0, "ties": 0}

    while True:
        user_choice = get_user_choice()
        ai_choice = get_comp_choice(user_history)
        print(f"Computer chose: {ai_choice}")
        result = determine_winner(user_choice, ai_choice)
        
        if result == "user":
            print("You win this round!")
            scores["user"] += 1
        elif result == "comp":
            print("Computer wins this round!")
            scores["comp"] += 1
        else:
            print("It's a tie!")
            scores["ties"] += 1
        
        user_history.append(user_choice)

        print(f"Scores - You: {scores['user']}, Computer: {scores['comp']}, Ties: {scores['ties']}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
