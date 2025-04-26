# Mini-Progetto: Gestione avanzata Studenti 🎓

# 🎯 Obiettivo:
# Creare un sistema completo di gestione studenti usando:
# - Python OOP (classi e oggetti)
# - Liste, dizionari, metodi avanzati (map, filter, reduce, for-in)
# - Funzioni asincrone (async/await)
# - Gestione errori (try/except)
# - Moduli separati (più file .py)
# - Uso di funzioni built-in come sorted(), len(), lower(), ecc.

# 📦 Organizzazione file:
# 1. studente.py --> definizione della classe Studente
# 2. utils.py --> funzioni utili (input, stampa, operazioni asincrone)
# 3. main.py --> logica principale del programma

# 🛠️ Funzionalità richieste:
# 1. Creare una classe Studente con attributi:
#    - nome (str)
#    - età (int)
#    - voti (lista di int)
#    e metodi:
#    - calcola_media() --> restituisce la media dei voti usando reduce
#    - saluta() --> stampa un messaggio personalizzato

class Studente:
    def __init__(self, nome, età, voti):
        self.nome = nome
        self.età = età
        self.voti = voti
    
    def calcola_media(self):
        if not self.voti:  # Evita divisione per zero
            return 0
        else:
            return sum(self.voti) / len(self.voti)
    
    def saluta(self):
        print(f"Ciao! Mi chiamo {self.nome} e ho {self.eta} anni.")
        
        
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

# 5. Usare costrutti:
#    - for-in su liste e dizionari
#    - map() per trasformare liste
#    - filter() per filtrare studenti
#    - reduce() per sommare voti
#    - continue per saltare input errati

# 🔥 Challenge Extra:
# - Creare una funzione asincrona che applica un "bonus day" (sceglie uno studente a caso e aggiunge 1 punto a tutti i suoi voti).
# - Salvare gli studenti in una lista globale gestita in memoria.

# 📌 Requisiti stilistici:
# - Ogni funzione deve avere commento di spiegazione
# - Codice modulare e ben organizzato
# - Uso di nomi chiari per variabili e funzioni
