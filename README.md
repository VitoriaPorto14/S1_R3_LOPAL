# Descrição dos Exercícios

## Exercício 1

- **O que faz:** Percorre os números de 0 a 100 e identifica se cada um deles é **par** ou **ímpar**, exibindo o resultado na tela.

## Exercício 2

- **O que faz:** Pede ao usuário para digitar três números e os armazena em uma lista. O programa simula um tempo de processamento de 2 segundos e, em seguida, varre a lista para encontrar e exibir qual é o **maior** e qual é o **menor** número digitado.

### Exercício 3

- **O que faz:** Solicita o nome do usuário e o imprime em formato de **"escada"** ou pirâmide crescente. Ele começa mostrando apenas a primeira letra, depois as duas primeiras, as três primeiras, e assim por diante, até mostrar o nome completo.

## Exercício 4

- **O que faz:** Gera e exibe a **Sequência de Fibonacci** até o número de termos ($n$) que o usuário escolher. A sequência começa com 1 e 1, e cada termo seguinte é a soma dos dois anteriores (1, 1, 2, 3, 5, 8...).

## Exercício 5

- **O que faz:** Um sistema de **validação de cadastro**. Ele solicita o nome (mínimo 4 caracteres), idade (entre 0 e 150), salário (maior que zero), sexo ('f' ou 'm') e estado civil ('s', 'c', 'v' ou 'd'). Se o usuário digitar algo incorreto, o programa entra em um loop e exige que o dado seja digitado novamente de forma correta. No final, exibe o comprovante do cadastro formatado.

## Exercício 6

- **O que faz:** Verifica se um número inteiro digitado pelo usuário é um **número primo** (ou seja, se ele é divisível apenas por 1 e por ele mesmo). O código testa divisões do número por todos os valores menores que ele.

## Exercício 7

- **O que faz:** Calcula o **fatorial** de um número inteiro digitado pelo usuário. O fatorial é a multiplicação desse número por todos os seus antecessores inteiros positivos (por exemplo, $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$).

## Exercício 8

- **O que faz:** Realiza várias operações sobre uma lista de números pré-definida `L = [5, 7, 2, 9, 4, 1, 3]`:
- **A)** Descobre o tamanho (quantidade de elementos).
- **B)** Encontra o maior valor.
- **C)** Encontra o menor valor.
- **D)** Calcula a soma de todos os valores.
- **E)** Ordena a lista em ordem crescente.
- **F)** Ordena a lista em ordem decrescente (há um pequeno erro de digitação no `print` do código, que repetiu a letra "E").



## Exercício 9

- **O que faz:** Cria e exibe um **dicionário** chamado `lanchonete`, onde os nomes dos produtos (chaves) estão associados aos seus respectivos preços (valores).

## Exercício 10

- **O que faz:** Simula um sistema de **verificação de senha**. O programa fica preso em um loop pedindo a senha. Se o usuário errar, aparece "Senha incorreta! Digite novamente". Se acertar a senha gravada (`"676767"`), exibe "Acesso autorizado!" e encerra o programa.

## Exercício 11

- **O que faz:** Cria uma **tabuada** automatizada. O usuário digita um número de 1 a 10. Se estiver dentro do intervalo, o programa calcula e mostra a tabuada de 0 a 10 desse número. Caso contrário, exibe uma mensagem de erro.

---

# Explicação dos Comandos Utilizados

Abaixo estão explicados os principais comandos e estruturas que dão vida a esses códigos:

## Estruturas de Repetição (Loops)

- **`for i in range(...)`**: Cria um laço de repetição que executa o bloco de código por um número determinado de vezes. O `range(101)`, por exemplo, vai de 0 até 100.
- **`while:`**: Cria uma repetição que continuará executando **enquanto** a condição for verdadeira. É excelente para validações (como no Exercício 5, onde continua pedindo o dado se ele estiver incorreto).
- **`while True:`**: Cria um loop infinito de propósito. Ele só será interrompido se encontrar o comando `break` por dentro.
- **`break`**: Interrompe e sai imediatamente de dentro de um laço `for` ou `while`.

## Estruturas Condicionais

- **`if` / `elif` / `else`**: Estruturas de decisão. O `if` testa uma condição inicial; o `elif` (abreviação de *else if*) testa uma nova condição caso a primeira seja falsa; e o `else` é o caminho padrão executado se nenhuma das condições anteriores for atendida.

## Entrada, Saída e Manipulação de Dados

- **`input("...")`**: Exibe uma mensagem na tela e aguarda o usuário digitar algum dado. Por padrão, ele sempre lê o dado como texto (string).
- **`print(...)`**: Exibe informações, textos ou resultados de variáveis no terminal.
- **`f"Texto {variavel}"` (f-strings)**: Permite incluir variáveis diretamente dentro de um texto usando chaves `{}`, facilitando muito a formatação da mensagem.
- **`int(...)` e `float(...)`**: Convertem um dado para o tipo **Inteiro** (números sem vírgula) ou **Flutuante** (números reais, com casas decimais), respectivamente. São muito usados junto com o `input()`.

## Operadores Matemáticos e de Comparação

- **`%` (Módulo)**: Retorna o resto da divisão entre dois números. Muito usado para saber se um número é par (`numero % 2 == 0`).
- **`*=` / `+=`**: Operadores de atribuição compacta. `fat *= x` é o mesmo que `fat = fat * x`.
- **`==` / `!=`**: Operadores de comparação. `==` verifica se dois valores são iguais; `!=` verifica se são diferentes.
- **`and` / `or`**: Operadores lógicos. O `and` exige que **todas** as condições sejam verdadeiras; o `or` exige que **pelo menos uma** seja verdadeira.

## Funções Nativas de Strings e Listas

- **`len(...)`**: Retorna o tamanho/comprimento de um objeto. Se aplicado a um texto, conta as letras; se aplicado a uma lista, conta os elementos.
- **Fatiamento de Strings `nome[:escada]`**: Extrai uma parte (subfração) do texto, começando do início (índice 0) até a posição indicada pela variável `escada`.
- **`L.sort()`**: Método utilizado para ordenar os elementos de uma lista de forma definitiva. Se usado como `L.sort(reverse=True)`, ele ordena em ordem decrescente.

### Biblioteca de Tempo

* **`import time`**: Importa o módulo nativo do Python para lidar com funções de tempo.
* **`time.sleep(2)`**: Faz o programa pausar ("dormir") a execução pelo número de segundos indicado entre parênteses (neste caso, 2 segundos).
