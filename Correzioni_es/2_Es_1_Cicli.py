#controllore del ciclo
risposta = True

while risposta:

    # isnerimento e conto alla rovescia
    numero = int(input("inserisci un numero da fare il conto alla rovescia"))
    for i in range (numero, -1, -1):
        print(i)

    #controllo di rottura
    risposta = input("vuoi continuare?")
    if risposta == "no":
        risposta = False
