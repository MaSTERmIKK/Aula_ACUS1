def fibonacci_fino_a_n():
    n = int(input("Inserisci un numero: "))
    a, b = 0, 1

    while a <= n:
        print(a)
        a, b = b, a + b

# Esegui la funzione
fibonacci_fino_a_n()
