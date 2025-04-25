# Crea una funzione chiamata "analizza_lista" che prende una lista di numeri come parametro

# All'interno della funzione:
# 1. Crea una nuova lista vuota chiamata "quadrati"
# 2. Con un ciclo for, aggiungi a "quadrati" il quadrato di ogni numero nella lista originale (usa .append)
# 3. Ordina la lista "quadrati" in ordine crescente (usa .sort)
# 4. Con un ciclo while, conta quanti numeri nella lista "quadrati" sono maggiori di 10
# 5. Ritorna sia la lista dei quadrati che il numero di valori maggiori di 10

def analizza_lista(numeri):
    quadrati = []
    
    for numero in numeri:
        nuovoNumero = numero ** 2
        quadrati.append(nuovoNumero)
    
    quadrati.sort()

    i=0
    conta = 0 
    while i < len(quadrati):
        if quadrati[i] > 10:
            conta += 1
            print("Totale numeri > 10:", conta)
        i+=1
         
    return quadrati, conta