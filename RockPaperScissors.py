import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Define choices and outcomes
choices = ["rock", "paper", "scissors"]
outcome_matrix = {
    ("rock", "scissors"): "win",
    ("scissors", "paper"): "win",
    ("paper", "rock"): "win",
    ("scissors", "rock"): "lose",
    ("paper", "scissors"): "lose",
    ("rock", "paper"): "lose"
}

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    return outcome_matrix.get((player_choice, computer_choice), "lose")

def play(player_choice):
    global player_score, computer_score, round_number
    
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1
    
    result_text = f"Round {round_number}\n\nYou chose {player_choice}, computer chose {computer_choice}.\n"
    if result == "win":
        result_text += "You win this round!"
    elif result == "lose":
        result_text += "You lose this round!"
    else:
        result_text += "This round is a draw!"
    
    result_text += f"\n\nCurrent Score -> You: {player_score}, Computer: {computer_score}"
    
    result_label.config(text=result_text)
    round_number += 1

def exit_game():
    messagebox.showinfo("Final Score", f"Final Score -> You: {player_score}, Computer: {computer_score}")
    root.destroy()

# Initialize scores and round number
player_score = 0
computer_score = 0
round_number = 1

# Set up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.config(bg="#cce7ff")

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

# Create and place widgets
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 20, "bold"), bg="#cce7ff")
title_label.pack(pady=20)

instructions_label = tk.Label(root, text="Choose your move:", font=("Helvetica", 14), bg="#cce7ff")
instructions_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#cce7ff")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play("rock"), bd=0)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play("paper"), bd=0)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play("scissors"), bd=0)
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#cce7ff")
result_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=exit_game, font=("Helvetica", 12), bg="#ff6666", fg="white", bd=0, padx=20, pady=10)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
