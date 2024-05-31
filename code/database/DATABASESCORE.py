import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect('snake_game_scores.db')
c = conn.cursor()

# Création de la table des scores
c.execute('''
          CREATE TABLE IF NOT EXISTS scores
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          player_name TEXT NOT NULL,
          score INTEGER NOT NULL,
          date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
          ''')

# Sauvegarder (commit) les changements et fermer la connexion
conn.commit()
conn.close()

def add_score(player_name, score):
    conn = sqlite3.connect('snake_game_scores.db')
    c = conn.cursor()
    c.execute('INSERT INTO scores (player_name, score) VALUES (?, ?)', (player_name, score))
    conn.commit()
    conn.close()

# Exemple d'utilisation :
add_score('Alice', 150)
add_score('Bob', 200)

def get_scores():
    conn = sqlite3.connect('snake_game_scores.db')
    c = conn.cursor()
    c.execute('SELECT player_name, score, date FROM scores ORDER BY score DESC')
    scores = c.fetchall()
    conn.close()
    return scores

# Exemple d'utilisation :
scores = get_scores()
for score in scores:
    print(f"Player: {score[0]}, Score: {score[1]}, Date: {score[2]}")
