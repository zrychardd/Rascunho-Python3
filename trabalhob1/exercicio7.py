def soma_todos(*numeros):
    return sum(numeros)

def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

resultado = soma_todos(2, 3, 4, 5, 6)
print(f"A soma de todos os números é: {resultado}")

exibir_dados(nome="Wesley", idade=30, cidade="Sorocaba")

