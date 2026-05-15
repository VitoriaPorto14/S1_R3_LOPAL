# Exercício 3

nome = input("Digite seu nome: ")

# len é o comando para a contagem de números na palavra, mais fácil
for escada in range(1, len(nome) + 1):
    print(nome[:escada])