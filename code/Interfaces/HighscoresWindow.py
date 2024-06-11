import tkinter as tk
import json
import os

def show_highscores(root):
   
    
   
     
    
    # Get the path to the parallel folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_folder_path = os.path.join(current_dir, '..', 'database')  # Adjust the folder name accordingly
    highscores_path = os.path.join(database_folder_path, 'highscores.json')
    
    
    
    def read_json_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    
    
    def transform_high_scores(data):
        high_scores = {"Classic": [], "Trivia": []}
        
        # Separate scores by game mode
        for entry in data:
            game_mode = entry["game_mode"]
            name = entry["name"]
            score = entry["score"]
            high_scores[game_mode].append({"name": name, "score": score})
            
            # Sort and format scores, keeping only top 5
        for mode in high_scores:
            sorted_scores = sorted(high_scores[mode], key=lambda x: x["score"], reverse=True)[:5]
            formatted_scores = [f"{i+1}. {entry['name']} - {entry['score']}" for i, entry in enumerate(sorted_scores)]
            high_scores[mode] = formatted_scores
    
        return high_scores
    



    # Create a new window for the high scores
    highscores_window = tk.Toplevel()
    highscores_window.title("High Scores")
    highscores_window.attributes("-fullscreen", True)  #full screen
    
    # # Hide the main menu window
    # main_menu_window.withdraw()

    print(read_json_file(highscores_path))  
    print()
    print(transform_high_scores(read_json_file(highscores_path)))
    high_scores_data = transform_high_scores(read_json_file(highscores_path))

   
    
    
    
    

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


    # Add a button to return to the main menu
    return_button = tk.Button(highscores_window, text="Main Menu", command=return_to_main_menu, width=20)
    return_button.pack(pady=10)

    # Ensure the main menu window reappears if the high scores window is closed
    def on_closing():

        highscores_window.destroy()

    highscores_window.protocol("WM_DELETE_WINDOW", on_closing)

if __name__ == "__main__":
    root = tk.Tk()
    show_highscores(root)
    root.mainloop()
