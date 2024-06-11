from tkinter import *
from random import randint

import os

def start_multiplayer_snake_game(speed, control_scheme='WASD'):
    fenetre = Tk()
    game = MultiplayerSnakeGame(fenetre, speed, control_scheme)

class MultiplayerSnakeGame:
    def __init__(self, fenetre, speed, control_scheme='WASD'):
        self.fenetre = fenetre
        self.speed = speed
        self.control_scheme = control_scheme
        self.paused = False

        if speed == 'Slow':
            self.delay = 200  # Slow
        elif speed == 'Medium':
            self.delay = 100  # Medium
        elif speed == 'Fast':
            self.delay = 50  # Fast

        self.fenetre.title('Multiplayer Snake Game')
        self.fenetre.attributes("-fullscreen", True)

        self.hauteur = fenetre.winfo_screenheight()
        self.largeur = fenetre.winfo_screenwidth()

        self.LargeurPlateau = self.largeur / 2
        self.HauteurPlateau = self.hauteur / 1.2

        self.Plateau = Canvas(fenetre, width=self.LargeurPlateau, height=self.HauteurPlateau, bg="green")
        self.Plateau.pack(side="bottom")

        self.top_frame = Frame(fenetre, bg="light blue")
        self.top_frame.pack(side="top", fill="x")

        self.Barre = Text(self.top_frame, width=int(self.largeur / 2), height=2, bg="light blue")
        self.Barre.pack(side="top")
        self.Barre.insert(END, "Snake 1: 0 | Snake 2: 0\n")

        self.pause_button = Button(self.top_frame, text="Pause", command=self.change_pause)
        self.pause_button.pack(side="right", padx=10, pady=10)

        self.NombreDeCases = 75
        self.LargeurCase = (self.LargeurPlateau / self.NombreDeCases)
        self.HauteurCase = (self.HauteurPlateau / self.NombreDeCases)

        self.setup_controls()

        self.reinitialiser_jeu()
        self.fenetre.after(0, self.tache)
        self.fenetre.mainloop()

    def setup_controls(self):
        # Player 1 controls
        self.fenetre.bind("<Left>", self.left_key)
        self.fenetre.bind("<Right>", self.right_key)
        self.fenetre.bind("<Up>", self.up_key)
        self.fenetre.bind("<Down>", self.down_key)
        
        # Player 2 controls based on control scheme
        if self.control_scheme == 'WASD':
            self.fenetre.bind("w", self.w_key)
            self.fenetre.bind("a", self.a_key)
            self.fenetre.bind("s", self.s_key)
            self.fenetre.bind("d", self.d_key)
        elif self.control_scheme == 'ZQSD':
            self.fenetre.bind("z", self.w_key)
            self.fenetre.bind("q", self.a_key)
            self.fenetre.bind("s", self.s_key)
            self.fenetre.bind("d", self.d_key)

    def change_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.tache()

    def remplir_case(self, x, y, color):
        OrigineCaseX1 = x * self.LargeurCase
        OrigineCaseY1 = y * self.HauteurCase
        OrigineCaseX2 = OrigineCaseX1 + self.LargeurCase
        OrigineCaseY2 = OrigineCaseY1 + self.HauteurCase
        self.Plateau.create_rectangle(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill=color)

    def case_aleatoire(self):
        AleatoireX = randint(0, self.NombreDeCases - 1)
        AleatoireY = randint(0, self.NombreDeCases - 1)
        return (AleatoireX, AleatoireY)

    def dessine_serpent(self, snake, color):
        for case in snake:
            x, y = case
            self.remplir_case(x, y, color)

    def etre_dans_snake(self, snake, case):
        return case in snake

    def fruit_aleatoire(self):
        FruitAleatoire = self.case_aleatoire()
        while self.etre_dans_snake(self.snake1, FruitAleatoire) or self.etre_dans_snake(self.snake2, FruitAleatoire):
            FruitAleatoire = self.case_aleatoire()
        return FruitAleatoire

    def dessine_fruit(self):
        x, y = self.FRUIT
        OrigineCaseX1 = x * self.LargeurCase
        OrigineCaseY1 = y * self.HauteurCase
        OrigineCaseX2 = OrigineCaseX1 + self.LargeurCase
        OrigineCaseY2 = OrigineCaseY1 + self.HauteurCase
        self.Plateau.create_oval(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="red")

    def left_key(self, event):
        if self.MOUVEMENT1 != (1, 0):
            self.MOUVEMENT1 = (-1, 0)

    def right_key(self, event):
        if self.MOUVEMENT1 != (-1, 0):
            self.MOUVEMENT1 = (1, 0)

    def up_key(self, event):
        if self.MOUVEMENT1 != (0, 1):
            self.MOUVEMENT1 = (0, -1)

    def down_key(self, event):
        if self.MOUVEMENT1 != (0, -1):
            self.MOUVEMENT1 = (0, 1)

    def w_key(self, event):
        if self.MOUVEMENT2 != (0, 1):
            self.MOUVEMENT2 = (0, -1)

    def a_key(self, event):
        if self.MOUVEMENT2 != (1, 0):
            self.MOUVEMENT2 = (-1, 0)

    def s_key(self, event):
        if self.MOUVEMENT2 != (0, -1):
            self.MOUVEMENT2 = (0, 1)

    def d_key(self, event):
        if self.MOUVEMENT2 != (-1, 0):
            self.MOUVEMENT2 = (1, 0)

    def serpent_mort(self, NouvelleTete, snake):
        NouvelleTeteX, NouvelleTeteY = NouvelleTete
        if (self.etre_dans_snake(snake, NouvelleTete) and (NouvelleTete != snake[0])) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= self.NombreDeCases or NouvelleTeteY >= self.NombreDeCases:
            return True
        return False

    def mise_a_jour_score(self):
        self.Barre.delete(0.0, 3.0)
        self.Barre.insert(END, f"Snake 1: {self.SCORE1} | Snake 2: {self.SCORE2}\n")

    def mise_a_jour_snake(self):
        AncienneTeteX1, AncienneTeteY1 = self.snake1[0]
        MouvementX1, MouvementY1 = self.MOUVEMENT1
        NouvelleTete1 = (AncienneTeteX1 + MouvementX1, AncienneTeteY1 + MouvementY1)

        AncienneTeteX2, AncienneTeteY2 = self.snake2[0]
        MouvementX2, MouvementY2 = self.MOUVEMENT2
        NouvelleTete2 = (AncienneTeteX2 + MouvementX2, AncienneTeteY2 + MouvementY2)

        if self.serpent_mort(NouvelleTete1, self.snake1) or self.etre_dans_snake(self.snake2, NouvelleTete1):
            self.PERDU = True
            self.winner = 'Snake 2'
        elif self.serpent_mort(NouvelleTete2, self.snake2) or self.etre_dans_snake(self.snake1, NouvelleTete2):
            self.PERDU = True
            self.winner = 'Snake 1'
        else:
            self.snake1.insert(0, NouvelleTete1)
            self.snake2.insert(0, NouvelleTete2)

            if NouvelleTete1 == self.FRUIT:
                self.FRUIT = self.fruit_aleatoire()
                self.SCORE1 += 1
                self.mise_a_jour_score()
            else:
                self.snake1.pop()

            if NouvelleTete2 == self.FRUIT:
                self.FRUIT = self.fruit_aleatoire()
                self.SCORE2 += 1
                self.mise_a_jour_score()
            else:
                self.snake2.pop()

    def reinitialiser_jeu(self):
        self.snake1 = [self.case_aleatoire()]
        self.snake2 = [self.case_aleatoire()]
        self.FRUIT = self.fruit_aleatoire()
        self.MOUVEMENT1 = (0, 0)
        self.MOUVEMENT2 = (0, 0)
        self.SCORE1 = 0
        self.SCORE2 = 0
        self.PERDU = False

    def tache(self):
        if not self.paused:
            self.mise_a_jour_snake()
            self.Plateau.delete("all")
            self.dessine_fruit()
            self.dessine_serpent(self.snake1, 'blue')
            self.dessine_serpent(self.snake2, 'yellow')
            if self.PERDU:
                
                self.show_result()
                
                # self.Barre.delete(0.0, 3.0)
                # self.Barre.insert(END, f"{self.winner} wins with a score of Snake 1: {len(self.snake1)}, Snake 2: {len(self.snake2)}")
                self.reinitialiser_jeu()
                self.fenetre.after(2000, self.tache)
            else:
                self.fenetre.after(self.delay, self.tache)

    def show_result(self):
        result_window = Toplevel(self.fenetre)
        result_window.title("Game Over")
        result_window.geometry("300x200")
        result_message = f"{self.winner} wins with a score of Snake 1: {len(self.snake1)}, Snake 2: {len(self.snake2)}"
        Label(result_window, text=result_message, font=("Helvetica", 12)).pack(pady=20)
        
        def back_to_menu():
            #pygame.quit()
            
           parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
           sys.path.append(parent_dir)
           
           result_window.destroy()
           self.fenetre.destroy()
           
           print("importing main")
           import run
           run.create_main_menu()
        Button(result_window, text="Close", command=back_to_menu).pack(pady=20)
        
    


if __name__ == "__main__":
    fenetre = Tk()
    game = MultiplayerSnakeGame(fenetre, 1, 'WASD')
