import random


print("Sorteio de Viado!! Descubra se você é um viado ou não!!")

people_1 = input("Digite o nome da pessoa 1: ")
people_2 = input("Digite o nome da pessoa 2: ")
people_3 = input("Digite o nome da pessoa 3: ")

pessoas = [people_1, people_2, people_3]

random.shuffle(pessoas)

g = "é Viado"
ga = "Não é Viado"
gay = "Não é Viado"

lista = [g, ga, ga]

for i in range(len(pessoas)):
    print("o {}  {}".format(pessoas[i], lista[i]))