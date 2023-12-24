from PIL import Image


def rotation(px, x0, y0, t):
    if t == 1:
        return px
    else:
        mil = t // 2
        rotation(px, x0, y0, mil)
        rotation(px, x0 + mil, y0, mil)
        rotation(px, x0, y0 + mil, mil)
        rotation(px, x0 + mil, y0 + mil, mil)
        for x in range(x0, x0 + mil):
            for y in range(y0, y0 + mil):
                px[x, y + mil], px[x + mil, y + mil], px[x + mil, y], px[x, y] = px[x, y], px[x, y + mil], px[x + mil, y + mil], px[x + mil, y]

        return px


name = "maison"
imageDebut = Image.open(f"../{name}.png")

size = imageDebut.size[0]  # Récupération de la dimension de l'image (carrée ...)
print("Taille : ", size)
matrices = imageDebut.load()  # Récupération des pixels en codage rvb
print(matrices[0, 4])  # vérification d'un pixel rouge sur la premiere ligne

rotation(matrices, 0, 0, size)

imageDebut.save(f"../{name}_rot.png")
