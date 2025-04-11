import sqlite3  # Importa il modulo per lavorare con SQLite

# 1. Connessione (crea un file 'miodatabase.db' se non esiste)
conn = sqlite3.connect('miodatabase.db')

# 2. Cursore per eseguire comandi SQL
cur = conn.cursor()

# 3. Creazione di una tabella (se non esiste)
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

# 4. Inserimento di un dato
cur.execute("INSERT INTO utenti (nome) VALUES (?)", ("Mirko",))

# 5. Salvataggio delle modifiche
conn.commit()

# 6. Query per leggere i dati
cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()

# 7. Stampa dei risultati
for riga in righe:
    print(riga)

# 8. Chiusura della connessione
conn.close()
