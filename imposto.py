def calcular_imposto(renda):
    if renda < 1614:
        return 0
    elif renda < 7000:
        return renda * 0.10
    elif renda < 10000:
        return renda * 0.23
    else:
        return renda * 0.30
    

User_Renda= float(input("Qual é a sua Renda? R$"))

imposto = calcular_imposto (User_Renda)

sobra = (User_Renda - imposto)

resultado = print("Você irá pagar R${:.2f} de imposto de acordo com seu salario de R${:.2f}".format(imposto,User_Renda))
