from tkinter import *
from random import randint

class SnakeGame:
    def __init__(self, fenetre, speed):
        self.fenetre = fenetre
        self.speed = speed
        self.paused = False

        if speed == 1:
            self.delay = 200  # Slow
        elif speed == 2:
            self.delay = 100  # Medium
        elif speed == 3:
            self.delay = 50  # Fast

        self.fenetre.title('Drake The Snake')
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
        self.Barre.insert(END, "score: 0\n")

        self.pause_button = Button(self.top_frame, text="Pause", command=self.change_pause)
        self.pause_button.pack(side="right", padx=10, pady=10)

        self.NombreDeCases = 75
        self.LargeurCase = (self.LargeurPlateau / self.NombreDeCases)
        self.HauteurCase = (self.HauteurPlateau / self.NombreDeCases)

        self.fenetre.bind("<Left>", self.left_key)
        self.fenetre.bind("<Right>", self.right_key)
        self.fenetre.bind("<Up>", self.up_key)
        self.fenetre.bind("<Down>", self.down_key)

        self.reinitialiser_jeu()
        self.fenetre.after(0, self.tache)
        self.fenetre.mainloop()

    def change_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.tache()

    def remplir_case(self, x, y):
        OrigineCaseX1 = x * self.LargeurCase
        OrigineCaseY1 = y * self.HauteurCase
        OrigineCaseX2 = OrigineCaseX1 + self.LargeurCase
        OrigineCaseY2 = OrigineCaseY1 + self.HauteurCase
        self.Plateau.create_rectangle(OrigineCaseX1, OrigineCaseY1, OrigineCaseX2, OrigineCaseY2, fill="black")

    def case_aleatoire(self):
        AleatoireX = randint(0, self.NombreDeCases - 1)
        AleatoireY = randint(0, self.NombreDeCases - 1)
        return (AleatoireX, AleatoireY)

    def dessine_serpent(self):
        for case in self.SNAKE:
            x, y = case
            self.remplir_case(x, y)

    def etre_dans_snake(self, case):
        return case in self.SNAKE

    def fruit_aleatoire(self):
        FruitAleatoire = self.case_aleatoire()
        while self.etre_dans_snake(FruitAleatoire):
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
        self.MOUVEMENT = (-1, 0)

    def right_key(self, event):
        self.MOUVEMENT = (1, 0)

    def up_key(self, event):
        self.MOUVEMENT = (0, -1)

    def down_key(self, event):
        self.MOUVEMENT = (0, 1)

    def serpent_mort(self, NouvelleTete):
        NouvelleTeteX, NouvelleTeteY = NouvelleTete
        if self.etre_dans_snake(NouvelleTete) and self.MOUVEMENT != (0, 0) or NouvelleTeteX < 0 or NouvelleTeteY < 0 or NouvelleTeteX >= self.NombreDeCases or NouvelleTeteY >= self.NombreDeCases:
            self.PERDU = 1

    def mise_a_jour_score(self):
        self.SCORE += 1
        self.Barre.delete(0.0, 3.0)
        self.Barre.insert(END, "score: " + str(self.SCORE) + "\n")

    def mise_a_jour_snake(self):
        AncienneTeteX, AncienneTeteY = self.SNAKE[0]
        MouvementX, MouvementY = self.MOUVEMENT
        NouvelleTete = (AncienneTeteX + MouvementX, AncienneTeteY + MouvementY)
        self.serpent_mort(NouvelleTete)
        self.SNAKE.insert(0, NouvelleTete)
        if NouvelleTete == self.FRUIT:
            self.FRUIT = self.fruit_aleatoire()
            self.mise_a_jour_score()
        else:
            self.SNAKE.pop()

    def reinitialiser_jeu(self):
        self.SNAKE = [self.case_aleatoire()]
        self.FRUIT = self.fruit_aleatoire()
        self.MOUVEMENT = (0, 0)
        self.SCORE = 0
        self.PERDU = 0

    def tache(self):
        if not self.paused:
            self.fenetre.update_idletasks()
            self.mise_a_jour_snake()
            self.Plateau.delete("all")
            self.dessine_fruit()
            self.dessine_serpent()
            if self.PERDU:
                self.Barre.delete(0.0, 3.0)
                self.Barre.insert(END, "Perdu avec un score de " + str(self.SCORE))
                self.reinitialiser_jeu()
                self.fenetre.after(70, self.tache)
            else:
                self.fenetre.after(self.delay, self.tache)

if __name__ == "__main__":
    fenetre = Tk()
    game = SnakeGame(fenetre, 1)
