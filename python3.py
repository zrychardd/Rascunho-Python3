Nota1 = float(input("Nota 1: "))
Nota2 = float(input("Nota 2: "))
Nota3 = float(input("Nota 3: "))

Média = (Nota1 + Nota2 + Nota3) / 3 

if Média >= 7:
    print("Parabéns você foi aprovado! Sua nota foi:", int(Média))
else: 
    print("Sua nota é menor que 6,Reprovado")