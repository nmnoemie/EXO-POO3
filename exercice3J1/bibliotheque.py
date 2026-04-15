from livre import Livre

class Bibliotheque:
    nb_emprunts_total = 0

    def __init__(self, nom):
        self.nom = nom
        self.livres = []  

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def rechercher(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None

    def emprunter_livre(self, titre, emprunteur):
        livre = self.rechercher(titre)
        if livre:
            if livre.emprunter(emprunteur):
                Bibliotheque.nb_emprunts_total += 1
        else:
            print("Livre introuvable.")

    def statistiques(self):
        total = len(self.livres)
        if total == 0:
            print("La bibliothèque est vide.")
            return

        disponibles = len(self.livres_disponibles())
        pourcentage_dispo = (disponibles / total) * 100
        
        print(f"\n--- Stats de la bibliothèque {self.nom} ---")
        print(f"Nombre total de livres : {total}")
        print(f"Livres disponibles : {pourcentage_dispo:.1f}%")
        print(f"Total historique des emprunts : {Bibliotheque.nb_emprunts_total}")

    def livres_disponibles(self):
        return [l for l in self.livres if l.disponible]