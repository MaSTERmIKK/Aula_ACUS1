# Lista per salvare i numeri pari trovati
numeri_pari = []

# Ciclo finché non abbiamo trovato 5 numeri pari
while len(numeri_pari) < 5:
    numero = int(input("Inserisci un numero: "))
    
    if numero % 2 == 0:
        print("Il numero è pari")
        numeri_pari.append(numero)
    else:
        print("Il numero non è pari")

# Alla fine stampa i numeri pari raccolti
print("Hai inserito 5 numeri pari:", numeri_pari)
