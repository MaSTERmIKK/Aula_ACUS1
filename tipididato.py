numeroconlavirgola = 3.56

#tipi numerici
intero = int(input("inserisci un intero"))
virgola = float(input("inserisci un numero con la virgola"))

# tipi semantici
stringa = input("inserisci una parola")
print(stringa[0])
print(stringa.lower())



#valori booleani

x= False
y= True

print(5>11)
print(13<50)


#liste 

lista_dati = [1,4,2,3,0]
lista_dati2 = [1,"mirko", True]
lista_dati3 = []

print(lista_dati)
print(lista_dati[2])
print(lista_dati2[1])
lista_dati.sort()
print(lista_dati)

inserimento = int(input("inserisci un numero"))
lista_dati3.append(inserimento)
inserimento = int(input("inserisci un numero"))
lista_dati3.append(inserimento)

print(lista_dati3)

x =  5
x += 5