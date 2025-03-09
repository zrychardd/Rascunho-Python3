import random

numero_secreto = random.randint(1, 2)

tentativa = int(input("escolha um numero de 1 a 10: "))

if tentativa == numero_secreto:
    print("parabéns você acertou o número secreto")

else:
    print(f"tente novamente o número era {numero_secreto}")
