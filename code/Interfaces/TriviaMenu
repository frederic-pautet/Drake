import tkinter as tk
from tkinter import messagebox

import sys
import os
# import the parent directory in the path to return later to main menu
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)



def main(precedent_window):
    from main import create_main_menu

  
    precedent_window.withdraw()
    # Create a new window for Classic Mode settings
    trivia_window = tk.Toplevel()
    trivia_window.title("trivia Mode Settings")
    trivia_window.attributes("-fullscreen", True)  #full screen

    # Function to display the rules
    def show_rules():
        rules = ("Classic Mode Rules:\n"
                 "1. Use arrow keys to move the snake.\n"
                 "2. Eat the correct answe to grow longer and pass the question.\n"
                 "3. Avoid running into walls or the snake's own body.\n"
                 "4. The game ends if the snake collides with itself or the walls, or if you select the wrong answer.")
        messagebox.showinfo("Trivia Mode Rules", rules)

    # Label for speed setting
    tk.Label(trivia_window, text="Select Question difficulty:").pack(pady=5)

    # Questions setting options
    difficulty_var = tk.StringVar(value="Medium")
    difficulties = ["Easy", "Medium", "Hard"]
    for difficulty in difficulties:
        tk.Radiobutton(trivia_window, text=difficulty, variable=difficulty_var, value=difficulty).pack(anchor='w')

    # Button to show rules
    tk.Button(trivia_window, text="Show Rules", command=show_rules).pack(pady=5)




    # Button to return to main menu
    def return_to_main_menu():
        trivia_window.destroy()
        create_main_menu()


    # Function to start the game with selected speed
    def start_classic_game():
        selected_difficulty = difficulty_var.get()
        print(f"Starting Trivia Mode with {selected_difficulty} questions...")  # Placeholder for actual game start logic
        trivia_window.destroy()  # Close the settings window

    tk.Button(trivia_window, text="Main Menu", command=return_to_main_menu).pack(pady=10)
    
    # Start game button
    tk.Button(trivia_window, text="Start Game", command=start_classic_game).pack(pady=10)

   
