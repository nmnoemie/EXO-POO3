from compte import CompteBancaire
if __name__=="__main__":
    compte1 = CompteBancaire("Alice",1000) 
    compte2 = CompteBancaire("Bob",500,200)

compte1.deposer(200)
compte1.retirer(500)
    
compte1.virement(compte2, 300)

compte2.appliquer_interets()

compte1.afficher_historique()
compte2.afficher_historique()
    