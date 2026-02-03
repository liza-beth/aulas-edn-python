# 1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
import random
import string
tamanho = int(input("digite o tamanho da senha"))
caractere = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choice(caractere) for _ in range(tamanho))
print(senha)

# 2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
import requests
def buscarUsuario():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados["results"][0]
        return usuario
    except requests.exceptions.RequestException:
        print("falha ao se conectar à API")

usuario = buscarUsuario()
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario["email"]
pais = usuario["location"]["country"]
print(f"Nome {nome}, email {email} e país {pais}")

# 3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
def acharCEP(cep:int):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        print(f"Estado {dados["uf"]}, Bairro {dados["bairro"]}, Logradouro {dados["logradouro"]}")
    except requests.exceptions.RequestException:
        print("erro")
c = input("digite o cep")
acharCEP(c)
# 4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

def consultar_moeda(moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        dados = response.json()
        chave = f"{moeda}BRL"

        if chave not in dados:
            print("Moeda não encontrada.")
            return

        cotacao = dados[chave]

        print("Cotação encontrada:")
        print("Valor atual:", cotacao["bid"])
        print("Máxima:", cotacao["high"])
        print("Mínima:", cotacao["low"])
        print("Última atualização:", cotacao["create_date"])

    except requests.exceptions.RequestException:
        print("Erro ao consultar a moeda.")

moeda = input("Digite a moeda (ex: USD, EUR): ").upper()
consultar_moeda(moeda)
