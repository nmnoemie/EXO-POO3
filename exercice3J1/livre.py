class Livre:
    def __init__(self, titre, auteur, isbn, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nb_pages = nb_pages
        self.disponible = True  
        self.emprunteur = None  

    def afficher(self):
        statut = "Disponible" if self.disponible else f"Emprunté par {self.emprunteur}"
        print(f"Livre : {self.titre} | Auteur : {self.auteur} | Pages : {self.nb_pages} | État : {statut}")

    def emprunter(self, nom_emprunteur):
        if self.disponible:
            self.disponible = False
            self.emprunteur = nom_emprunteur
            return True
        else:
            print(f"Le livre '{self.titre}' est déjà pris.")
            return False

    def rendre(self):
        self.disponible = True
        self.emprunteur = None

    def temps_lecture_estime(self):
        return self.nb_pages