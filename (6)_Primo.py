# Exercício 6

num = int(input("Digite um número: "))
primo = True

if num < 2:
    primo = False
else:
    for x in range(2, num):
        if num % x == 0:
            primo = False
            break

if primo:
    print(num, "é primo.")
else:
    print(num, "não é primo.")