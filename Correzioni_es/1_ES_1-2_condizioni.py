lista = ["mirko", "paolo", "pippo"]

scelta = input("scegli cosa vuoi fare")

if scelta.lower() == "e":
    print(lista)
    scelta = input("scegli cosa vuoi eliminare")
    lista.remove(scelta)
    print(lista)
elif scelta.lower() == "a":
    scelta = input("Dimmi cosa vuoi aggiungere")
    lista.append(scelta)
    print(lista)
elif scelta.lower() == "m":
    print(lista)
    scelta = int(input("Dimmi quale posizione vuoi modificare da 0 a 2"))
    scelta2 = input("Dimmi cosa vuoi aggiungere")
    lista[scelta]= scelta2
    print(lista)
else:
    print("comando sbagliato")


numero_scelto =int(input("dammi un numero superiore a 10"))
if numero_scelto > 10:
    
    numero_scelto =int(input("dammi un numero superiore a 20"))
    if numero_scelto > 20:
        
            numero_scelto =int(input("dammi un numero superiore a 50"))
            if numero_scelto > 50:
                
                print("sei arrivato al terzo livello di profondità")
                
                
                
            else: 
                print("numero inferiore a 50")
    else: 
        print("numero inferiore a 20")
else: 
    print("numero inferiore a 10")
