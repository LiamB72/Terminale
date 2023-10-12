import socket,sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crée une socket

try:
    print("Tentative de mise en route du serveur")
    s.bind(('', 23))
except s.error:
    print("la connexion a échoué")
    sys.exit()
print("Serveur en attente de connexion")
s.listen(5) #ecoute le port 23

connexion, adresse = s.accept() #le serveur accepte la connexion entrante sur le port 23
print('Connection du client',adresse)
connexion.send('Bonjour'.encode("Utf8"))
print(connexion)

requete = connexion.recv(1024).decode('ascii') #récupére la requete client
print('Requete du client = ',requete)
connexion.send('bien recu\n\r'.encode("Utf8"))
connexion.close()
s.close()
