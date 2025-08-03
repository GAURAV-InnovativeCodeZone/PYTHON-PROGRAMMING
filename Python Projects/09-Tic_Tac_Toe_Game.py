"""
=========================== ✪ TIC-TAC-TOE GAME using PYTHON ✪ ============================
"""

import random
import os
import time  # Added for delay
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'  # Human is always X
        self.game_active = False
        self.winner = None
        self.vs_computer = None
        self.colors = {
            'X': Fore.BLUE,
            'O': Fore.RED,
            'title': Fore.MAGENTA + Style.BRIGHT,
            'border': Fore.YELLOW,
            'win': Fore.GREEN + Style.BRIGHT,
            'lose': Fore.RED + Style.BRIGHT,
            'draw': Fore.CYAN,
            'button': Fore.WHITE + Back.BLUE,
            'active_button': Fore.BLACK + Back.WHITE,
            'instructions': Fore.LIGHTYELLOW_EX
        }
    
    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.colors['title'] + "\n  TIC TAC TOE\n")
        print(self.colors['border'] + "╔═══╦═══╦═══╗")
        for i in range(3):
            print(self.colors['border'] + "║", end=" ")
            for j in range(3):
                pos = i * 3 + j
                if self.board[pos] == 'X':
                    print(self.colors['X'] + self.board[pos], end=" ")
                elif self.board[pos] == 'O':
                    print(self.colors['O'] + self.board[pos], end=" ")
                else:
                    print(pos + 1, end=" ")
                print(self.colors['border'] + "║", end=" ")
            print()
            if i < 2:
                print(self.colors['border'] + "╠═══╬═══╬═══╣")
        print(self.colors['border'] + "╚═══╩═══╩═══╝")
    
    def print_mode_selection(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.colors['title'] + "\n  TIC TAC TOE\n")
        print(self.colors['instructions'] + "Select game mode:\n")
        
        # Button for Player vs Player
        button_text = "1. Player vs Player"
        if self.vs_computer == False:
            print(self.colors['active_button'] + f"  {button_text}  ", end=" ")
        else:
            print(self.colors['button'] + f"  {button_text}  ", end=" ")
        
        # Button for Player vs Computer
        button_text = "2. Player vs Computer"
        if self.vs_computer == True:
            print(self.colors['active_button'] + f"  {button_text}  ")
        else:
            print(self.colors['button'] + f"  {button_text}  ")
        
        print("\n" + self.colors['instructions'] + "Use 1 or 2 to select, then press Enter")
    
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                self.game_active = False
            elif ' ' not in self.board:
                self.game_active = False
            else:
                self.switch_player()
            return True
        return False
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        return False
    
    def computer_move(self):
        # Add thinking delay
        time.sleep(1)  # Computer "thinks" for 1 second
        
        # Simple AI - first checks for winning move, then blocks player, then random
        # Check for winning move
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                if self.check_winner():
                    return
                self.board[i] = ' '
        
        # Block player's winning move
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                if self.check_winner():
                    self.board[i] = 'O'
                    return
                self.board[i] = ' '
        
        # Try to take center
        if self.board[4] == ' ':
            self.board[4] = 'O'
            return
        
        # Try to take corners
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for corner in corners:
            if self.board[corner] == ' ':
                self.board[corner] = 'O'
                return
        
        # Take any available position
        available_positions = [i for i, spot in enumerate(self.board) if spot == ' ']
        if available_positions:
            position = random.choice(available_positions)
            self.board[position] = 'O'
    
    def print_result(self):
        self.print_board()
        if self.winner:
            if self.vs_computer:
                if self.winner == 'X':
                    print(self.colors['win'] + "\nCongratulations! You win! 🎉")
                else:
                    print(self.colors['lose'] + "\nComputer wins! Better luck next time! 💻")
            else:
                print(self.colors['win'] + f"\nPlayer {self.winner} wins! 🎉")
        else:
            print(self.colors['draw'] + "\nIt's a draw! 🤝")

def main():
    while True:
        game = TicTacToe()
        
        # Game mode selection
        while game.vs_computer is None:
            game.print_mode_selection()
            mode = input("\n> ")
            if mode == '1':
                game.vs_computer = False
                game.game_active = True
            elif mode == '2':
                game.vs_computer = True
                game.game_active = True
            else:
                print(Fore.RED + "Invalid choice! Please select 1 or 2")
        
        game.print_board()
        
        while game.game_active:
            if game.current_player == 'X' or not game.vs_computer:
                try:
                    position = int(input(f"\nPlayer {game.current_player}'s turn (1-9): ")) - 1
                    if 0 <= position <= 8:
                        if not game.make_move(position):
                            print(Fore.RED + "Position already taken! Try again.")
                            continue
                    else:
                        print(Fore.RED + "Invalid position! Choose between 1-9.")
                        continue
                except ValueError:
                    print(Fore.RED + "Please enter a valid number!")
                    continue
            else:
                print("\nComputer is thinking...", end="", flush=True)
                game.computer_move()
                if game.check_winner():  # Check if computer's move caused a win
                    game.winner = 'O'    # Computer is always O
                    game.game_active = False
                elif ' ' not in game.board:
                    game.game_active = False
                else:
                    game.switch_player()
            
            game.print_board()
        
        game.print_result()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print(Fore.MAGENTA + "\nGame Over!")
            print(Fore.MAGENTA + "\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
