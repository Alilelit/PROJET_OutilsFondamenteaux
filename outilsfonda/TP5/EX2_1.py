import unicodedata

def lettre_vers_nombre(c):
    return ord(c) - ord("A")


def nombre_vers_lettre(n):
    return chr(n + ord("A"))


def nettoyer(texte):
    sans_accent = unicodedata.normalize("NFD", texte)
    sans_accent = "".join(
        c for c in sans_accent
        if unicodedata.category(c) != "Mn"
    )
    return "".join(
        c for c in sans_accent.upper()
        if "A" <= c <= "Z"
    )


def chiffrer(texte, a, b):
    resultat = []
    for c in nettoyer(texte):
        x = lettre_vers_nombre(c)
        resultat.append(
            nombre_vers_lettre((a * x + b) % 26)
        )
    return "".join(resultat)


message = "ATTAQUEALAUBE"
print(chiffrer(message, 5, 8))
print(chiffrer(message, 1, 3))