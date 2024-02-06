def conversionNote(userNote):
    if userNote >= 80:
        return 'A'
    elif userNote < 80 and userNote >= 60:
        return 'B'
    elif userNote < 60 and userNote >= 50:
        return 'C'
    elif userNote < 50 and userNote >= 40:
        return 'D'
    else:
        return 'E'

#def conversionNote(userNote):
#    return 'A' if userNote >= 80 else ('B' if userNote < 80 and userNote >= 60 else ('C' if userNote < 60 and userNote >= 50 else ('D' if userNote < 50 and userNote >= 40 else 'E')))

print(conversionNote(73))