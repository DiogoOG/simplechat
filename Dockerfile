FROM python:3

RUN mkdir /simplechat
WORKDIR /simplechat
COPY server.py /simplechat

EXPOSE 9000

CMD [ "python", "./server.py","0.0.0.0:9000" ]
