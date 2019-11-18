import requests
import sys
import threading

def req(serverName, serverPort, arc):
    r = requests

    r = requests.get(url = 'http://' + serverName + ':' + str(serverPort) + '/' + arc)

    if(r.status_code == 404):
        print(r.status_code)
        print('NOT FOUND')
    else:
        print(r.text)


serverName = sys.argv[1]
serverPort = sys.argv[2]
arc = sys.argv[3]
req(serverName, serverPort, arc)

# essa parte foi feita para simular a capacidade do servidor em lidar com varias silicitacoes
# t1 = threading.Thread(target=req, args=(serverName, serverPort, arc))
# t2 = threading.Thread(target=req, args=(serverName, serverPort, 'in'))
# t3 = threading.Thread(target=req, args=(serverName, serverPort, 'page.html'))
# t1.start()
# t2.start()
# t3.start()
# while (t1.isAlive() or t2.isAlive() or t3.isAlive()):
#     continue
