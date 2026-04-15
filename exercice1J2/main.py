from comptesecurise import CompteBancaire
if __name__=="__main__":
    c = CompteBancaire("Alice", 500, 200)
    c.deposer(100)          # Dépôt de 100. Nouveau solde : 600
c.retirer(800)          # Retrait200
c.retirer(50)          

print(c.solde)           # -200
print(c.est_a_decouvert)  # True
print(c.nb_operations)   # 2 (seules les opérations réussies comptent)

c.afficher_historique()

c.titulaire = ""         
c.deposer(True)       
    