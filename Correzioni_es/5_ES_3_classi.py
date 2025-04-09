#classe libro
class Libro():
    
    def __init__(self, titolo, autore, nr_pag):
        self.titolo = titolo
        self.autore = autore
        self.nr_pag = nr_pag
        
    def stampa(self):
        print(self.titolo)
        print(self.autore) 
        print(self.nr_pag)
        
class Biblioteca():
    libri = []
    
    def __init__(self):
        self.libri = []
        
    def aggiungi_libro(self, titolo, autore, nr_pag):
        libro = Libro(titolo, autore, nr_pag)
        self.libri.append(libro)
        
    def stampa_libri(self):
        for x in self.libri:
            x.stampa()
            
Bilioteca_mia = Biblioteca()

while True:
      
    titolo = input("inserisci il titolo")
    autore = input("inserisci l'autore")
    nr_pag = int(input("inserisci il numero pagine"))
    
    Bilioteca_mia.aggiungi_libro(titolo, autore, nr_pag)
    
    Bilioteca_mia.stampa_libri()
    
    
    scelta_ciclo = input("vuoi ripetere?")
    if scelta_ciclo.lower == "si":
        continue
    else:
        break