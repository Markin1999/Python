# Esercizio: "Lista della Spesa Intelligente"
#Scrivi un programma che:
#Chiede all’utente di inserire articoli della spesa (nome e quantità)
#Salva ogni articolo in un dizionario con nome e quantità
#Evita i duplicati usando un set
#Al termine, stampa un riepilogo in ordine alfabetico (usa una lista di tuple per farlo)
#Chiede all’utente se vuole cercare un articolo e ne mostra i dettagli

inseriti = set()
spesa = {}

number = int(input("Quanti articoli vuoi inserire nella lista?: "))

for i in range(number): 
    
    print("Inserisci articoli nella spesa")
    nome = input("Inserisci nome: ").lower()

    if nome in inseriti:
        print("Nome già inserito.")
        quantita = int(input("Inserisci nuova quantità: "))
        spesa[nome] = quantita  
    else:
        quantita = int(input("Inserisci quantità: "))
        spesa[nome] = quantita
        inseriti.add(nome)

print(spesa)



