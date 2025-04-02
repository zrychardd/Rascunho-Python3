
def gerador_impares(maximo):
    for numero in range(1, maximo + 1):
        if numero % 2 != 0:
            yield numero

valor_maximo = int(input("Digite o valor máximo: "))

print("Números ímpares gerados:")
for impar in gerador_impares(valor_maximo):
    print(impar)
