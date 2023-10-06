

def reactionDistance(v):

    if v != 0:
        react = v / 3.6
    else:
        return 0
    return react

def freinageDistance(v,weather):

    if vitesse != 0:
        if weather == "rainy":
             freinge = ((vitesse ** 2)/200) * 2
        freinge = (vitesse ** 2)/200
    else:
        return 0
    return freinge

vitesse = int(input("Speed : "))
weather = input("Rainy, Clear, Thunderstorm, Hot, ... : ")
weather = weather.lower()

react, freinage = reactionDistance(vitesse), freinageDistance(vitesse, weather)

print(f"La distance d’arrêt du véhicule est de {round(react+freinage)} metres")



