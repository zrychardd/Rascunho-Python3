import random

numero_secreto = random.randint(1, 30)
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Advinhe o número secreto: "))

    if tentativa < numero_secreto:
        print("tente um número maior!")

    elif tentativa > numero_secreto:
        print("tente um número menor!")

if tentativa == numero_secreto:
    print("Parabéns, você acertou o número secreto!")
