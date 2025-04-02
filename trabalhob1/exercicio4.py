numero =int(input("digite o numero para saber a tabuada : "))

print (f"tabuada de {numero}")

for i in range (0,11):

    resultado = numero * i

    print (f"{numero} x {i} = {resultado}")