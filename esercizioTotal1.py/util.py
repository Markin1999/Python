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
# 


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
import asyncio

studenti_db = []

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
            return obj  # Se trovato, torna lo studente

    print("Nessuno studente trovato")
    return None  # Se non trovato

async def ottieni_media():
    studente = await cerca_studente()
    
    if studente is None:
        return None  
    else:
        return sum(studente.voti) / len(studente.voti)
