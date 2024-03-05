from ModuleDataUsefull.GestionDB import *
from ModuleDataUsefull.TraitementData import *
from ModuleDataUsefull.InterfaceData import *

TD = TraitementData("BerneProject/extraction-2021-2022-anonyme.csv")
TD.lire_fichier_csv()
TD.suppressionColonnes(['Réservation au nom de', 'Type', 'Dernière mise à jour'])
df = TD.traitementDateDuree()

print(df)


