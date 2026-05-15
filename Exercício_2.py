# Exercício 2

import time

num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
num3 = float(input("Digite o número 3: "))

numeros = [num1, num2, num3]

print("Processando os dados...")
time.sleep(2)

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")