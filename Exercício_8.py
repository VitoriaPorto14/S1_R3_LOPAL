# Exercício 8

L = [5, 7, 2, 9, 4, 1, 3]
print("Dada a lista", L, "temos as seguintes informações: ")

# A
tamanho = len(L)
print("A) Tamanho:", tamanho)

# B
maior = L[0]
for numero in L:
    if numero > maior:
        maior = numero

print("B) Maior valor encontrado:", maior)

# C
menor = L[0]
for numero in L:
    if numero < menor:
        menor = numero

print("C) Menor valor encontrado:", menor)

# D
soma = 0
for numero in L:
    soma = soma + numero
print("D) Soma:", soma)

# E
L.sort()
print("E) Em ordem crescente: ", L)

# F
L.sort(reverse=True)
print("E) Em ordem decrescente: ", L)