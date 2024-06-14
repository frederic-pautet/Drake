**Drake The Snake (menu)**

This project is a graphical user interface (GUI) for the Snake Game Menu using Tkinter in Python. The menu allows users to select different game modes, view highscores, show game rules, and exit the game. The game modes include Classic, Trivia, and Multiplayer. library for the graphical interface and Pygame for sound effects.

**Table of Contents**

- [Installation](#_page0_x0.00_y42.00)
- [Usage](#_page0_x0.00_y42.00)
- [Project Structure](#_page0_x0.00_y842.00)
- [Code Explanation](#_page0_x0.00_y842.00)

**Installation**

**Steps**

1\.

Clone the repository:

git clone https://github.com/yourusername/snake-game-menu.git  cd snake-game-menu

2\.

Ensure the following files and directories are in place:

- run.py
- Interfaces/ClassicMenu.py
- Interfaces/TriviaMenu.py
- Interfaces/MultiplayerMenu.py
- Interfaces/HighscoresWindow.py
- database/rules.json
- database/highscores.json
- database/questions.json

**Usage**

1\.

Run the main menu script:

python code/run.py 

2\.

Interacting with the menu:

- Classic Mode: Start the classic Snake game.
- Trivia Mode: Start the trivia version of the Snake game.
- Multiplayer Mode: Start the multiplayer version of the Snake game.
- Highscores: View the highscores.
- Show Rules: Display the main rules of the game.
- Leave<a name="_page0_x0.00_y842.00"></a> Game: Exit the application.

**Project Structure**

- code/run.py: The main script to launch the game menu.
- Interfaces/: Directory containing the modules for different game modes and highscores.
- ClassicMenu.py
- TriviaMenu.py
- MultiplayerMenu.py
- HighscoresWindow.py
- database/rules.json : JSON file containing the game rules.
- database/questions.json : JSON file containing the trivia questions and their answers.
- database/highscores.json : JSON file containing the players' scores. It can be modified while playing.


**Code Explanation**

1\.

create\_main\_menu() : This function creates the main window for the game menu and adds buttons for each game mode, highscores, game rules, and exit.

2\.

start\_game(mode): A placeholder function to start a game mode.

3\.

show\_highscores(): A placeholder function to display the highscores.

4\.

show\_rules(root): Reads and displays the game rules from rules.json in a message box. 5.

leave\_game(root): Closes the application.

**Drake The Snake (classic mode)**

This is a classic Snake game implemented using Python's Tkinter library for the graphical interface and Pygame for sound effects.

**How to Play**

Use the arrow keys to control the direction of the snake. The goal is to eat the red fruits that appear on the screen. Each fruit increases your score by 1 and makes the snake longer. The game ends if the snake collides with the screen edges or itself.

**Code Overview**

The main components of the code are:

1\.

**Initialization**: The game initializes the Tkinter window, Pygame sound, and sets up the game dimensions

based on the screen size. 2.

**Drawing Functions**:

- remplir\_case(x, y): Draws a filled rectangle representing a part of the snake.
- dessine\_serpent(snake): Draws the entire snake.
- dessine\_fruit(): Draws the fruit as a red oval.

3\.

**Game Mechanics**:

- case\_aleatoire(): Generates random positions for the snake and fruit.
- etre\_dans\_snake(case): Checks if a position is part of the snake.
- fruit\_aleatoire(): Generates a random fruit position that is not occupied by the snake.
- mise\_a\_jour\_snake(): Updates the snake's position and handles collisions with the fruit and edges.

4\.

**Controls**:

- Functions like left\_key(event), right\_key(event), etc., handle the arrow key inputs to change the snake's direction.

5\.

**Game Loop**:

- tache(): The main game loop that updates the game state and redraws the graphics every 70 milliseconds.

6\.

**Game Over**:

- serpent\_mort(NouvelleTete): Checks if the snake has collided with the edges or itself.
- afficher\_fenetre\_perdu(): Displays a game-over window with the score and options to replay.

**Drake The Snake (multiplayer mode)**

This is a Python implementation of a multiplayer snake game using the Tkinter library for the graphical user interface.

**Table of Contents**

- Features (#features)
- [Configuration](#_page4_x0.00_y842.00)
- [Code Explanation](#_page4_x0.00_y842.00)

**Features**

- Fullscreen gameplay
- Two-player support :
  - Player 1: Arrow keys
  - Player 2: Configurable control scheme (WASD or ZQSD)
- Three speed settings: Slow, Medium, Fast
- Pause and resume functionality
- Game over screen with play again and main menu options


**Usage**

1\.controls

-Player 1 (Arrow keys)

- Up: Up Arrow
- Down: Down Arrow
- Left: Left Arrow
- Right: Right Arrow

-Player 2 (WASD or ZQSD) Default control scheme is WASD.

- Up: Z
- Down: S
- Left: Q
- Right: D

2\.Playing the Game:

- Use the arrow keys to move the snake..
- Answer trivia questions by moving the snake to the correct answer position.
- The game updates the score for correct answers and ends if the snake collides with itself or the walls.

**Configuration**

You can customize the game speed and control scheme when starting the game by calling the start\_multiplayer\_snake\_game function with the desired parameters.

- example : start\_multiplayer\_snake\_game('Fast', 'WASD')

**Code Explanation**

- **init**: Initializes the game window, canvas, controls, and other settings.
- setup\_controls: Sets up the control bindings for both players.
- change\_pause: Toggles the game's pause state.
- remplir\_case: Fills a grid cell with a specified color.
- case\_aleatoire: Generates a random grid cell.
- dessine\_serpent: Draws a snake on the canvas.
- etre\_dans\_snake: Checks if a cell is part of a snake.
- fruit\_aleatoire: Generates a random position for the fruit.
- dessine\_fruit: Draws the fruit on the canvas.
- serpent\_mort: Checks if a snake has collided with itself or the boundaries.
- mise\_a\_jour\_score: Updates the score display.
- mise\_a\_jour\_snake: Updates the position of the snakes.
- reinitialiser\_jeu: Resets the game state.
- tache: Main game loop, handling the game state updates and rendering.
- show\_result: Displays the game over screen with options to play again or return to the main menu.

**Drake The Snake (trivia mode)**

This project is a trivia mode for the "Drake The Snake" game, combining the classic Snake gameplay with trivia questions. The game is developed using Tkinter for the GUI and Pygame for sound effects.


**Usage**

Playing the Game:

- Use the arrow keys to move the snake..
- Answer trivia questions by moving the snake to the correct answer position.
- The game updates the score for correct answers and ends if the snake collides with itself or the walls.

**Project Structure**

- trivia\_mode.py: The main script to launch the trivia mode of the game.
- questions.json: JSON file containing the trivia questions and answers. <a name="_page6_x0.00_y842.00"></a>•

**Code Explanation**

-charger\_questions(): Loads trivia questions from the questions.json file.

-remplir\_case(x, y): Fills a grid cell at the given coordinates.

-case\_aleatoire(): Returns random coordinates for a grid cell.

-dessine\_serpent(snake): Draws the snake on the canvas.

-etre\_dans\_snake(case): Checks if a given cell is part of the snake.

-Arrow Key Handlers Functions to update the direction of the snake based on arrow key presses: 1.left\_key(event)

2\.right\_key(event)

3\.up\_key(event)

4\.down\_key(event)

-serpent\_mort(NouvelleTete): Checks if the snake has collided with itself or the boundaries. -mise\_a\_jour\_score(): Updates the score displayed on the screen.

-mise\_a\_jour\_snake(): Updates the snake's position and checks for collisions.

-reinitialiser\_jeu(): Resets the game state for a new game.

-afficher\_question(): Displays the current trivia question and options on the canvas.

-verifier\_reponse(): Checks if the snake's position matches the correct answer and updates the game state accordingly.

-afficher\_felicitations(): Displays a congratulatory message when all questions are answered correctly. -tache(): The main game loop that updates the game state and GUI.
