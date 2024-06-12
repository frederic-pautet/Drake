import json
#import pygame
from tkinter import *
from random import randint, shuffle

import os


def start_trivia_snake_game():
    # Initialiser Pygame pour les sons
    #pygame.init()
    #correct_sound = pygame.mixer.Sound('correct.mp3')
    #wrong_sound = pygame.mixer.Sound('wrong.mp3')

    # Get the path to the parallel folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_folder_path = os.path.join(current_dir, '..', 'database')  # Adjust the folder name accordingly
    questions_path = os.path.join(database_folder_path, 'questions.json')
    highscores_path = os.path.join(database_folder_path, 'highscores.json')

    
            
            
    def process_name(name, game_mode, score, filename=highscores_path):
        print("writing database")
        data = read_database(filename)
        new_record = {
            "name": name,
            "game_mode": game_mode,
            "score": score
            }
        data.append(new_record)
        write_database(data, filename)
        
    def write_database(data, filename=highscores_path):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            
    def read_database(filename=highscores_path):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    

    def charger_questions():
        with open(questions_path, 'r', encoding='utf-8') as file:
            return json.load(file)
            

    # Créer une fenêtre grâce à la fonction Tk()
    fenetre = Tk()
    fenetre.title('Drake The Snake - Trivia Mode')

    # Récupérer les dimensions de l'écran
    hauteur = fenetre.winfo_screenheight()
    largeur = fenetre.winfo_screenwidth()

    H = str(int(hauteur / 1.1))
    L = str(int(largeur / 2))
    fenetre.geometry(L + "x" + H + "+0+0")

    # Dimensions du plateau de jeu
    LargeurPlateau = largeur / 2
    HauteurPlateau = hauteur / 1.2

    # Créer un Canvas pour le plateau de jeu
    Plateau = Canvas(fenetre, width=LargeurPlateau, height=HauteurPlateau, bg="green")
    Plateau.pack(side="bottom")

    # Créer un Canvas pour le score
    Barre = Text(fenetre, width=int(largeur / 2), height=int(HauteurPlateau / 10), bg="light blue")
    Barre.pack(side="top")
    Barre.insert(END, "score: 0\n")

    # Nombre de cases du plateau
    NombreDeCases = 75
    LargeurCase = (LargeurPlateau / NombreDeCases)
    HauteurCase = (HauteurPlateau / NombreDeCases)

    questions = charger_questions()
    shuffle(questions)
    index_question = 0
    new_index = 0

    def remplir_case(x, y):
        OrigineCaseX1 = x * LargeurCase
        OrigineCaseY1 = y * HauteurCase
        OrigineCaseX2 = OrigineCaseX1 + LargeurCase
        OrigineCaseY2 = OrigineCaseY1 + HauteurCase
        Plateau.create_rectangle(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="black")

    def case_aleatoire():
        AleatoireX = randint(0, NombreDeCases - 1)
        AleatoireY = randint(0, NombreDeCases - 1)
        return (AleatoireX, AleatoireY)

    def dessine_serpent(snake):
        for case in snake:
            x, y = case
            remplir_case(x, y)

    def etre_dans_snake(case):
        return 1 if case in SNAKE else 0

    def left_key(event):
        global MOUVEMENT
        if MOUVEMENT != (1, 0):  # Empêcher de revenir en arrière
            MOUVEMENT = (-1, 0)

    def right_key(event):
        global MOUVEMENT
        if MOUVEMENT != (-1, 0):  # Empêcher de revenir en arrière
            MOUVEMENT = (1, 0)

    def up_key(event):
        global MOUVEMENT
        if MOUVEMENT != (0, 1):  # Empêcher de revenir en arrière
            MOUVEMENT = (0, -1)

    def down_key(event):
        global MOUVEMENT
        if MOUVEMENT != (0, -1):  # Empêcher de revenir en arrière
            MOUVEMENT = (0, 1)

    fenetre.bind("<Left>", left_key)
    fenetre.bind("<Right>", right_key)
    fenetre.bind("<Up>", up_key)
    fenetre.bind("<Down>", down_key)

    def serpent_mort(NouvelleTete):
        global PERDU
        NouvelleTeteX, NouvelleTeteY = NouvelleTete
        if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= NombreDeCases or NouvelleTeteY >= NombreDeCases:
            PERDU = 1

    def mise_a_jour_score():
        global SCORE
        SCORE += 1
        Barre.delete(0.0, 3.0)
        Barre.insert(END, "score: " + str(SCORE) + "\n")

    def mise_a_jour_snake():
        global SNAKE, SCORE
        (AncienneTeteX, AncienneTeteY) = SNAKE[0]
        MouvementX, MouvementY = MOUVEMENT
        NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)
        serpent_mort(NouvelleTete)
        if not PERDU:
            SNAKE.insert(0, NouvelleTete)
            if SCORE > len(SNAKE) - 1:  # Augmenter le serpent d'un segment pour chaque point gagné
                pass
            else:
                SNAKE.pop()
                
    def reinitialiser_jeu():
        global SNAKE, MOUVEMENT, SCORE, PERDU, questions, index_question, question_affichee
        SNAKE = [case_aleatoire()]
        MOUVEMENT = (0, 0)
        SCORE = 0
        PERDU = False
        questions = charger_questions()  # Recharger et mélanger les questions
        shuffle(questions)
        index_question = 0
        question_affichee = False

    def afficher_question(index_question):
        question = questions[index_question]
        options = question["options"]
        Plateau.create_text(LargeurPlateau / 2, HauteurPlateau / 2 - 20, text=question["question"], fill="white")
        positions = [(3, 3), (3, NombreDeCases - 6), (NombreDeCases - 6, 3), (NombreDeCases - 6, NombreDeCases - 6)]
        for i, option in enumerate(options):
            x, y = positions[i]
            Plateau.create_text(x * LargeurCase, y * HauteurCase, text=option, fill="white", anchor="nw")

    def verifier_reponse(index_question, PERDU=False):
        print(f"index_question: {index_question}")
        global new_index
        
        if index_question != 0:
            index_question = new_index
        print(f"index_question2: {index_question}")
    
        question = questions[index_question]
        reponses = {"A": (3, 3), "B": (3, NombreDeCases - 6), "C": (NombreDeCases - 6, 3), "D": (NombreDeCases - 6, NombreDeCases - 6)}
        reponse_choisie = None
        for rep, pos in reponses.items():
            print(rep, pos)
            if SNAKE[0] == pos:
                reponse_choisie = str(rep)
                print(reponse_choisie)
                
                if reponse_choisie == question["answer"]:
                    # correct_sound.play()
                    index_question += 1
                    mise_a_jour_score()
                    mise_a_jour_snake()
                    question_affichee = False
                    if index_question >= len(questions):
                        afficher_felicitations()
                        index_question = 0  # Recommence les questions si toutes sont répondues
                    
                    return index_question
                else:
                    return -1  # Wrong answer
            
        return index_question  # If no matching position found

    def afficher_felicitations():
        Plateau.create_text(LargeurPlateau / 2, HauteurPlateau / 2, text="Félicitations ! Vous avez répondu à toutes les questions !", fill="yellow", font=("Helvetica", 24))
    
    def tache():
        global index_question, new_index, PERDU
        if not PERDU:
            fenetre.update()
            fenetre.update_idletasks()
            mise_a_jour_snake()
            
            new_index = verifier_reponse(index_question)
            index_question = new_index
            
            print(f"new_index: {new_index}")
            
            Plateau.delete("all")
            dessine_serpent(SNAKE)
            afficher_question(index_question)
            
            if new_index == -1:
                PERDU = True
    
            fenetre.after(100, tache)
    
        elif PERDU:
            Barre.delete(0.0, 3.0)
            Barre.insert(END, "Perdu avec un score de " + str(SCORE))
            
            fenetre_perdu = Toplevel(fenetre)
            fenetre_perdu.title("Partie Perdue")
            fenetre_perdu.attributes("-fullscreen", True)  # full screen
            fenetre_perdu.geometry("300x200")
    
            Label(fenetre_perdu, text=f"Score: {SCORE} Entrez votre nom pour enregistrer votre score", font=("Helvetica", 16, "bold")).pack(pady=10)
    
            name_entry = Entry(fenetre_perdu)
            name_entry.pack(pady=10)

            
            
            def submit_name() :
                print("submitting_name")
                name = name_entry.get()
                print("submitting_name2")
                if not name:
                    process_name("unknown", "Trivia", SCORE) #default name
                    return
                else: 
                    process_name(name, "Trivia", SCORE)
            
            
            submit_button = Button(fenetre_perdu, text="Submit", command=submit_name, bg="lightgreen")
            submit_button.pack(pady=10)


            Button(fenetre_perdu, text="Rejouer", bg="lightgreen", command=lambda: [fenetre_perdu.destroy(), reinitialiser_jeu()]).pack(pady=10)
            Button(fenetre_perdu, text="Back to the menu", command=back_to_menu).pack(pady=10)
            
            
    def back_to_menu():
        #pygame.quit()
       import sys
       parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
       sys.path.append(parent_dir)
       
       fenetre.destroy()
       
       print("importing main")
       import run
       run.create_main_menu() 

               
            
            

    reinitialiser_jeu()  # Assurez-vous de réinitialiser le jeu avant de commencer

    fenetre.after(0, tache)
    fenetre.mainloop()

# If you want to run the game directly from this script
if __name__ == "__main__":
    start_trivia_snake_game()
