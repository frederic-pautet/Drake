from tkinter import *
from random import randint
import os
import json

def main(speed):
    # Créer une fenêtre grâce à la fonction Tk()
    fenetre = Tk()
    fenetre.title('Drake The Snake')
    fenetre.attributes("-fullscreen", True)  # full screen

    # Récupérer les dimensions de l'écran
    hauteur = fenetre.winfo_screenheight()
    largeur = fenetre.winfo_screenwidth()

    # Convertir les données de la hauteur (H) et de la largeur (L) en int, puis en string, et modifie les dimensions voulues
    H = str(int(hauteur / 1.1))
    L = str(int(largeur / 2))
    fenetre.geometry(L + "x" + H + "+0+0")

    # Définir les dimensions du plateau de jeu
    LargeurPlateau = largeur / 2
    HauteurPlateau = hauteur / 1.2

    # Créer un Canvas pour le plateau de jeu
    Plateau = Canvas(fenetre, width=LargeurPlateau, height=HauteurPlateau, bg="green")
    Plateau.pack(side="bottom")

    # Créer un Canvas pour le score
    Barre = Text(fenetre, width=int(largeur / 2), height=int(HauteurPlateau / 10), bg="light blue", font=("Helvetica", 16, "bold"))
    Barre.pack(side="top")
    Barre.tag_configure("center", justify='center')
    Barre.insert("1.0", "score: 0\n", "center")

    # Définir le nombre de cases du plateau
    NombreDeCases = 75
    LargeurCase = (LargeurPlateau / NombreDeCases)
    HauteurCase = (HauteurPlateau / NombreDeCases)
    
    # Get the path to the parallel folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_folder_path = os.path.join(current_dir, '..', 'database')  # Adjust the folder name accordingly
    highscores_path = os.path.join(database_folder_path, 'highscores.json')

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

    def fruit_aleatoire():
        FruitAleatoire = case_aleatoire()
        while etre_dans_snake(FruitAleatoire):
            FruitAleatoire = case_aleatoire()
        return FruitAleatoire

    def dessine_fruit():
        global FRUIT
        x, y = FRUIT
        OrigineCaseX1 = x * LargeurCase
        OrigineCaseY1 = y * HauteurCase
        OrigineCaseX2 = OrigineCaseX1 + LargeurCase
        OrigineCaseY2 = OrigineCaseY1 + HauteurCase
        Plateau.create_oval(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="red")

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

        # si le serpent se mange lui-même (sauf au démarrage, c'est-à-dire: sauf quand MOUVEMENT vaut (0, 0))
        # OU si on sort du canvas
        if (etre_dans_snake(NouvelleTete) and MOUVEMENT != (0, 0)) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= NombreDeCases or NouvelleTeteY >= NombreDeCases:
            # alors, on a perdu
            PERDU = 1

    def mise_a_jour_score():
        global SCORE
        SCORE += 1
        Barre.delete("1.0", "end")
        Barre.insert("1.0", "score: " + str(SCORE) + "\n", "center")

    def mise_a_jour_snake():
        global SNAKE, FRUIT
        (AncienneTeteX, AncienneTeteY) = SNAKE[0]
        MouvementX, MouvementY = MOUVEMENT
        NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)
        serpent_mort(NouvelleTete)
        SNAKE.insert(0, NouvelleTete)
        if NouvelleTete == FRUIT:
            #eat_sound.play()  # Jouer le son quand le serpent mange un fruit
            FRUIT = fruit_aleatoire()
            mise_a_jour_score()
        else:
            SNAKE.pop()

    def reinitialiser_jeu():
        global SNAKE, FRUIT, MOUVEMENT, SCORE, PERDU, GAME_OVER_SHOWN
        SNAKE = [case_aleatoire()]
        FRUIT = fruit_aleatoire()
        MOUVEMENT = (0, 0)
        SCORE = 0
        PERDU = 0
        GAME_OVER_SHOWN = False

    def afficher_fenetre_perdu():
        global GAME_OVER_SHOWN
        if GAME_OVER_SHOWN:
            return
        GAME_OVER_SHOWN = True

        def submit_name(local_score):
            name = name_entry.get()
            if not name:
                process_name("unknown", "Classic", local_score)  # default name
            else:
                process_name(name, "Classic", local_score)

        def process_name(name, game_mode, score, filename=highscores_path):
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

        fenetre_perdu = Toplevel(fenetre)
        fenetre_perdu.title("Partie Perdue")
        fenetre_perdu.attributes("-fullscreen", True)  # full screen
        fenetre_perdu.geometry("300x200")
        local_score = SCORE
        Label(fenetre_perdu, text=f"Score: {SCORE} Entrez votre nom pour enregistrer votre score", font=("Helvetica", 16, "bold")).pack(pady=10)

        name_entry = Entry(fenetre_perdu)
        name_entry.pack(pady=10)

        submit_button = Button(fenetre_perdu, text="Submit", command=lambda: submit_name(local_score), bg="lightyellow")
        submit_button.pack(pady=10)

        Button(fenetre_perdu, text="Play again", bg="lightgreen", command=lambda: [reinitialiser_jeu()]).pack(pady=10)
        Button(fenetre_perdu, text="Back to the menu", command=lambda: [back_to_menu()]).pack(pady=10)

    def tache():
        fenetre.update()
        fenetre.update_idletasks()
        mise_a_jour_snake()
        Plateau.delete("all")
        dessine_fruit()
        dessine_serpent(SNAKE)
        if PERDU:
            afficher_fenetre_perdu()
        else:
            fenetre.after(interval, tache)

    def back_to_menu():
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(parent_dir)
        fenetre.destroy()
        print("importing main")
        import run
        run.create_main_menu()

    # Speed intervals mapping
    speed_intervals = {
        'Slow': 200,
        'Medium': 100,
        'Fast': 50
    }

    interval = speed_intervals.get(speed, 100)  # Default to medium if speed is not recognized

    global SNAKE, FRUIT, MOUVEMENT, SCORE, PERDU, GAME_OVER_SHOWN
    SNAKE = [case_aleatoire()]
    FRUIT = fruit_aleatoire()
    MOUVEMENT = (0, 0)
    SCORE = 0
    PERDU = 0
    GAME_OVER_SHOWN = False

    fenetre.after(0, tache)
    fenetre.mainloop()

if __name__ == "__main__":
    main('Medium')  # medium by default
