def saluer(nom):
    return f"Hello, {nom}!"

if __name__ == "__main__":
    nom_utilisateur = input("Entrez votre nom : ")
    print(saluer(nom_utilisateur))