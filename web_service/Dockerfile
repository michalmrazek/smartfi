FROM python:3.7-buster

RUN pip install pandas 
RUN pip install CherryPy 
RUN pip install pyOpenSSL
RUN pip install xmltodict


COPY web_service .

EXPOSE 8000

CMD python ws.py
  

