# Lettura del file
file = open("esempio_testo.txt" , "r")
tutte_le_righe = file.read()
riga = file.readline()
print(tutte_le_righe)
file.close()

# Scrittura di file
file = open("esempio_testo2.txt" , "w")
file.write("Sto sostituendo il testo")
file.close()

# Aggiunta al file di file
file = open("esempio_testo2.txt" , "a")
file.write(" Sto Aggiugendo al testo")
file.close()


# Senza bisogno della chiusura
with open("esempio_testo_nuovo.txt" , "w") as file:
    file.write("Auto chiudo la mia chiamata")


with open("esempio_testo_nuovo.txt" , ) as file:
    pass
