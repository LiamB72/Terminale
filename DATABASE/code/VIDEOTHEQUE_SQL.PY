# https://www.w3schools.com/python/python_mysql_getstarted.asp
import mysql.connector
from mysql.connector import FieldType


def connectBD():
    db = mysql.connector.connect(user='root', password='',
                                 host='127.0.0.1',
                                 database='videotheque')
    return db


# effectue une requete et affiche les résulats
def selectRequete(requete):
    print(requete, "\n")
    db = connectBD()
    requestExecutor = db.cursor()
    requestExecutor.execute(requete)
    valuesList = requestExecutor.fetchall()
    for columnTitle in requestExecutor.description:
        print(f"{columnTitle[0]:35}", end="")
    print("\n")

    for rows in valuesList:
        for val in rows:
            print(f"{val:35}", end='')
        print()

    requestExecutor.close()
    db.close()


# effectue une insertion de données
def insertData(request):
    print(request)
    db = connectBD()
    cur = db.cursor()
    cur.execute(request)
    db.commit()
    print(cur.rowcount, "Enregistrement  inséré.")
    cur.close()
    db.close()


# demande le genre du film et retourne une chaine de caractère correspondant au genre
def choixGenre():
    print("Quel genre voulez-vous ?")
    print("1 : Science-fiction ")
    print("2 : Comedie")
    print("3 : Policier")
    print("4 : Aventure")
    numeroGenre = input("\nVotre choix de film : ")
    genreNB = 0
    genre = ""

    match numeroGenre:
        case "1":
            genreNB = 5
            genre = "Science-fiction"
        case "2":
            genreNB = 1
            genre = "Comedie"
        case "3":
            genreNB = 3
            genre = "Policier"
        case '4':
            genreNB = 7
            genre = "Aventure"
    return genreNB, genre

# fonction requete Affichage de tous les films par ordre décroissant de durée
def afficheFilmsDesc():
    request = "SELECT titre, genreFilm, duree FROM film NATURAL JOIN genre ORDER BY duree DESC;"
    selectRequete(request)


# fonction requete Affichage des les films par genre
def afficheFilmsGenre():
    genre = choixGenre()
    request = f"SELECT titre, genreFilm, duree FROM film NATURAL JOIN genre WHERE genreFilm='{genre[1]}' ORDER BY genreFilm DESC;"
    selectRequete(request)

# fonction requete Liste tous les films d’une durée supérieur à une valeur
def afficheFilmsDuree():
    valeur = input("\ndurée minimale du film : ")
    request = f"SELECT titre, genreFilm, duree FROM film NATURAL JOIN genre WHERE duree>={valeur};"
    selectRequete(request)


# fonction requete Comptabilise tous les films
def comptabiliseFilms():
    request = "SELECT titre, genreFilm, duree FROM film, genre WHERE film.idGenre=genre.idGenre"

    selectRequete(request)


# fonction d'insertion de film
def ajouterFilms():
    titre = input("Votre titre de film : ")
    duree = int(input("La duree du film : "))
    genre = choixGenre()
    request = f"INSERT INTO film(`idFilm`, `titre`, `duree`, `idGenre`) VALUES (NULL,'{str(titre)}','{str(duree)}','{str(genre[0])}');"
    insertData(request)


menu = '0'
while menu != 'q':
    print()
    print("------------------------------------------------------------")
    print("1 : Afficher tous les films par ordre décroissant de durée")
    print("2 : Afficher les films par genre")
    print("3 : Lister tous les films d’une durée supérieur à une valeur")
    print("4 : Comptabiliser tous les films")
    print("5 : Ajouter un film")
    print("q : Quitter")
    print("------------------------------------------------------------")
    print()
    menu = input("--> ")
    print("\n")
    match menu:
        case "1":
            afficheFilmsDesc()
        case "2":
            afficheFilmsGenre()
        case "3":
            afficheFilmsDuree()
        case "4":
            comptabiliseFilms()
        case "5":
            ajouterFilms()
