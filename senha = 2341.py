senha_correta = "2341"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

    if senha != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Acesso permitido!")
