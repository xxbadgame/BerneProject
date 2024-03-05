import csv
import pandas as pd
import tkinter as tk
import matplotlib as mpl
import datetime

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
            return self.df

        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
        except Exception as e:
            print("Une erreur s'est produite :", e)
    
    def traitementDateDuree(self):
        # Traitement de la colonne 'Heure - Durée'
        # La colonne Date
        self.df['DateComplete'] = self.df['Heure - Durée'].apply(lambda x: x.split(' - ')[0]).str.strip()
        # Je creéer une colonne avec la date formater pour ensuite l'envoyer dans ma BDD SQLite
        self.df['Jour'] = self.df['DateComplete'].apply(lambda x: x.split(' ')[1]).str.strip()
        self.df['Mois'] = self.df['DateComplete'].apply(lambda x: x.split(' ')[2]).str.strip()
        self.df['Annee'] = self.df['DateComplete'].apply(lambda x: x.split(' ')[3]).str.strip()
        self.df['HMS'] = self.df['DateComplete'].apply(lambda x: x.split(' ')[4]).str.strip()
        
        self.df['Date'] = self.df['Annee'] + '-' + self.df['Mois'].map(self.mois_numeriques) + '-' + self.df['Jour'] + ' ' + self.df['HMS']
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        
        # La colonne Durée
        self.df['Durée'] = self.df['Heure - Durée'].apply(lambda x: x.split(' - ')[1]).str.strip()
        # Suppression de la colonne 'Heure - Durée'
        self.df = self.df.drop(columns=['Heure - Durée', 'DateComplete', 'Jour', 'Mois', 'Annee', 'HMS'])
        return self.df
    
    def get_df(self):
        return self.df


if __name__ == "__main__":
    TD = TraitementData("BerneProject/extraction-2021-2022-anonyme.csv")
    TD.lire_fichier_csv()
    df = TD.traitementDateDuree()






