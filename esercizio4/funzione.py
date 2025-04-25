# Importa la funzione analizza_lista dal modulo util

# Crea una lista di numeri, ad esempio: [3, 5, 1, 4, 2]

# Chiama la funzione analizza_lista passando la lista come argomento
# Salva i due valori restituiti in due variabili, ad esempio: quadrati, maggiore_di_10

# Stampa:
# - la lista originale
# - la lista dei quadrati ordinati
# - quanti valori sono maggiori di 10

from modulo import analizza_lista

numeri = [3, 5, 1, 4, 2]

quadrati, maggiore_di_10 = analizza_lista(numeri)

print("Lista originale:", numeri)
print("Quadrati ordinati:", quadrati)
print("Numeri maggiori di 10:", maggiore_di_10)