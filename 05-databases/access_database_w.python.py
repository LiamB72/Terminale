import mysql.connector
from mysql.connector import FieldType

def connectBD():
    db = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='userlogin')
    return db

#effectue une requête et affiche les résultats
def selectRequete(request):
    print(request)
    db=connectBD()
    cur = db.cursor()
    cur.execute(request)
    enregistrements=cur.fetchall()
    #affiche le nom des champs
    for champs in cur.description:
        print("{0:30}".format(champs[0]),end='')
    print()
    #affiche les enregistrements
    for lignes in enregistrements:
        for valeurs in lignes:
            print("{0:30}".format(str(valeurs)),end='')
        print()
    cur.close()
    db.close()

def identifieUser(login,passwd):
    # recherche l'idUser du login et du mot de passe passé en paramètre
    request= "select idUser from user where login='{}' and passwd='{}';".format(login, passwd)
    print(request)
    db=connectBD()
    cur = db.cursor()
    cur.execute(request)
    enregistrements=cur.fetchall()
    if len(enregistrements)==1:
        print("accès autorisé, idUser",enregistrements[0][0])  #iduser en ligne 0, colonne 0
    else:
        print("mauvais login ou mot de passe")
    cur.close()
    db.close()

requete="select * from user;"
selectRequete(requete)
identifieUser('nsi','4560')

