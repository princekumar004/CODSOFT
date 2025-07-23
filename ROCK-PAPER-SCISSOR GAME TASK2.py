import random

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

print("Welcome to Rock, Paper, Scissors!")
user_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"\n--- Round {round_number} ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print(f"Score: You {user_score} | Computer {computer_score}")

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again not in ['yes', 'y']:
        print("\nFinal Score:")
        print(f"You: {user_score}\nComputer: {computer_score}")
        print("Thank you for playing!")
        break
    round_number += 1
