import random

print("Indovina il numero")

randomNumber = random.randint(1, 10)

number = int(input("Inserisci un numero da 1 a 10: "))

x = 0

while x < 3:
    print("Tentativi:", x)
    number = int(input("Inserisci un numero da 1 a 10: "))
    x+=1
    if number == randomNumber:
        print("Hai indovinato il numero!!!")
        break
    else:
        print("Riprova")

        