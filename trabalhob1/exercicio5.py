import random

numero_secreto = random.randint(0,100)
tentativa= 0

while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o numero secreto: "))
    if tentativa < numero_secreto:
        print("Tente um numero maior")

    elif tentativa > numero_secreto:
        print("Tente um numero menor")
if tentativa == numero_secreto:
    print("Parabens, voce acertou o numero secreto!")