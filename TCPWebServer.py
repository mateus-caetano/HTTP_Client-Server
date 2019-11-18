#import socket module
from socket import *
import sys # para terminar o programa
import threading #para trabalhar com threads
# from _thread import*

def server(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode() #codigo_inicio #codigo_fim
        filename = message.split()[1][1:]
        # print(filename)
        arc = open(filename).read()
        if (arc):
            response = ''.join(arc)

            #Envia um linha de cabecalho HTTP para o socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            connectionSocket.send("Content-Type: text/html\r\n".encode())

            #Envia o conteudo do arquivo solicitado ao cliente
            connectionSocket.send('\n'.encode())
            connectionSocket.send(response.encode())

            # fecha a conexao
            connectionSocket.close()
            
    except IOError:
        #Envia uma mensagem de resposta File not Found
        #codigo_inicio
        connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n'.encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        #codigo_fim
        #Fecha o socket cliente
        connectionSocket.close()


#Prepara o socket servidor
serverSocket = socket(AF_INET, SOCK_STREAM)
#codigo_inicio
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('localhost', 3000))
serverSocket.listen(1)
#codigo_fim

while True:
    #Estabelece a conexao
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #codigo_inicio #codigo_fim

    t = threading.Thread(target=server,args=(connectionSocket,))
    t.start()
    # while t.isAlive():
    #     continue
   

serverSocket.close()
sys.exit()  #Termina o programa depois de enviar os dados