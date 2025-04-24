# 🧠 Esercizio Completo: Libreria Virtuale

# 🎯 Obiettivo: creare un'applicazione Python che simula la gestione di una libreria.

# ✍️ Requisiti:
# 1. Chiedi all’utente quanti libri vuole inserire
# 2. Per ogni libro, chiedi:
#    - Titolo
#    - Autore
#    - Anno di pubblicazione
# 3. Ogni libro deve essere salvato come una tupla: (titolo, autore, anno)
# 4. Le tuple vanno salvate dentro una lista chiamata `libreria`
# 5. Evita duplicati usando un set `libri_inseriti` con chiavi tipo "titolo-autore"
# 6. Al termine, stampa l’elenco dei libri ordinati alfabeticamente per titolo
# 7. Chiedi all’utente se vuole cercare un libro per titolo. Se lo trova, mostra autore e anno.
# 8. Crea un dizionario `libri_per_autore` dove le chiavi sono gli autori e i valori il numero di libri che hanno scritto
# 9. Stampa il numero di libri per ogni autore

# 🧩 Usa tutto ciò che hai imparato:
# - input(), print()
# - if, for, while
# - list, tuple, dict, set
# - sorted(), lower(), in

lista = []
libriInseriti = set()

number = int(input("quanti libri inserire? "))

for _ in range(number):
    
    print("\n📥 Inserisci un nuovo libro:")
    titolo = input("Inserisci un titolo: ").lower()
    autore = input("Inserisci un autore: ").lower()
    anno = int(input("Inserisci un anno di pubblicazione: "))
    
    if titolo in libriInseriti:
        print("Libro gia presente, salta l'inserimento")
        continue
    
    libro = (titolo, autore, anno)
    
    lista.append(libro)
    
    libriInseriti.add(titolo)
    
    print(sorted(lista))

risposta = input("vuoi cercare un nuovo titolo? (s/n)").lower()

if risposta == "s":
    nome = input("Inserisci nome: ")
    for titolo in lista:
        if nome == titolo[0]:
            libro = (titolo[0], titolo[1], titolo[2])
            print(libro)
    
elif risposta == "n":
    print("Ok, niente ricerca.")
else:
    print("Risposta non valida.")

    
