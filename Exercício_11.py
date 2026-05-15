# Exercício 11

numero = int(input("Digite um número de 1 a 10 para ver a tabuada: "))

if 1 <= numero <= 10:
    print(f"Tabuada de {numero}:")

    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Esse número não vale! Por favor, digite novamente.")