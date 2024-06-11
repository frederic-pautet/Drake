import tkinter as tk
from tkinter import messagebox
import sys
import json


from Interfaces import ClassicMenu
from Interfaces import TriviaMenu
from Interfaces import MultiplayerMenu
from Interfaces import HighscoresWindow



def create_main_menu():
    
    def start_game(mode):
        print(f"Starting {mode} mode...")  # Placeholder for actual game logic
    
    def show_highscores():
        print("Showing highscores...")  # Placeholder for actual highscores display logic
    
    # Create the main window
    root = tk.Tk()
    root.title("Snake Game Menu")
    root.attributes("-fullscreen", True)  #full screen
    

    # Function to create buttons
    def create_button(text, command, color):
        button = tk.Button(root, text=text, command=lambda: command(root), width=20, bg=color)
        button.pack(pady=5)

    tk.Label(root, text="Drake The Snake Game:", font=("Arial", 24)).pack(pady=5)
    # Buttons for different game modes
    create_button("Classic Mode", ClassicMenu.main, "lightblue")
    create_button("Trivia Mode", TriviaMenu.main, "lightblue")
    create_button("Multiplayer Mode", MultiplayerMenu.main, "lightblue")
    
    # Button to view highscoresd
    create_button("Highscores", HighscoresWindow.show_highscores, "lightyellow")
    
    # Button to view main rules
    create_button("Show rules", show_rules, "white")
    
    #Button to leave the game
    create_button("Leave Game", leave_game, "lightgreen")
    

    
    # Run the tkinter event loop
    root.mainloop()

def show_rules(root):
    with open('database/rules.json','r',encoding='utf_8') as f :
        rules = json.load(f)
        messagebox.showinfo("Rules", rules["main"])

def leave_game(root): #to close the program
    root.destroy()
    sys.exit()


if __name__ == "__main__":
    create_main_menu()
