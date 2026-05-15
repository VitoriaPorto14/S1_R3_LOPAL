# Exercício 7

num = int(input("Digite um número: "))
fat = 1

for x in range(1, num + 1):
    fat *= x

print(f"O fatorial de {num} é {fat}")


# fat é fatorial
# num é número
# lembrar que no range o segundo número define onde ele para, então num + 1 faz com que pare no número a frente. Ex: se quero o fatorial de 5 preciso fazer com que o python pare no 6 porque ele para e usa apenas o número anterior, então faço 1 (de onde começa) num + 1 (onde termina)