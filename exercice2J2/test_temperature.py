import csv

def traiter_donnees_capteurs(fichier):
    with open(fichier, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nom = row['capteur']
            val_str = row['valeur']
    
            try:
            
                if val_str.lower() in ["true", "false"]:
                    val_prep = True 
                else:
                    val_prep = float(val_str)
                
                temp = Temperature(val_prep)
                print(f"Capteur {nom} : {temp.valeur_celsius}°C -> {temp.etat}")
                
            except (ValueError, TypeError) as e:
                print(f"Capteur {nom} : REJETÉ - {e}")

#