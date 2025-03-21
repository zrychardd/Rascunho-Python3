
from functools import reduce


num1 = int(input("Escreva o primeiro numero: "))
num2 = int(input("Escreva o segundo numero: "))
num3 = int(input("Escreva o terceiro numero: "))
num4 = int(input("Escreva o quarto numero: "))
num5 = int(input("Escreva o quinto numero: "))

def multiplicar (x,y):
    return x * y


lista = [num1, num2, num3, num4, num5]

resultado = reduce(multiplicar, lista)


print(resultado)