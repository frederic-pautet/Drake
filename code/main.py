import tkinter as tk

from Controllers import ClassicMenuController
from Controllers import TriviaMenuController
from Controllers import MultiplayerMenuController
from Controllers import HighscoresWindowController

def create_main_menu():
    
    def start_game(mode):
        print(f"Starting {mode} mode...")  # Placeholder for actual game logic
    
    def show_highscores():
        print("Showing highscores...")  # Placeholder for actual highscores display logic
    
    # Create the main window
    root = tk.Tk()
    root.title("Snake Game Menu")
    
    # Function to create buttons
    def create_button(text, command):
        button = tk.Button(root, text=text, command=lambda: command(root), width=20)
        button.pack(pady=5)
    
    # Buttons for different game modes
    create_button("Classic Mode", ClassicMenuController.main)
    create_button("Trivia Mode", TriviaMenuController.main)
    create_button("Multiplayer Mode", MultiplayerMenuController.main)
    
    # Button to view highscores
    create_button("Highscores", HighscoresWindowController.main)
    
    # Run the tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_main_menu()
