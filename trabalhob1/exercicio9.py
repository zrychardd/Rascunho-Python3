alunos_notas = {
    "Alice": 1,
    "Bob": 8,
    "Carlos": 9,
    "Diana": 9
}

if alunos_notas:

    notas = list(alunos_notas.values())
    

    maior_nota = max(notas)
    menor_nota = min(notas)

    print("A maior nota é {}".format(maior_nota))
    print("A menor nota é {}".format(menor_nota))


    alunos_crescentes = sorted(alunos_notas.items(), key=lambda x: x[1])
    print("Lista de alunos em ordem crescente pelas notas:")
    for aluno, nota in alunos_crescentes:
        print("{}: {}".format(aluno, nota))

    alunos_decrescentes = sorted(alunos_notas.items(), key=lambda x: x[1], reverse=True)
    print("Lista de alunos em ordem decrescente pelas notas:")
    for aluno, nota in alunos_decrescentes:
        print("{}: {}".format(aluno, nota))