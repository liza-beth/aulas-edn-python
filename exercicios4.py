# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
operacao = float(input("Qual a operação? Digite 1 para subtração, 2 para soma, 3 para multiplicação e 4 para divisão "))
num1 = float(input("Primeiro número "))
num2 = float(input("Segundo número "))
resultado = 0
if operacao == 1:
    resultado = num1 - num2
elif operacao == 2:
    resultado = num1 + num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    resultado = num1 / num2
else:
    print("operação inválida")
print(f"O resultado é {resultado:.2f}")

# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.
numero_alunos = int(input("Há quantos alunos na sala? "))
notas = []
for i in range(numero_alunos):
    print(f"digite a nota do aluno {i+1}")
    notas.append(int(input()))
media = sum(notas) / numero_alunos
print(f"A média é {media:.2f}")

# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.
def validar_senha(senha:str) -> bool:
    if len(senha) < 8:
        return False
    haNumero = False
    for letra in senha:
        if letra.isdigit():
            haNumero = True
    return haNumero

senha = input("Digite sua senha: ")
if (validar_senha(senha)):
    print("A senha é válida")
else:
    print("A senha é inválida")

# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
def numerosImpares(n:list[int]) -> int: 
    quantidade = 0
    for numero in n:
        if numero % 2 != 0:
            quantidade += 1
    return quantidade

quantidade_numeros = int(input("quantos números deseja inserir? "))
n = []
for i in range(quantidade_numeros):
    print(f"inserir número {i+1}")
    n.append(int(input()))
impares = numerosImpares(n)
print(f"Dentre os números digitados, {impares} são ímpares e {quantidade_numeros-impares} são pares")