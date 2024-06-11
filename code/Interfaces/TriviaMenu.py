import tkinter as tk
from tkinter import messagebox



import sys
import os
# import the parent directory in the path to return later to main menu
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)



def main(precedent_window):
    precedent_window.withdraw()
    # Create a new window for Classic Mode settings
    classic_window = tk.Toplevel()
    classic_window.title("Classic Mode Settings")
    classic_window.attributes("-fullscreen", True)  #full screen

    # Function to display the rules
    def show_rules():
        rules = ("Trivia Mode Rules:\n"
                 "1. Use arrow keys to move the snake.\n"
                 "2. Eat the right answeer to grow longer.\n"
                 "3. Avoid running into walls or the snake's own body.\n"
                 "4. The game ends if the snake collides with itself or the walls.")
        messagebox.showinfo("Trivia Mode Rules", rules)

   
    # Label for menu title
    tk.Label(classic_window, text="Trivia Game", font=("Arial", 24)).pack(pady=5)
   
    # Button to show rules
    tk.Button(classic_window, text="Show Rules", command=show_rules).pack(pady=5)




    # Button to return to main menu
    def return_to_main_menu():
        from run import create_main_menu
        classic_window.destroy()
        create_main_menu()

    tk.Button(classic_window, text="Main Menu", command=return_to_main_menu).pack(pady=10)








    # Function to start the game with selected speed
    def start_classic_game():
        from Interfaces import TriviaMode
        
        print("Starting Trivia Mode.")  # Placeholder for actual game start logic
        classic_window.destroy()  # Close the settings window
        TriviaMode.start_trivia_snake_game()
        
        

    # Start game button
    tk.Button(classic_window, text="Start Game", command=start_classic_game).pack(pady=10)

if __name__ == "__main__":
  main()
