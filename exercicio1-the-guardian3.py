
import requests
import json
import pandas as pd 

def exportar_csv(titulo, link, nome):

    df = pd.DataFrame({"Titulo": titulo, "Link": link})
    df.to_csv("%s.csv" % nome, index=False, sep=";", encoding="utf-8-sig")
    
    print("")
    print("Arquivo Exportado com Sucesso")
    print("")

def buscar_noticias(dados):
    titulo=[]
    link=[]
    for posicao in dados ["response"]["results"]:
        titulo.append(posicao["webTitle"])
        link.append(posicao["webUrl"])
    if len(titulo) == 0:
        print("Não há nenhuma postagem nessa área")
    else:
        exportar_csv(titulo, link, "noticias")

def buscar_sports(dados):
    titulo=[]
    link=[]
    for posicao in dados ["response"]["results"]:
        if posicao ["pillarName"] == "Sport":
            titulo.append(posicao["webTitle"])
            link.append(posicao["webUrl"])
    if len(titulo) == 0:
        print("Não há nenhuma postagem nessa área")
    else:
        exportar_csv(titulo, link, "sports")

def buscar_news(dados):
    titulo=[]
    link=[]
    for posicao in dados ["response"]["results"]:
        if posicao ["pillarName"] == "News":
            titulo.append(posicao["webTitle"])
            link.append(posicao["webUrl"])
    if len(titulo) == 0:
        print("Não há nenhuma postagem nessa área")
    else:
        exportar_csv(titulo, link, "news")

def buscar_arts(dados):
    titulo=[]
    link=[]
    for posicao in dados ["response"]["results"]:
        if posicao ["pillarName"] == "Arts":
            titulo.append(posicao["webTitle"])
            link.append(posicao["webUrl"])
    if len(titulo) == 0:
        print("Não há nenhuma postagem nessa área")
    else:
        exportar_csv(titulo, link, "arts")

def main():

    url = "https://content.guardianapis.com/search?api-key=4b0b60a3-f727-4a07-b933-54c80d8a4448" 

    print("")
    print("Acessando base de dados...")
    print("")

    response =  requests.get(url)
    print(response)

    if response.status_code == 200:
        print("")
        print("Base de dados acessada com sucesso")
        print("Buscando informações no The Guardian...")
        print("")
        dados = response.json()
        
        escolha = 4
        while escolha != 0:
            print("1 - Esportes")
            print("2 - Notícias")
            print("3 - Artes")
            print("4 - Todas")
            print("0 - para sair")
            try:
                escolha = int(input("Digite o número da notícia que você quer baixar: "))
            except:
                print("Por favor, digite apenas números")
            if escolha > 4:
                print("Por favor, digite apenas números entre 0 e 4")
            elif escolha == 1:
                buscar_sports(dados)
            elif escolha == 2:
                buscar_news(dados)
            elif escolha == 3:
                buscar_arts(dados)
            elif escolha == 4:
                buscar_noticias(dados)
            elif escolha == 0:
                print("Obrigado por utilizar o programa")
    
    else:
        print("Site com Problemas! Não deu 200 ou Não foi possível acessar base de dados")
    




if __name__ == "__main__":
    main()