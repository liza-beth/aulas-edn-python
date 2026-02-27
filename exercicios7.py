# 1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 
import csv

nome_arquivo = input("Digite o nome do arquivo CSV: ")

try:
    tempos = []

    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                tempos.append(float(linha["tempo_execucao"]))
            except (ValueError, KeyError):
                print("Linha ignorada por conter valor inválido.")

    if len(tempos) == 0:
        print("Nenhum valor válido encontrado.")
    else:
        media = sum(tempos) / len(tempos)
        maior = max(tempos)

        print(f"Média do tempo_execucao: {media:.2f}")
        print(f"Maior tempo_execucao: {maior:.2f}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)

# 2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 

nome_saida = input("Digite o nome do arquivo para salvar (ex: pessoas.csv): ")

pessoas = [
    {"nome": "Ana", "idade": 22, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Mariana", "idade": 27, "cidade": "Belo Horizonte"}
]

try:
    with open(nome_saida, mode="w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "idade", "cidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(pessoas)

    print("Arquivo salvo com sucesso.")

except Exception as e:
    print("Falha ao salvar o arquivo:", e)


# 3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.
nome_arquivo1 = input("Informe o nome do arquivo TXT: ")

try:
    with open(nome_arquivo1, "r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
            print(f"Linha {numero}: {linha.strip()}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print("Erro ao abrir o arquivo:", e)


# 4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
import json

nome_arquivo2 = input("Digite o nome do arquivo JSON: ")

dados = {
    "nome": "Fernanda",
    "idade": 25,
    "cidade": "Curitiba"
}

# Salvando
try:
    with open(nome_arquivo2, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Dados salvos com sucesso.")

except Exception as e:
    print("Erro ao salvar o arquivo:", e)

# Lendo
try:
    with open(nome_arquivo2, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("Dados lidos do arquivo:")
    for chave, valor in dados_lidos.items():
        print(f"{chave}: {valor}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)