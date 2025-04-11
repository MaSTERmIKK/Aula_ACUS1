import sqlite3
import random

class Libreria:
    def __init__(self, nome_db="libreria.db"):
        self.conn = sqlite3.connect(nome_db)
        self.cur = self.conn.cursor()
        self.crea_tabella()

    def crea_tabella(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS libri (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titolo TEXT,
                autore TEXT
            )
        ''')
        self.conn.commit()

    def inserisci_libri(self, lista_libri):
        self.cur.executemany('''
            INSERT INTO libri (titolo, autore) VALUES (?, ?)
        ''', lista_libri)
        self.conn.commit()

    def mostra_libri(self):
        self.cur.execute('SELECT id, titolo, autore FROM libri')
        libri = self.cur.fetchall()
        for libro in libri:
            print(f"ID: {libro[0]}, Titolo: {libro[1]}, Autore: {libro[2]}")

    def aggiungi_colonna_vendite(self):
        try:
            self.cur.execute('ALTER TABLE libri ADD COLUMN vendite INTEGER')
        except sqlite3.OperationalError:
            # La colonna esiste già
            pass

        self.cur.execute('SELECT id FROM libri')
        ids = [r[0] for r in self.cur.fetchall()]
        for libro_id in ids:
            vendite_random = random.randint(10, 1000)
            self.cur.execute('UPDATE libri SET vendite = ? WHERE id = ?', (vendite_random, libro_id))
        self.conn.commit()

    def chiudi(self):
        self.conn.close()

# --- Uso della classe Libreria ---
libri_iniziali = [
    ("Il nome della rosa", "Umberto Eco"),
    ("1984", "George Orwell"),
    ("Il piccolo principe", "Antoine de Saint-Exupéry")
]

libreria = Libreria()
libreria.inserisci_libri(libri_iniziali)
print("Libri inseriti:")
libreria.mostra_libri()

libreria.aggiungi_colonna_vendite()
print("\nLibri con vendite aggiunte:")
libreria.mostra_libri()

libreria.chiudi()
