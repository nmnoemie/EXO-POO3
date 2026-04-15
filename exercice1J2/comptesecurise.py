class CompteBancaire:
    taux_interet = 0.02  

    def __init__(self, titulaire,solde,deposer,retirer,decouvert_autorise=0):
        self._titulaire = titulaire
        self.deposer=deposer
        self.retirer=retirer
        self._decouvert_autorise = decouvert_autorise
        self._solde= solde
        self.historique = []
    @property
    def est_a_decouvert(self):
        if self._solde<0:
         return True
    def nb_operations(self):
        return self.historique
         
    @deposer.setter
    def deposer(self, montant):
        if isinstance(montant,bool):
            raise TypeError("Pas de booléen")
        if not isinstance(montant,int):
            raise TypeError("Doit etre un entier")
        if montant<0:
            raise ValueError("Le montant doit etre positif")
        else:
            self.solde += montant
        self.historique.append(f"Dépôt d'une somme de {montant}€")
        print(f"{montant}€ déposés avec succès.")
        
    @retirer.setter 
    def retirer(self, montant,solde,decouvert_autorise):
        if isinstance(montant, bool):
            raise TypeError("Pas de booléen")
        if not isinstance(montant, int):
            raise TypeError("Doit être un entier")
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            return True
        else:
            print("Opération refusée : solde insuffisant.")
            return False
    

    def virement(self, autre_compte, montant):
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            autre_compte.deposer(montant)
            self.historique.append(f"Virement de {montant}€ vers {autre_compte.titulaire}")
        else:
            print("Virement impossible.")

    def historique(self):
        print(f"Historique de {self.titulaire}")
        for op in self.historique:
            print(f"- {op}")
        print(f"Solde actuel : {self.solde}€")