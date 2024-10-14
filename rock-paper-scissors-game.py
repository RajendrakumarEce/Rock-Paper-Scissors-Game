import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.master.configure(bg='#F0F0F0')  # Light gray background

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.master, text="Rock Paper Scissors", font=("Helvetica", 16, "bold"), bg='#F0F0F0', fg='#333333')
        title_label.pack(pady=10)

        # Score
        self.score_label = tk.Label(self.master, text="Score - You: 0, Computer: 0", font=("Helvetica", 12), bg='#F0F0F0', fg='#333333')
        self.score_label.pack()

        # Buttons
        button_frame = tk.Frame(self.master, bg='#F0F0F0')
        button_frame.pack(pady=20)

        choices = ["Rock", "Paper", "Scissors"]
        button_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # Red, Teal, Light Blue
        for choice, color in zip(choices, button_colors):
            button = tk.Button(button_frame, text=choice, width=10, command=lambda c=choice: self.play(c),
                               bg=color, fg='white', activebackground='#333333', activeforeground='white')
            button.pack(side=tk.LEFT, padx=5)

        # Result
        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12), bg='#F0F0F0', fg='#333333', wraplength=350)
        self.result_label.pack(pady=10)

        # Play Again
        self.play_again_button = tk.Button(self.master, text="Play Again", command=self.reset_game,
                                           bg='#FFA500', fg='white', activebackground='#FF8C00', activeforeground='white')
        self.play_again_button.pack()
        self.play_again_button.pack_forget()  # Hide initially

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.update_score(result)
        self.display_result(user_choice, computer_choice, result)

        self.play_again_button.pack()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "user"
        else:
            return "computer"

    def update_score(self, result):
        if result == "user":
            self.user_score += 1
        elif result == "computer":
            self.computer_score += 1
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def display_result(self, user_choice, computer_choice, result):
        result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n"
        if result == "tie":
            result_text += "It's a tie!"
            color = '#FFA500'  # Orange for tie
        elif result == "user":
            result_text += "You win!"
            color = '#4CAF50'  # Green for win
        else:
            result_text += "Computer wins!"
            color = '#F44336'  # Red for loss
        self.result_label.config(text=result_text, fg=color)

    def reset_game(self):
        self.result_label.config(text="", fg='#333333')
        self.play_again_button.pack_forget()

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()