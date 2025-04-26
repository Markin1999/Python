# 3. Implementare:
#    - Aggiunta di uno studente con input() controllato da try/except
#    - Visualizzazione di tutti gli studenti
#    - Ricerca di studenti per nome (case insensitive, usando lower() + filter)
#    - Ordinamento studenti per media (con sorted e lambda)
#    - Rimozione di studenti con gestione errori (try/except)
#    - Modifica dei voti di uno studente usando map
#    - Applicare un bonus casuale (+1 punto) a un voto usando random

# 4. Gestire correttamente errori:
#    - Input non valido (es. età non numerica)
#    - Studente non trovato
#    - Operazioni fallite (simulate in async)

# 5. Usare costrutti:
#    - for-in su liste e dizionari
#    - map() per trasformare liste
#    - filter() per filtrare studenti
#    - reduce() per sommare voti
#    - continue per saltare input errati

import util
import asyncio
    
async def main():
    util.mainPage()
    
    while True: 
        print("\nMenu Studenti")
        print("1. Aggiungi nuovo studente")
        print("2. Visualizza tutti gli studenti")
        print("3. Ottieni la media di uno studente")
        print("4. Mostra studenti ordinati per media")
        print("5. Esci")

        try:
            scelta = input("Scegli (1/2/3/4/5): ")
            if scelta == "1":
                await util.nuovoStudente()
            elif scelta == "2":
                studenti = await util.carica_Studente()
                for studente in studenti:
                    print(f"Nome: {studente.nome}, Età: {studente.età}, Voti: {studente.voti}, Media: {studente.calcola_media()}")
            elif scelta == "3":
                media = await util.ottieni_media()
                if media is not None:
                    print(f"La media dello studente è: {media:.2f}")
                else:
                    print("Studente non trovato.")
            elif scelta == "4":
                studenti = await util.ordinaMedia()
                for i, studente in enumerate(studenti):
                    print(f"{i + 1} Nome: {studente.nome}, Età: {studente.età}, Voti: {studente.voti}, Media: {studente.calcola_media()}")  
               
              
                    
                    
            elif scelta == "5":
                print("Uscita dal programma.")
                break 
            else:
                print("Scelta non valida, riprova!")

        except ValueError as ve:
            print(f"Errore: {ve}")
        except Exception as e:
            print(f"Errore imprevisto: {e}")


asyncio.run(main())
