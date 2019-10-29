FROM ubuntu:18.04

RUN apt-get update -qq
RUN apt-get update
RUN apt-get install python
RUN apt-get install -qq tesseract-ocr libtesseract-dev libleptonica-dev python3 python3-distutils python3-pip
RUN pip3 install pytesseract


COPY . .

EXPOSE 8000

CMD python script.py
  

