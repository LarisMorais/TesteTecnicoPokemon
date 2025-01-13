FROM python:3.10-slim
WORKDIR /app
COPY .  . 
RUN pip install requests
RUN pip install IPython
RUN pip install pandas 
RUN pip install numpy 
RUN pip install matplotlib
CMD ["python", "app/Main.py"]
