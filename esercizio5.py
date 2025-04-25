# 📝 ESERCIZIO: Calcolatrice con gestione errori

# 1. Chiedi all'utente di inserire due numeri (usa input())
# 2. Poi chiedi quale operazione vuole fare: +, -, * o /
# 3. Usa un blocco try-except per:
#    - gestire se l'utente inserisce un valore non numerico (ValueError)
#    - gestire la divisione per zero (ZeroDivisionError)
#    - opzionale: gestire un'operazione non riconosciuta

# 4. Se tutto va bene, stampa il risultato dell'operazione
# 5. Alla fine del programma, stampa sempre "Calcolo terminato" (usando finally)

# Suggerimento:
# Usa int() o float() per convertire gli input numerici
# E un blocco if-elif-else per gestire le operazioni scelte
try:

    numeroUno = int(input("Inserisci il primo numero: "))
    numeroDue = int(input("Inserisci il secondo numero: "))

    operazione = input("Quale operazione vuoi fare? (+, -, *, /): ")

    if operazione == "+":
        risultato = numeroDue + numeroUno
    
    elif operazione == "-":
        risultato = numeroUno - numeroDue
        
    elif operazione == "/":
        risultato = numeroUno/numeroDue
    
    elif operazione == "*":
        risultato = numeroUno*numeroDue
    
    else:
       raise ValueError("Non hai inserito l'operazione giusta")
        

except ValueError as ve: #conserviamo il valore che abbiamo inserito con raise
    print("Errore di input:", ve)

except ZeroDivisionError:
    print("Errore: non puoi dividere per zero!")

finally: #si verifica sempre
    print("Calcolo terminato ✅")
    

    
    


    