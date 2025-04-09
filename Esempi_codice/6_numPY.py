import numpy as np

# 1. Creare un array NumPy da una lista
lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print("Array da lista:", array)

# 2. Creare array di zeri e uni
zeri = np.zeros(5)  # array di 5 zeri
print("Zeri:", zeri)

uni = np.ones((2, 3))  # matrice 2x3 di uni
print("Uni:\n", uni)

# 3. Creare array con range
range_array = np.arange(0, 10, 2)  # da 0 a 10 escluso, passo 2
print("Range array:", range_array)

# 4. Creare un array con valori equidistanti
lin = np.linspace(0, 1, 5)  # 5 valori da 0 a 1 inclusi
print("Linspace:", lin)

# 5. Operazioni base tra array
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("Somma:", a + b)
print("Moltiplicazione:", a * b)

# 6. Indicizzazione e slicing
print("Primo elemento di a:", a[0])
print("Ultimi due elementi di b:", b[-2:])

# 7. Funzioni statistiche base
print("Media di b:", np.mean(b))
print("Massimo di b:", np.max(b))
print("Somma di b:", np.sum(b))

# 8. Reshape di array
c = np.array([1, 2, 3, 4, 5, 6])
c_reshaped = c.reshape((2, 3))  # da vettore a matrice 2x3
print("Array reshaped:\n", c_reshaped)

# 9. Matrice identità
identita = np.eye(3)  # matrice identità 3x3
print("Matrice identità:\n", identita)

# 10. Array casuali
casuali = np.random.rand(4)  # 4 numeri casuali tra 0 e 1
print("Numeri casuali:", casuali)
