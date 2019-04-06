

# ================================================================================
# ===========================OUTRA FORMA DE FAZER 2===============================
# ================================================================================

print("")
print("")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>> Outra forma de fazer 2:")
print("")

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

    titulo = []
    link = []

    for posicao in dados ["response"]["results"]:
        print (posicao["webTitle"])
        print (posicao["webUrl"])

        titulo.append(posicao["webTitle"])
        link.append(posicao["webUrl"])
        
    exportar_csv(titulo, link, "noticias")

def main():

    # Vamos criar uma FUNÇÃO. É uma boa prática para organizar o código
    # Chama-se main, mas poderia ser qualquer nome para deixar um código grande organizado
    # Cada MAIN é um mundo paralelo, cada variável pertence a cada mundo paralelo

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
        
        buscar_noticias(dados)
           
    else:
        print("Site com Problemas! Não deu 200 ou Não foi possível acessar base de dados")
    



# Essa espaço grande aqui no final também é uma boa prática

if __name__ == "__main__": # Parte final do DEF
    main()

    # O Python gera o __main__ e salva na variável interna __name__
    # ou seja, a variável __NAME__ é padrão interno do Python (programação dentro da programação)
    # e o nome dado a essa variável (__MAIN__) também é padrão
    # Variável interna do Python se chama NAME
    # Se name existir e for igual igual a main, execute main()
    # Observe que o código não está na ordem, mas ele vai executar começando pelo DEF MAIN