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
from studente import Studente
import util
import asyncio

async def nuovoStudente ():
    try:
        nome = input("Inserisci il nome: ")
        età = int(input("Inserisci l' eta"))
    
        voti = []
        
        i = int(input("Quanti voti vuoi inserire? "))
        
        for n in range(i):
            while True:  # Fino a quando non scrive un voto corretto
                try:
                    voto = int(input(f"Inserisci il {n+1}° voto: "))
                    voti.append(voto)
                    break  
                except ValueError:
                    print("Errore: devi inserire un numero per il voto!")

        studente = Studente(nome, età, voti)

        await util.salva_Studente(studente)
        await main()
        
    except ValueError:
        print("Errore: Devi inserire un numero valido!")
        
    except Exception as e:
        print("Errore imprevisto:", e)
        
    
async def main():
    
    print("1. Aggiungi nuovo studente")
    print("2. Visualizza tutti gli studenti")
    print("3. Ottieni la media di uno studente")

    try:
        scelta = input("Scegli (1/2/3): ")
        if scelta == "1":
            await nuovoStudente()
        elif scelta == "2":
            studenti = await util.carica_Studente()  # Aspetta che carichi gli studenti
            for studente in studenti:
                print(f"Nome: {studente.nome}, Età: {studente.età}, Voti: {studente.voti}")
        elif scelta == "3":
            media = await util.ottieni_media()
            if media is not None:
                print(f"La media dello studente è: {media:.2f}")
            else:
                print("Studente non trovato.")

        else: 
            raise ValueError("Scelta non valida.")
            

    except ValueError as ve:
        print(f"Errore: {ve}")
        
asyncio.run(main())