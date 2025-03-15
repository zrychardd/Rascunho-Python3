numero =int(input("Digite o numero para saber a Tabuada : "))

print (f"tabuada de {numero}")
for i in range (1,11):
    resultado = numero * i
    print ("{} X {} = {}".format(numero,i,resultado))