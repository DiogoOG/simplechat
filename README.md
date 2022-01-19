# simple-chat

Grupo 5: Diogo Gouveia; Francisco Gonçalves; José Fabrício Silva

Uma simples aplicação de chat.
Esta aplicação segue uma arquitetura CLIENTE/SERVIDOR; um servidor disponibiliza-se a conexões de múltiplos clientes, recebendo as suas mensagens
e redirecionando-as para os restantes. Ambas as partes estão incluídas aqui, mas note-se que apenas server.py é destinado a correr num contentor.

Para utilizar, é apenas necessário correr o ficheiro server.py com os argumentos IP:PORTA (i.e. 'server.py x.x.x.x:x).
Depois, para aceder, correr o ficheiro client.py e inserir o mesmo par IP:PORTA. Será solicitado uma alcunha e a partir daí será possível enviar mensagens.

Para testar localmente:

> server.py 0.0.0.0:9000

> client.py

    - Insira o IP: localhost:9000
    - Nickname: André
   
A partir deste ponto o cliente envia mensagens que o servidor recebe e retransmite para todos os conetados.

## Github actions

Sempre que criarmos uma tag no projeto com a sintaxe v*.*.* é desploteado uma github action que faz o build da imagem e envia
para o docker hub.

