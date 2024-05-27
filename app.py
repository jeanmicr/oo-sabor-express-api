import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })
else:
    print(f'Erro: {response.status_code}')
    
for nome_restaurante, dados in dados_restaurante.items(): # items() método de dicionário para retornar uma visão dos objetos contido no dicionario.
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo,'w') as arquivo_restaurante: #open - abre um arquivo em modo de escrita com o nome_arquivo referente ao restaurante. | with - garanta que o arquivo seja fechado adequadamente.
        json.dump(dados, arquivo_restaurante, indent=4)

    
    
