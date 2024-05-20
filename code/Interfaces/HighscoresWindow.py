# Controllers/highscorescontroller.py
import tkinter as tk

def main(main_menu_window):
    # Hide the main menu window
    main_menu_window.withdraw()

    # Create a new window for the high scores
    highscores_window = tk.Toplevel()
    highscores_window.title("High Scores")
    highscores_window.attributes("-fullscreen", True)  #full screen

    # # Function to transform the databses into a highscore list (to be done yet)
    # def highscores() :
    #   return dictionnary

    # high_scores_data = highscores
  
    # High scores data example (to be removed later)
    high_scores_data = {
        "Classic": [
            "1. Timothé - 986",
            "2. maxime 35 - 456",
            "3. progamer07 - 455",
            "4. Constance - 400",
            "5. Victoire67 - 23"
        ],
        "Trivia": [
            "1. Cadence126 - 2013",
            "2. BigG89 - 1001",
            "3. DA - 967",
            "4. solange - 500",
            "5. prog - 2"
        ]
    }

    # Title for the high scores window
    title_label = tk.Label(highscores_window, text="High Scores", font=("Arial", 24))
    title_label.pack(pady=10)

    # Label to show which mode is currently shown
    current_mode_label = tk.Label(highscores_window, text="Classic Mode High Scores", font=("Arial", 16))
    current_mode_label.pack(pady=5)

    
    # Frame to contain the high scores
    scores_frame = tk.Frame(highscores_window)
    scores_frame.pack(pady=10)

    # Function to update the displayed high scores
    def display_high_scores(category):

        # Update the current mode label
        current_mode_label.config(text=f"{category} Mode High Scores")

      
        # Clear existing widgets in the frame
        for widget in scores_frame.winfo_children():
            widget.destroy()


        # Display the high scores for the selected category
        for score in high_scores_data[category]:
            label = tk.Label(scores_frame, text=score, padx=10, pady=5)
            label.pack()

    # Initial display of Classic mode high scores
    display_high_scores("Classic")

    # Buttons to switch between different high score categories
    def create_button(text, command):
        button = tk.Button(highscores_window, text=text, command=command, width=20)
        button.pack(pady=5)

    create_button("Classic Mode", lambda: display_high_scores("Classic"))
    create_button("Trivia Mode", lambda: display_high_scores("Trivia"))

    # Function to return to the main menu
    def return_to_main_menu():
        highscores_window.destroy()
        main_menu_window.deiconify()

    # Add a button to return to the main menu
    return_button = tk.Button(highscores_window, text="Main Menu", command=return_to_main_menu, width=20)
    return_button.pack(pady=10)

    # Ensure the main menu window reappears if the high scores window is closed
    def on_closing():
        main_menu_window.deiconify()
        highscores_window.destroy()

    highscores_window.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()
