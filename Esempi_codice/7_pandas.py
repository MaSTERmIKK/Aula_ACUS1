import pandas as pd

# 1. Creare un DataFrame da un dizionario
dati = {
    'Nome': ['Anna', 'Luca', 'Marco'],
    'Età': [23, 30, 25],
    'Città': ['Roma', 'Milano', 'Torino']
}
df = pd.DataFrame(dati)
print("DataFrame:\n", df)

# 2. Leggere un file CSV (qui simulato con un esempio)
# df_csv = pd.read_csv('file.csv')  # scommenta se hai un file CSV

# 3. Visualizzare le prime righe
print("\nPrime righe del DataFrame:")
print(df.head())  # di default mostra le prime 5 righe

# 4. Informazioni generali sul DataFrame
print("\nInformazioni:")
print(df.info())

# 5. Statistiche descrittive
print("\nStatistiche descrittive:")
print(df.describe())

# 6. Selezionare una colonna
print("\nColonna 'Nome':")
print(df['Nome'])

# 7. Selezionare una riga con il metodo loc
print("\nRiga con indice 1:")
print(df.loc[1])  # seleziona la seconda riga

# 8. Aggiungere una nuova colonna
df['Punti'] = [80, 95, 70]
print("\nDataFrame con nuova colonna 'Punti':")
print(df)

# 9. Filtrare righe con condizione
over_25 = df[df['Età'] > 25]
print("\nPersone con età > 25:")
print(over_25)

# 10. Ordinare i dati
ordinato = df.sort_values(by='Punti', ascending=False)
print("\nDataFrame ordinato per 'Punti':")
print(ordinato)

# 11. Salvare il DataFrame in un file CSV
# df.to_csv('output.csv', index=False)  # scommenta per salvare
