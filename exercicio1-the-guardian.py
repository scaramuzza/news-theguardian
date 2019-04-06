
# Criar um programa que consuma a API do jornal The Guardian e mostre o título e o link 
# das notícias do dia: http://open-platform.theguardian.com

import requests
import json
import pandas as pd 

# 'as pd' é um apelido que você está colocando no panda >>> pd (apenas usou o comando 'as')
# pandas é uma biblioteca para exportal em CSV
# 'pd' é uma boa prática, apenas apelido. Poderia ser qualquer coisa ou até manter o nome 'pandas'

url = "https://content.guardianapis.com/search?api-key=4b0b60a3-f727-4a07-b933-54c80d8a4448" 
# Se cadastrou no site (The Guardian) para obter a chave de acesso e acessar os dados das moedas

print("")
print("Acessando base de dados...")
print("")

# Fazendo requisição ao servidor onde o site está hospedado. Códigos: OK = 200, ERRO = 404
# Victor Romário utilizou no cmd: pip install requests
# O que já é nativo do Python não precisa instalar (pip install X)
# O que não é nativo tem que instalar com o pip install Y
# 'requests' e 'json' são bibliotecas

response =  requests.get(url) # Response vai receber as requisições da variável URL
print(response)

# A resposta 200 significa que conseguiu acessar o site sem problemas
# URL com lista de códigos de resposta = https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status

if response.status_code == 200: # Final de IF, ELSE.... laços, tem que ter dois pontos (:) no final
    print("")
    print("Base de dados acessada com sucesso")
    print("Buscando informações no The Guardian...")
    print("")
    dados = response.json()
    
    # Desempacotar o JSON, que é um dicionário. A informação vem em formato JSON (pacote)

    print (dados["response"]["results"][5]["webTitle"])
    print (dados["response"]["results"][5]["webUrl"])

    # Entre aspas também poderia ser com aspa simples 'teste'
    # Vai pegar os dados que estão dentro da chave {response} e {results} do arquivo JSON
    # A resposta JSON com as notícioas na verdade é uma lista de dicionários (várias notícias)
    # Da para perceber claramente os subgrupos de abrir o arquivo da API com a chave no Firefox (abaixo)
    # https://content.guardianapis.com/search?api-key=4b0b60a3-f727-4a07-b933-54c80d8a4448
    # Neste caso ele vai acessar a reportagem 5 e dizer o título da 5
    # Se quiser tudo que está dentro da 'response' fazer:
    # print (dados["response"])
    
else:
    print("Site com Problemas! Não deu 200 ou Não foi possível acessar base de dados")
    print("")

# ================================================================================
# ===========================OUTRA FORMA DE FAZER=================================
# ================================================================================

print("")
print("")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>> Outra forma de fazer:")
print("")

if response.status_code == 200:
    print("")
    print("Base de dados acessada com sucesso")
    print("Buscando informações no The Guardian...")
    print("")
    dados = response.json()

    titulo = []
    link = []

    for posicao in dados ["response"]["results"]:
        print (posicao["webTitle"])
        print (posicao["webUrl"])

    # Essa função FOR vai permitir mostrar o Título e Url de todas as notícias trazidas pelo JSON
    # então, se tiver 10 notícias agora e daqui a pouco 300. Ele vai mostrar tudo toda a raiz importada
    # Observe que ele criou a variável 'posicao' já direto e dentro do FOR

        titulo.append(posicao["webTitle"])
        link.append(posicao["webUrl"])

        # A função 'append' adiciona itens da lista na última posição

    df = pd.DataFrame({"Titulo": titulo, "Link": link})
    df.to_csv("news.csv", index=False, sep=";", encoding="utf-8-sig")
    
    print("")
    print("Arquivo Exportado com Sucesso")
    print("")

    # 'pd' do Panda aí
    # Está chamando a biblioteca PANDA para exportar para o excel (CSV) o título e o link
    # Diz que vai criar o arquivo com nome de news.csv, tirar o INDEX, separar por ponto e vírgula
    # pois o excel só separa em coluna se vinher com ponto e vírgula
    # O 'encoding="utf-8-sig' permite ao Banda ter acesso a um conjunto de caracteres alfa numéricos
    # As variáveis titulo e link foram criadas fora do LAÇO para não ficar executando toda hora
    # ... essas variáveis estão na linha 73 e 74

else:
    print("Site com Problemas! Não deu 200 ou Não foi possível acessar base de dados")