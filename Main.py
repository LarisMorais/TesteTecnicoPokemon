#CONSUMO DE DADOS, ESTRUTURAÇÃO COM PANDAS E CATEGORIZAÇÃO

import json 
import requests
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO,filename="execucao.log",format="%(asctime)s - %(levelname)s - %(message)s") #configurações do logging
base_url = "https://pokeapi.co/api/v2"

def consumo_dados(): #Função para requisitar informações na API, retornar erro com logging
    logging.info(f"Consumindo dados POKEAPI...")
    r = requests.get(f"{base_url}//pokemon?limit=100&offset=0")
    if r.status_code == 200: #status da requisão 200(sucesso)
        logging.info("Dados carregados")
        return r.json()["results"]
    else:
        logging.error(f"Erro para carregar dados")
        return []

pokemon_list = consumo_dados()
detailed_pokemon_list = [] #lista de pokemons importados do json

for pokemon in pokemon_list:
    pokemon_info = requests.get(pokemon["url"]).json()

    types = []
    for type in pokemon_info["types"]:
        types.append(type["type"]["name"].capitalize())
 
    data = {
        "id": pokemon_info["id"],
        "name": pokemon_info["name"].capitalize(),
        "base_experience": pokemon_info["base_experience"],
        "types": types,
        "hp": pokemon_info ["stats"][0]["base_stat"],
        "attack": pokemon_info["stats"][1]["base_stat"],
        "defense": pokemon_info["stats"][2]["base_stat"],
    }
    detailed_pokemon_list.append(data)

def info_categoria(base_experience): #função para categorização dos pokemons, classificando entre fraco, medio e forte
   if base_experience < 50:
         return 'fraco'
   if base_experience >= 50 and base_experience <= 100:
        return 'medio'
   else:
        return 'forte'    
    
pokemons_df = pd.DataFrame(detailed_pokemon_list)

pokemons_df.columns = ["ID", "Nome", "Experiencia Base", "Tipos", "HP", "Ataque", "Defesa"] #renomeando colunas do dataframe
pokemons_df["Categoria"]= pokemons_df["Experiencia Base"].apply(info_categoria) #adicionando nova coluna com a categorização dos pokemons
pd.set_option('display.max_rows', None) #visualizando todos os dados do dataframe do pd
pokemons_df1 = pokemons_df.fillna(value=0) #caso algum dado esteja vazio irá retornar 0 no lugar

#Transformações de Tipos: contagem por tipo

pokemons_dt_tp = pokemons_df1.explode("Tipos") #filtrando apenas a coluna tipos do dataframe de pokemons
pokemons_dt_tp2 = pokemons_dt_tp["Tipos"].value_counts().reset_index() #fazendo a contagem de pokemons por tipos
pokemons_dt_tp2.columns = ["Tipos", "Qte"] #nomeando as colunas
pokemons_dt_tp2.sort_values(["Qte"], ascending=[True], inplace=True) #ordenando em ordem crescente
pokemons_df_tipos = pd.DataFrame(pokemons_dt_tp2)

#Transformações de Tipos: gráfico de barras com matplotlib mostrando a distribuição de Pokémon por tipo.
#dando valores aos eixos do grafico
y = (pokemons_dt_tp2["Qte"])
x = (pokemons_dt_tp2["Tipos"])
#caracteristicas do grafico, como tipo, tamanho, cor
plt.figure(figsize=(16,10))
plt.bar(x, y, edgecolor="white")
#personalizando grafico
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Pokémon')
plt.title('Distribuição de Pokémon por tipo')
plt.xticks(rotation=90)
plt.show()

#Análise Estatística: A média de ataque, defesa e HP por tipo de Pokémon.
pokemons_dt_tp = pokemons_df1.explode("Tipos") #pegar novamente os tipos separados
def calcmedia(x):  #funcao calculo media
    media = x.mean()
    return media

Media_hp = calcmedia(pokemons_dt_tp.groupby('Tipos')['HP'])  #calculo da média do hp
Media_Ataque = calcmedia(pokemons_dt_tp.groupby('Tipos')['Ataque'])  #calculo média do ataque
Media_Defesa = calcmedia(pokemons_dt_tp.groupby('Tipos')['Defesa']) #calculo media defesa
df_medias = pd.concat([Media_hp.rename('Média HP'),Media_Ataque.rename('Média Ataque'), Media_Defesa.rename('Média Defesa')], axis=1).round(1)  #concatenando todos os df

#Análise Estatística:Os 5 Pokémon com maior experiência base
pokemons_df_base = pokemons_df1.sort_values(["Experiencia Base"], ascending=[False]).head(5) #os 5 maiores resultados por experiencia base

#Relatorio consolidado
df_medias.to_csv('MediasPokemonPorTipo.csv',sep=';')
pokemons_df_base.to_csv('5MaioresExperienciabase.csv',sep=';')