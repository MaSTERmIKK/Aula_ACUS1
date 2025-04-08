#esempio basilare
class Esempio():
    x = 10

#creazione oggetto basilare    
oggetto_1 = Esempio()
oggetto_2 = Esempio()

#modifica attiributo
oggetto_1.x = 20
oggetto_2.x = 50
print(oggetto_1.x)
print(oggetto_2.x)

class Penna():
    altezza=0
    larghezza=0
    
    # Metodo speciale: Costruttore
    def __init__(self,h,l):
        self.altezza = h
        self.larghezza = l
        
oggetto_penna = Penna(10,7)

print(oggetto_penna.altezza)
print(oggetto_penna.larghezza)

non_lo_so = Penna(5,6)

print(non_lo_so.altezza)
