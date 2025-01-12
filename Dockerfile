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
