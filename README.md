Projeto para consumo de Dados de API (POKE API)

1. Consumo da API 
2. Estruturação dos dados usando pandas
3. Transformação de Dados com categorização (pokemons fortes, médios e fracos)
4. Transformaçao de tipos com gráficos utilizando matplotlib
5. Analise estatística de média de ataque, defesa e HP por pokemon e classificação dos 5 com maior experiência
6. Relatório com pandas, gerando um arquivo csv com as analises estatísticas


Para executar é necessário: 
1. importar bibliotecas e pacotes: json, requests, pandas, numpy, matplotlib, Ipython. 
2. clonar repositorio do git
3. executar docker
4. executar comandos:
   01. docker build -t testetecnicopokemon-python .
   02. docker run -it testetecnicopokemon-python
   03. docker run --rm -v "$(pwd):/app" testetecnicopokemon-python



