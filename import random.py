import random

numero_secreto = random.randint(1, 10)  
tentativa = int(input("Adivinhe o número de 1 a 10: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print(f"Errou! O número era {numero_secreto}.")
