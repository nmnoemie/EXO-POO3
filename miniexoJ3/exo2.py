class Employe:
    def __init__(self,nom,salaire_base):
        self.nom=nom
        self.salaire_base=salaire_base
    def afficher(self):
     print (f"{self.nom},{self.salaire_base}")
    
    def calculer_prime(self):
        return 0
class Commercial(Employe):
    def __init__(self,nom,salaire_base,prime):
        super().__init__(nom,salaire_base)
        self.prime=prime
    def calculer_prime(self):
        return (self.salaire_base*0.15)
    
class Technicien(Employe):
    def __init__(self, nom, salaire_base,prime):
        super().__init__(nom, salaire_base)
        self.prime=prime
    def calculer_prime(self):
        return ((self.salaire_base*0.10)+200)
    
equipe=[Employe("Marc",2000),
        Commercial("Sophie",2000,2500),
        Technicien("Lucas",2000,2200)]
for i in equipe:
    print(f"{i.nom}/ {i.calculer_prime()} de prime")
    
total=sum(i.calculer_prime() for i in equipe)
print(f"Total des primes:{total:}")
    
