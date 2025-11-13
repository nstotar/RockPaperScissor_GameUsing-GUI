import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors - Best of Three")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 3

        # Labels
        self.title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Player: {self.player_score} | Computer: {self.computer_score}", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Buttons
        self.rock_button = tk.Button(root, text="Rock", width=10, command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", width=10, command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Game", width=10, command=self.reset_game)
        self.reset_button.pack(pady=10)

    def play(self, player_choice):
        if self.rounds_played >= self.max_rounds:
            return

        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.get_result(player_choice, computer_choice)
        self.result_label.config(text=f"Player: {player_choice} | Computer: {computer_choice}\n{result}")

        if "win" in result:
            self.player_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")
        self.rounds_played += 1

        if self.rounds_played == self.max_rounds:
            self.end_game()

    def get_result(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            return "You win!"
        else:
            return "You lose!"

    def end_game(self):
        if self.player_score > self.computer_score:
            winner = "Player"
        elif self.computer_score > self.player_score:
            winner = "Computer"
        else:
            winner = "It's a tie!"

        messagebox.showinfo("Game Over", f"Game Over!\nWinner: {winner}")
        self.reset_game()

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
