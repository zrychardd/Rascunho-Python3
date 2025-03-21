nota1= 8
nota2 = 6
nota3 = 9
nota4 = 1

lista_notas = [nota1,nota2,nota3,nota4]

if lista_notas:
    maior_nota= max(lista_notas)
    menor_nota = min(lista_notas)

print("A maior nota é {}".format(maior_nota))
print("A menor nota é {}".format(menor_nota))

print("A lista em ordem crescente é: {}".format(sorted(lista_notas)))
print(" A lista em ordem decrescente é: {}".format(sorted(lista_notas, reverse=True)))
