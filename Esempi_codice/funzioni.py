#semantica delle funzioni
def nome_della_funzione ():
    pass
    
#funzione di esecuzione
def saluta():
    print ("ciao")
    
saluta()

#funzioni con parametri 
def somma(x,y,z):
    risulato= x+y+z
    print(risulato)
    
somma(1,2,2)

def saluta_con_parametro(nome):
    print ("ciao", nome)
    
saluta_con_parametro("Alice")

#funzione di ritorno
def riporta_dato(x):
    risultato = x*x
    return risultato

numero = riporta_dato(3)
print(riporta_dato(3))

somma(riporta_dato(3), riporta_dato(3), riporta_dato(3) )

if riporta_dato(3) > 10:
    pass
else:
    pass

#funzione di ritorno con input interno
def riporta_dato_senza_parametri():
    x = int(input("dammi un numero da elevare in potenza"))
    return x*x

#funzione con parametri standard
def funzione_standard(x = 1):
    return x+x

print(funzione_standard())