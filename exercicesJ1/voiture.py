class Voiture:
    nb_produits =0
    
    def __init__(self,marque,modele,annee,kilometrage,prix_neuf):
        self.marque= marque
        self.modele= modele
        self.annee= annee
        self.kilometrage= kilometrage
        self.prix_neuf= prix_neuf
        Voiture.nb_produits +=1
        
    def afficher(self):
         print(f"{self.marque }| {self.modele} |{self.annee} | {self.kilometrage} |{self.prix_neuf}")
         
    def est_recente(self):
         if self.annee>=2020:
            return True
         else:
             return None

    def parcourir_distance(self, distance):
        self.kilometrage +=1
    
    def estimer_valeur(self):
        if self.prix_neuf>=500:
           return round((self.prix_neuf-0.05)/self.parcourir_distance)
        else:
            return None