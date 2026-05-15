# Exercício 4

n = int(input("Digite a quantidades de termos: "))

a = 1
b = 1

for i in range(n):
    print(a, end=" ")

    proximo = a + b
    a = b
    b = proximo