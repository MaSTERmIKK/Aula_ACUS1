import random

def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    
    while True:
        tentativo = input("Indovina il numero (o digita 'esci' per terminare): ")
        if tentativo.lower() == 'esci':
            print("Hai deciso di uscire. Il numero era:", numero_da_indovinare)
            break

        tentativo = int(tentativo)

        if tentativo == numero_da_indovinare:
            print("Bravo! Hai indovinato il numero!")
            break
        elif tentativo < numero_da_indovinare:
            print("Troppo basso!")
        else:
            print("Troppo alto!")

# Esegui la funzione
indovina_il_numero()
