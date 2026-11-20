def calculer_moyenne(notes):
    if not notes:
        raise ValueError("La liste des notes est vide")
    return sum(notes) / len(notes)


def afficher_resultat(nom, notes):
    moyenne = calculer_moyenne(notes)
    print("Étudiant :", nom)
    print("Moyenne :", moyenne)
    if moyenne >= 10:
        print("Résultat : Admis")
    else:
        print("Résultat : Non admis")


def main():
    notes = [14, 16, 12, 18]
    afficher_resultat("Ahmed", notes)


if __name__ == "__main__":
    main()
