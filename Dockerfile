FROM python:3

ADD server.py /

RUN pip install pystrich

CMD [ "python", "./server.py","0.0.0.0:9000" ]
