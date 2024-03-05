from ModuleDataUsefull.GestionDB import *
from ModuleDataUsefull.TraitementData import *
from ModuleDataUsefull.InterfaceData import *

# Traitement des données
TD = TraitementData("BerneProject/extraction-2021-2022-anonyme.csv")
TD.lire_fichier_csv()
df = TD.traitementDateDuree()

# Alimentation de la base de données
GDG = GestionDB(df)
GDG.connectionDB()
GDG.ajoutDF()

# Interface utilisateur
UI = InterfaceData(df['Domaines'].unique().tolist(), df['Ressource'].unique().tolist())
UI.run()




