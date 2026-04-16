class Temperature:
    def __init__(self,valeur_celsius):
        self.valeur_celsius=valeur_celsius
    
@property
def valeur_celsius(self):
    return self._valeur_celsius

@valeur_celsius.setter
def valeur_celsius(self,valeur):
    if isinstance(valeur,bool):
        raise TypeError("La température ne peut pas etre un booléen")
    if not isinstance(valeur,(int,float)):
        raise TypeError("La température doit etre un nombre")
    if valeur < -273.15 or valeur > 1000000:
        raise ValueError(f"Température hors limites(-273.15 a 1000000):{valeur}")
    self._valeur_celsius =float(valeur)
@property
def fahrenheit(self):
    return (self._valeur_celsius*9/5)+32
@property
def kelvin(self):
    return self._valeur_celsius +273.15
@property
def etat(self):
    if self._valeur_celsius<=0:
        return "solide"
    elif self._valeur_celsius<100:
        return "liquide"
    else:
        return "gazeux"

@classmethod
def depuis_fahrenheit(cls,valeur_f):
    c_val=(valeur_f-32)*5/9
    return cls(c_val)
def est_compatible_avec(self,autre):
    if not isinstance(autre,Temperature):
        return False
    return self.etat == autre.etat
    
    
