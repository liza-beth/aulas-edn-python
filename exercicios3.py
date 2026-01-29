# 1- Classificador de Idade
# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:
# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).
idade = int(input("Qual a sua idade? "))
faixa_etaria = ""
if idade > 0 and idade <=12:
    faixa_etaria = "criança"
elif idade > 12 and idade <=17:
    faixa_etaria = "adolescente"
elif idade > 17 and idade < 59:
    faixa_etaria = "adulto"
elif idade > 60:
    faixa_etaria = "idoso"
else:
    print("idade inválida")
print(faixa_etaria)

# 2- Calculadora de IMC
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

peso = float(input("Qual o seu peso? (em kg) "))
altura = float(input("Qual a sua altura? (em metros) "))
imc = peso/(altura*altura)
if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc < 25:
    classificacao = "peso normal"
elif imc < 30:
    classificacao = "sobrepeso"
else:
    classificacao = "obeso"
print(f"Seu imc é {imc:.2f}, classificado como {classificacao}")

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
def celsius_fahrenheit(t):
    return (t*9/5) + 32

def fahrenheit_celsius(t):
    return (t-32) * (9/5)

def celsius_kevin(t):
    return t + 273.15

def kevin_celsius(t):
    return t - 273.15
    
def fahrenheit_kevin(t):
    return fahrenheit_celsius(t) + celsius_fahrenheit(t)

def kevin_farenheit(t):
    return kevin_celsius(t) * 9/5 + 32

print("tipo de temperatura atual")
temperatura_tipo = input("digite C para Celsius, F para Fahrenheit, K para Kevin: ").upper().strip()
temperatura_atual = float(input("digite a temperatura atual: "))
temperatura_converter = input("digite para qual temperatura converter? digite C para Celsius, F para Fahrenheit, K para Kevin: ").upper().strip()
temperatura_convertida = 0
print(temperatura_converter)

if temperatura_tipo == "C":
    if temperatura_converter == "K":
        temperatura_convertida = celsius_kevin(temperatura_atual)
    elif temperatura_converter == "F":
        temperatura_convertida = celsius_fahrenheit(temperatura_atual)
    else:
        print("tipo para converter inválido")
elif temperatura_tipo == "K":
    if temperatura_converter == "C":
        temperatura_convertida == kevin_celsius(temperatura_atual)
    elif temperatura_converter == "F":
        temperatura_convertida == kevin_farenheit(temperatura_atual)
    else:
        print("tipo para converter inválido")
elif temperatura_tipo == "F":
    if temperatura_converter == "C":
        temperatura_convertida == fahrenheit_celsius(temperatura_atual)
    elif temperatura_converter == "K":
        temperatura_convertida == fahrenheit_kevin(temperatura_atual)
    else:
        print("tipo para converter inválido")
else:
    print("tipo atual de temperatura inválido")
print(temperatura_convertida)

# 4- Verificador de Ano Bissexto
# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
def ehBissexto(ano:int) -> bool:
    if ano%4 == 0 and not (ano%100 == 0 and not ano%400 == 0):
        return True
    else:
        return False

print(ehBissexto(2024))
print(ehBissexto(2020))
print(ehBissexto(2027))