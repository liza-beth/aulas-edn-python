# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada
def calcular_gorjeta(valor_conta:float, porcentagem_gorjeta:float) -> float:
    return valor_conta*(porcentagem_gorjeta/100)
valor_conta = float(input("Qual o valor da conta? "))
porcentagem = float(input("Qual a porcentagem da gorjeta (em %)? "))
print(f"O valor da gorjeta é R${calcular_gorjeta(valor_conta, porcentagem):.2f}")

# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
def ehPalindromo(texto:str) -> bool:
    texto = texto.strip().replace(" ", "")
    if texto == texto[::-1]:
        return True
    return False
texto = input("Digite: ")
if (ehPalindromo(texto)):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

from datetime import date, datetime
def calcular_desconto(valor, porcentagem_desconto) -> float:
    return round(valor*(porcentagem_desconto/100),2)
valor = float(input("Qual o preço do produto? "))
p_desconto = float(input("Qual a porcentagem de desconto? (em %)"))
print(f"O {valor} com {p_desconto}% de desconto é igual a {calcular_desconto(valor, p_desconto)}")

# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
def calcular_dias_vividos(data:date) -> int:
    data_atual = date.today()
    return (data_atual - data).days 

data = input("Data de nascimento: (formato DD/MM/AAAA) ")
data = datetime.strptime(data, '%d/%m/%Y').date()
print(f"Você viveu {calcular_dias_vividos(data)} dias")