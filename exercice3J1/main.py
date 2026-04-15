from livre import Livre
from bibliotheque import Bibliotheque

if __name__ == "__main__":
    ma_biblio = Bibliotheque("Médiathèque de Paris")

    l1 = Livre("Le Petit Prince", "Saint-Exupéry", "978-2070408504", 96)
    l2 = Livre("L'Étranger", "Albert Camus", "978-2070360024", 184)
    l3 = Livre("Python Crash Course", "Eric Matthes", "978-1593279288", 544)

    ma_biblio.ajouter_livre(l1)
    ma_biblio.ajouter_livre(l2)
    ma_biblio.ajouter_livre(l3)

    print("--- Tentative d'emprunt ---")
    ma_biblio.emprunter_livre("L'Étranger", "Alice")
    l2.afficher() 

    ma_biblio.emprunter_livre("L'Étranger", "Bob") 

    ma_biblio.statistiques()
    temps = l3.temps_lecture_estime()
    print(f"\nTemps de lecture estimé pour {l3.titre} : {temps} minutes.")