class CompteBancaire:
    taux_interet=0.02
    def __init__(self, titulaire,solde,decouvert_autorise):
        self.titulaire=titulaire
        self.solde=solde
        self.decouvert_autorise=0
        self.historique=[]
        
    def deposer(montant,solde,self):
        solde=[]
        while montant>0:
            self.solde=solde+montant
    def retirer(montant,self,solde): 
        solde=[]    
        self_solde=solde-montant
        decouvert_autorisee=0
        if sel>=-decouvert_autorisee:
            return ("opération réussie",solde_final)
        else:
            return ("opération réfusée")
            
    def virement(autre_compte ,montant) : 
        
    def afficher_historique():
        
    def appliquer_interets():