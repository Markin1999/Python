# 2. Creare funzioni asincrone:
#    - salva_studente(studente) --> simula salvataggio su "database" con await
#    - carica_studenti() --> simula caricamento dati con await

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
#    - continue per saltare input errati

from studente import Studente
import asyncio

studenti_db = []

def mainPage():
    a = Studente("Marco", 25, [6,9,3])
    b = Studente("Kekko", 25, [8,9,5])
    c = Studente("Luigi", 20, [2,9,7])
    
    studenti_db.extend([a, b, c])


async def nuovoStudente ():
    try:
        nome = input("Inserisci il nome: ")
        età = int(input("Inserisci l' eta"))
    
        voti = []
        
        i = int(input("Quanti voti vuoi inserire? "))
        
        for n in range(i):
            while True:  
                try:
                    voto = int(input(f"Inserisci il {n+1}° voto: "))
                    voti.append(voto)
                    break  
                except ValueError:
                    print("Errore: devi inserire un numero per il voto!")

        studente = Studente(nome, età, voti)

        await salva_Studente(studente)
        
        
    except ValueError:
        print("Errore: Devi inserire un numero valido!")
        
    except Exception as e:
        print("Errore imprevisto:", e)
        

async def salva_Studente(studente):
    
    print(f"Salvataggio di {studente.nome} in corso...")
    await asyncio.sleep(1)
    studenti_db.append(studente)
    
    asyncio

async def carica_Studente():
    print(f"Caricamento in corso...")
    await asyncio.sleep(1)
    
    return (studenti_db)

async def cerca_studente():
    nome = input("Cerca per nome: ").lower()
    
    for obj in studenti_db:
        if obj.nome.lower() == nome:
            return obj  

    print("Nessuno studente trovato")
    return None  

async def ottieni_media():
    studente = await cerca_studente()
    
    if studente is None:
        return None  
    else:
        return sum(studente.voti) / len(studente.voti)

async def ordinaMedia():
    studenti_ordinati = sorted(studenti_db, key= lambda x: x.calcola_media())
    print(f"Caricamento in corso...")
    await asyncio.sleep(1)
    return (studenti_ordinati)



async def eliminaStudente():
    studente = await cerca_studente()
    
    if studente is None:
        return None  
    else:
        studenti_db.remove(studente)