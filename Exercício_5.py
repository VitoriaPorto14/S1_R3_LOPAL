# Exercício 5

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Erro! O nome deve ter mais que 3 caracteres.")
    nome = input("Digite seu nome novamente. Deve conter no mínimo 4 quatro caracteres.")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida.")
    idade = int(input("Digite sua idade novamente. A idade deve ser entre 1 a 150"))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("Erro! O salário deve ser maior que zero: ")
    salario = float(input("Digite seu salário novamente. Você não é desempregado! "))

sexo = input("Digite seu sexo: ")
while sexo != 'f' and sexo != 'm':
    print("Erro! Sexo inválido.")
    sexo = input("Digite seu sexo novamente (f ou m). ")

estado = input("Digite seu estado civil (s, c, v, d): ")
while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
    print("Erro! Estado civil inválido.")
    estado = input("Digite novamente seu estado civil (s, c, v, d). ")

print("\n" + "="*30)
print("      DADOS DO CADASTRO")
print("="*30)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado}")
print("="*30)
print("Cadastro realizado com sucesso!")