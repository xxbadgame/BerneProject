from ModuleDataUsefull.GestionDB import *
from ModuleDataUsefull.TraitementData import *

TD = TraitementData("BerneProject/extraction-2021-2022-anonyme.csv")
TD.lire_fichier_csv()
df = TD.traitementDateDuree()

GDB = GestionDB(df)
GDB.ajoutDF()
