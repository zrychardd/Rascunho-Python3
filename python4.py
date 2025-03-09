import random as rd

numero_secreto = rd.randint(1 , 100)

tentativa = int(input("Escolha um numero de 1 até 100: "))

if tentativa == numero_secreto:
    print("Você acertou o número secreto")


else:
    print("Você errou o número secreto")