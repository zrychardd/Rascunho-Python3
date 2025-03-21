nome = input('Digite seu nome:')
idade = int(input('Me diga a sua idade:'))

if idade < 16:
    print(f'{nome}, você ainda não pode votar! :(')
else:
    print(f'{nome}, você esta apto a votar! :)')
