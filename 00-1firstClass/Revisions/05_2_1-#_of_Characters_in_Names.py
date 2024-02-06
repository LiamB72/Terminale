noms = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien','Alexandre-Benoît', 'Louise']
a = 0
for name in noms:
    for characters in name:
        a += 1
    print(f"{name} has {a} characters")
    a = 0