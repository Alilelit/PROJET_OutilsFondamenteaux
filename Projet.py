import itertools
import string
import time

def generer_caracteres():
    """Retourne l'ensemble des caractères possibles : lettres, chiffres, symboles."""
    lettres_minuscules = string.ascii_lowercase   # a-z
    lettres_majuscules = string.ascii_uppercase   # A-Z
    chiffres = string.digits                      # 0-9
    speciaux = string.punctuation                 # !@#$%^&*()_+-= etc.
    return lettres_minuscules + lettres_majuscules + chiffres + speciaux

def forcer_mot_de_passe(mot_de_passe_cible, longueur_max=8):
    """
    Essaie de retrouver le mot de passe par force brute,
    en testant toutes les combinaisons possibles, longueur par longueur.
    """
    caracteres = generer_caracteres()
    tentatives = 0
    debut = time.time()

    for longueur in range(1, longueur_max + 1):
        print(f"Essai des combinaisons de longueur {longueur}...")
        for combinaison in itertools.product(caracteres, repeat=longueur):
            tentatives += 1
            essai = ''.join(combinaison)

            if essai == mot_de_passe_cible:
                duree = time.time() - debut
                print(f"\nMot de passe trouvé : {essai}")
                print(f"Nombre de tentatives : {tentatives}")
                print(f"Temps écoulé : {duree:.4f} secondes")
                return essai

    print("Mot de passe non trouvé dans la limite de longueur fixée.")
    return None

def main():
    print("=== Simulation de force brute sur un mot de passe ===\n")
    mot_de_passe = input("Entrez le mot de passe à tester (il restera caché aux yeux du programme) : ")
    
    print("\nRecherche en cours...\n")
    forcer_mot_de_passe(mot_de_passe, longueur_max=len(mot_de_passe))

if __name__ == "__main__":
    main()²