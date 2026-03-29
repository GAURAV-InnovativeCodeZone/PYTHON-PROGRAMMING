"""
=========================== ✪ ROCK-PAPER-SCISSORS GAME using PYTHON ✪ ============================
"""
import random
import time
import os                                  # For clearing the terminal screen
from colorama import Fore, Style, init     # Initialize colorama for colored text

# Initialize colorama for colored text
init(autoreset=True)

# Game art with consistent title case display
ART = {
    'rock': f"""
    {Style.BRIGHT + Fore.RED}_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    'paper': f"""
    {Style.BRIGHT + Fore.BLUE}_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    'scissors': f"""
    {Style.BRIGHT + Fore.GREEN}_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the game header."""
    clear_screen()
    print(f"{Fore.YELLOW}===================================")
    print(f"{Style.BRIGHT + Fore.CYAN}    ✪ ROCK - PAPER - SCISSORS ✪")
    print(f"{Fore.YELLOW}==================================={Style.RESET_ALL}\n")

def get_user_choice():
    """Get and validate user input, accepting any case but standardizing to lowercase."""
    valid_choices = ['rock', 'paper', 'scissors', 'exit', 'quit']
    while True:
        print(f"{Fore.MAGENTA}Choices: {Fore.WHITE}Rock, Paper, Scissors")
        print(f"{Fore.MAGENTA}Type: {Fore.WHITE}exit/quit to end game")
        user_input = input(f"{Fore.CYAN}Enter your choice: ").strip()
        user_choice = user_input.lower()  # Convert to lowercase for comparison
        
        if user_choice in valid_choices:
            return user_choice, user_input  # Return both lowercase and original input
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.\n")

def get_computer_choice():
    """Generate computer's choice with a delay for suspense."""
    print(f"\n{Fore.YELLOW}Computer is choosing...")
    time.sleep(1.5)
    return random.choice(['rock', 'paper', 'scissors'])

def display_choices(user_choice, user_input, computer_choice):
    """Display both choices with ASCII art in title case."""
    # Display user's choice in title case (but preserve original formatting)
    print(f"\n{Fore.MAGENTA}You chose {user_choice.title()}:{ART.get(user_choice, '')}")
    print(f"{Fore.MAGENTA}Computer chose {computer_choice.title()}:{ART.get(computer_choice, '')}")

def determine_winner(user, computer):
    """Determine the game winner."""
    if user == computer:
        return "tie"
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    return "user" if winning_combinations[user] == computer else "computer"

def play():
    """Main game loop."""
    user_wins = 0
    computer_wins = 0
    ties = 0
    
    while True:
        print_header()
        print(f"{Fore.CYAN}Score: You {user_wins} | Computer {computer_wins} | Ties {ties}\n")
        
        user_choice, original_input = get_user_choice()  # Get both versions
        
        if user_choice in ['exit', 'quit']:
            print_header()
            print(f"{Fore.CYAN}Final Score:")
            print(f"{Fore.GREEN}Your wins: {user_wins}")
            print(f"{Fore.RED}Computer wins: {computer_wins}")
            print(f"{Fore.YELLOW}Ties: {ties}")
            print(f"\n{Fore.MAGENTA}Thanks for playing! Goodbye!")
            break
        
        computer_choice = get_computer_choice()
        print_header()
        display_choices(user_choice, original_input, computer_choice)
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print(f"{Fore.YELLOW}\nIt's a tie!")
            ties += 1
        elif winner == "user":
            print(f"{Fore.GREEN}\nYou win! {user_choice.title()} beats {computer_choice.title()}!")
            user_wins += 1
        else:
            print(f"{Fore.RED}\nComputer wins! {computer_choice.title()} beats {user_choice.title()}!")
            computer_wins += 1
        
        time.sleep(1.1)
        input(f"\n{Fore.WHITE}Press Enter to continue...")

if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Game interrupted. Goodbye!")
        


"===================ALTERNATIVE CODE===================\n"

# import random

# # Define valid choices in all three allowed formats
# valid_choices = {
#     "rock": "Rock",
#     "ROCK": "Rock",
#     "Rock": "Rock",
#     "paper": "Paper",
#     "PAPER": "Paper",
#     "Paper": "Paper",
#     "scissor": "Scissor",
#     "SCISSOR": "Scissor",
#     "Scissor": "Scissor",
# }

# print("Welcome to Rock-Paper-Scissors! Type 'exit' to quit at any time.")

# while True:
#     user_input = input("\nEnter your choice (Rock/Paper/Scissor): ").strip()
    
#     if user_input.lower() == 'exit':
#         print("Exiting the game...")
#         break
        
#     # Check if input matches one of the allowed formats
#     if user_input not in valid_choices:
#         print("Invalid Choice! Please enter Rock, Paper, or Scissor in the correct case (rock, ROCK, or Rock).")
#         continue
        
#     # Get standardized choice (e.g., "Rock") from the dictionary
#     user_choice = valid_choices[user_input]
#     comp_choice = random.choice(["Rock", "Paper", "Scissor"])
    
#     print(f"Your choice: {user_choice}, Computer's choice: {comp_choice}")
    
#     if user_choice == comp_choice:
#         print("Both chose the same: It's a tie!")
#     elif user_choice == "Rock":
#         if comp_choice == "Paper":
#             print("Paper covers Rock. Computer wins!")
#         else:
#             print("Rock breaks Scissors. You win!")
#     elif user_choice == "Paper":
#         if comp_choice == "Scissor":
#             print("Scissors cut Paper. Computer wins!")
#         else:
#             print("Paper covers Rock. You win!")
#     elif user_choice == "Scissor":
#         if comp_choice == "Rock":
#             print("Rock breaks Scissors. Computer wins!")
#         else:
#             print("Scissors cut Paper. You win!")