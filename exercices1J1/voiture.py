class Voiture:
    nb_voitures = 0 
    
    def __init__(self, marque, modele, annee, kilometrage, prix_neuf):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.prix_neuf = prix_neuf
        Voiture.nb_voitures += 1
        
    def afficher(self):
        valeur = self.estimer_valeur()
        print(f"{self.marque} {self.modele} ({self.annee}) — {self.kilometrage} km — Valeur : {valeur}€")

def est_recente(self):
    return self.annee >= 2020
    
def parcourir(self, distance):
    self.kilometrage += distance
    
def estimer_valeur(self):
    valeur = self.prix_neuf - (self.kilometrage * 0.05)
    return float(max(valeur, 0))



