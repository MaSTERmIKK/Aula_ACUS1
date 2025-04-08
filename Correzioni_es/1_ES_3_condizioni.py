# creazione variabili
nome = ""
password= ""
id=0
x = True

#condizioni

#Registrazione
if x:
    nome = input("inserisci il tuo nickname")
    password = input("inserisci la tua password")
    id +=1
    
#Login
if nome == "":
    print("non hai valorizato")
else:
    nome_inserito = input("inserisci il tuo nickname")
    password_inserito = input("inserisci la tua password")
    
    if nome_inserito == nome and password_inserito == password:
        print("sei loggato") 
