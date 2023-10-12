import socket,sys

HOST="172.18.49.131" #adresse du serveur à modifier avant exécution
PORT=23

mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    print("Tentative de connexion avec un serveur")
    mySocket.connect((HOST,PORT))
except socket.error:
    print("la connexion a échoué")
    sys.exit()
print("connexion établie avec le serveur")
mySocket.send("hello".encode("Utf8"))

cnx=True
while cnx==True:
    msgServeur = mySocket.recv(1024) #attente des données du serveur
    print("message de retour>", msgServeur)
    if len(msgServeur)>0:
        cnx=False
print("Connexion interrompue.")
mySocket.close()
