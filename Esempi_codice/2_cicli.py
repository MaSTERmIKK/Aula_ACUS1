controllore = True

while controllore:
    print(1)
    
    controllore = False

print("qui è finita")





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


risposta = True
while risposta:
    
    numero = int(input("inserisci un numero da fare il conto alla rovescia"))
    for i in range (numero, -1, -1):
        print(i)
    
    
    risposta = input("vuoi continuare?")
    if risposta == "no":
        risposta = False


while True:
    x = 10
    
    while True:
        
        pass
    
