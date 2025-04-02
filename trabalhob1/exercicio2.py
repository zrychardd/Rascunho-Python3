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

if numeros: 
    print("o maior numero digitado foi", max(numeros))
else:
    print("não foi digitado nenhum numero")
