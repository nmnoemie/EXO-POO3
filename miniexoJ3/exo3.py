class Produit:
    def __init__(self,reference, nom,prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht=prix_ht
        self.stock     = stock
class ProduitElectronique(Produit):
    def __init__(self,reference, nom,prix_ht, stock,garantie_mois):
        super().__init__(reference, nom, prix_ht, stock)
        self.garantie_mois = garantie_mois
clavier = ProduitElectronique("KB-001", "Clavier", 79.99, 15, 24)
if isinstance(clavier,Produit):
    print("C'est un produit")

class Produit:
    def __init__(self,reference, nom,prix_ht, stock):
        self.reference = reference
        self.nom = nom
        self.prix_ht=prix_ht
        self.stock= stock

class ProduitAlimentaire(Produit):
    def __init__(self, reference, nom, prix_ht, stock,date_de_peremption):
        super().__init__(reference, nom, prix_ht, stock)
        self.date_de_peremption=date_de_peremption

    def appliquer_remise(produit):
        if isinstance(produit.prix_ht,Produit):
            return produit.prix_ht * 0.9
        return produit.prix_ht   
panier = [
    Produit("GEN-001", "Câble USB", 9.99, 50),
    ProduitAlimentaire("ALI-001", "Fromage", 12.99, 50, "2025-06-15")
]
for p in panier:
    if isinstance(p,(ProduitAlimentaire)):
       print( p.appliquer_remise())