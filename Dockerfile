FROM python:3-alpine

RUN mkdir /simplechat
RUN mkdir /simplechat/logs
WORKDIR /simplechat
COPY server.py /simplechat

EXPOSE 32000

CMD [ "python", "./server.py","0.0.0.0:32000" ]