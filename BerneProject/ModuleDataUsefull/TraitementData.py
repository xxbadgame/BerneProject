import csv
import pandas as pd
import tkinter as tk
import matplotlib as mpl


class TraitementData:

    def __init__(self, fichier = None) :
        self.df = None
        self.nom_fichier = fichier
        self.mois_numeriques = {
        'janvier': '01', 'février': '02', 'mars': '03', 'avril': '04', 'mai': '05', 'juin': '06',
        'juillet': '07', 'août': '08', 'septembre': '09', 'octobre': '10', 'novembre': '11', 'décembre': '12'
        }
        self.jours_numeriques = {
        'lundi': '01', 'mardi': '02', 'mercredi': '03', 'jeudi': '04', 'vendredi': '05', 'samedi': '06', 'dimanche': '07'
        }



    # Fonction pour extraire, lire et afficher le contenu d'un fichier CSV :
    def lire_fichier_csv(self):
        try:
            self.df = pd.read_csv(self.nom_fichier, delimiter= ';', encoding = 'Latin-1')
            self.df.columns = self.df.columns.str.strip()  
            print(self.df.columns)       
            return self.df

        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
        except Exception as e:
            print("Une erreur s'est produite :", e)
    
    def suppressionColonnes(self, ListeColonnes):
        # ['Réservation au nom de', 'Type', 'Dernière mise à jour']
        self.df = self.df.drop(columns=ListeColonnes)
        return self.df
    
    def traitementDateDuree(self):
        # Traitement de la colonne 'Heure - Durée'
        # La colonne Date
        self.df['Date'] = self.df['Heure - Durée'].apply(lambda x: x.split(' - ')[0]).str.strip()
        for i in range(len(self.df['Date'])):
            partieDate = self.df['Date'].str.split(' ')
            Jour, Mois, Annee , Heures = partieDate[i][1], partieDate[i][2], partieDate[i][3], partieDate[i][4]
            Heures = Heures.split(':')

        # La colonne Durée
        self.df['Durée'] = self.df['Heure - Durée'].apply(lambda x: x.split(' - ')[1]).str.strip()
        # Suppression de la colonne 'Heure - Durée'
        self.df = self.df.drop(columns=['Heure - Durée'])
        return self.df


    
    def get_df(self):
        return self.df


if __name__ == "__main__":
    TD = TraitementData("BerneProject/extraction-2021-2022-anonyme.csv")
    TD.lire_fichier_csv()
    df = TD.traitementDateDuree()






