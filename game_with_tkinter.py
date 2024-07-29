import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")
        self.h = 0
        self.b = 0
        self.round = 1

        # Label for the title
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Label for displaying scores
        self.score_label = tk.Label(root, text="You: 0 - Bot: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        # Buttons for choices
        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Arial", 14), command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Arial", 14), command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Arial", 14), command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Label for displaying round result
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Button to reset the game
        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def bot_choice(self):
        options = ['rock', 'paper', 'scissors']
        return random.choice(options)

    def play_round(self, human_choice):
        bot_choix = self.bot_choice()

        # Determine the result
        if human_choice == bot_choix:
            result = f"It's a tie! Both chose {human_choice}."
        elif (human_choice == "rock" and bot_choix == "scissors") or \
             (human_choice == "paper" and bot_choix == "rock") or \
             (human_choice == "scissors" and bot_choix == "paper"):
            self.h += 1
            result = f"You won! You chose {human_choice} and the bot chose {bot_choix}."
        else:
            self.b += 1
            result = f"You lost! You chose {human_choice} and the bot chose {bot_choix}."

        # Update the labels and scores
        self.score_label.config(text=f"You: {self.h} - Bot: {self.b}")
        self.result_label.config(text=result)
        self.round += 1

        # Check if someone won
        if self.h == 3:
            messagebox.showinfo("Game Over", "Congratulations! You won the game!")
            self.reset_game()
        elif self.b == 3:
            messagebox.showinfo("Game Over", "Sorry! The bot won the game.")
            self.reset_game()

    def reset_game(self):
        self.h = 0
        self.b = 0
        self.round = 1
        self.score_label.config(text="You: 0 - Bot: 0")
        self.result_label.config(text="")
        
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
