# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
print("Para qual moeda você deseja converter? Digite E para Euro ou D para Dólar")
moeda = input().upper()
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15
valor_convertido = 0
if moeda == 'D':
    valor_convertido = valor_reais/taxa_dolar
elif moeda == 'E':
    valor_convertido = valor_reais/taxa_euro
else:
    print("Moeda inválida. Digite E para Eurou ou D para Dólar")
print(f'{valor_convertido:.2f}')

# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 0.20
valor_desconto = preco_original*porcentagem_desconto
print(f"A camiseta de {preco_original} está saindo pelo valor de {preco_original - valor_desconto}, um desconto de {valor_desconto} reais")

# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
notas = [7.5, 8.0, 6.5]
media = sum(notas) / 3
print(f"A média das notas {notas[0]}, {notas[1]} e {notas[2]} é {media:.2f}")

# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
distancia_percorrida = 300
combustivel = 25
print(f"O consumo médio da corrida de 300km foi {combustivel/distancia_percorrida:.2f}km/l, consumindo 25 litros ao todo")