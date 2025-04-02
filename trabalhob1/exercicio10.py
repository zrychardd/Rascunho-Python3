from functools import reduce
numeros = []
while True: 
    try:
        entrada=input("escreva os numeros inteiros:")
        if entrada.lower() == "a":
            break

        num=int(entrada)
        numeros.append(num)
    except ValueError:
        print ("escreva um numero, ou finalize com 'a' para sair")
    
print("os numeros digitados", numeros)

def multiplicar (x,y):
    return x*y

resultado = reduce(multiplicar, numeros)

print("o resultado é {}" .format(resultado))