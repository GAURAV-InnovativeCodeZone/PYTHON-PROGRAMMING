# Project : 01 => Head-Tail Game using random module 
# This game created by Gaurav Panwar

import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def main():
    print("\n --------Welcome to the Head-Tail Game!--------\n")
    print("\n                    Start Game\n")

    while True:
        user_choice = input("\nEnter your choice! (Heads/Tails): ")

        if user_choice not in ['Heads', 'Tails']:
            print("Invalid choice! Please enter 'Heads' or 'Tails' \n")
            continue;

        result = flip_coin()
        print(f"The coin landed on: {result} \n")

        if result == user_choice:
            print("Congratulations! You won the toss.")
        else:
            print("Oops! Better luck next time.")

        play_again = input("\n\nDo you want to play again? (Yes/No): ")

        
        if play_again != 'Yes':
            print("\n\n                   Finished Game\n\n")
            print("----------Thanks for playing! Goodbye!----------")
            break;
        else:
        	print("\nLet's play again --->")

if __name__ == "__main__":
    main()