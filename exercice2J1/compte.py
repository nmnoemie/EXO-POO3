class CompteBancaire:
    taux_interet = 0.02  

    def __init__(self, titulaire, solde, decouvert_autorise=0):
        self.titulaire = titulaire
        self.solde = solde
        self.decouvert_autorise = decouvert_autorise
        self.historique = []

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            self.historique.append(f"Dépôt d'une somme de {montant}€")
            print(f"{montant}€ déposés avec succès.")

    def retirer(self, montant):
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            self.historique.append(f"Retrait d'une somme de {montant}€")
            return "Opération réussie"
        else:
            print("Opération refusée : solde insuffisant.")
            return "Opération refusée"

    def virement(self, autre_compte, montant):
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            autre_compte.deposer(montant)
            self.historique.append(f"Virement de {montant}€ vers {autre_compte.titulaire}")
        else:
            print("Virement impossible.")

    def appliquer_interets(self):
        if self.solde > 0:
            interets = self.solde * CompteBancaire.taux_interet
            self.solde += interets
            self.historique.append(f"Intérêts ajoutés : {interets}€")

    def afficher_historique(self):
        print(f"Historique de {self.titulaire}")
        for op in self.historique:
            print(f"- {op}")
        print(f"Solde actuel : {self.solde}€")