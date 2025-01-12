configurar interpretador do python vscode
importar bibliotecas e pacotes: json, requests, pandas, numpy, matplotlib, logging e Ipython. 


criar conteiner no docker
Dockerfile
FROM python:3.13.0
WORKDIR /testetec
COPY .  . 
RUN pip install requests
RUN pip install IPython
RUN pip install pandas 
RUN pip install numpy 
RUN pip install matplotlib
RUN pip install logging
CMD ["python", "Main.py"]


terminal vs code
docker build -t testetecnico-python .   
docker run -it testetecnico-python
