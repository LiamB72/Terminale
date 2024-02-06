def cryptage(message, clef):
    res = ''
    i = 0
    for letter in message:
        ordValue = ord(letter)
        ordClef = ord(clef[i])

        cryptedValue = ordValue ^ ordClef
        cryptedLetter = chr(cryptedValue)
        res += cryptedLetter

        if i < 4:
            i += 1
        if i >= 4:
            i = 0

    return res

crypto1=cryptage("Il fait super beau aujourd'hui", 'Test')

fichier = open("cryptage.txt", "w", encoding='utf8') # ouverture en mode write
fichier.write(crypto1)
fichier.close()

fichier = open("cryptage.txt", "r", encoding='utf8') # ouverture en mode read
cryptogramme=fichier.read()
fichier.close()

messageDecrypte=cryptage(cryptogramme, 'Test') # On décrypte !

fichier = open("decryptage.txt", "w", encoding='utf8')
fichier.write(messageDecrypte)
fichier.close()

