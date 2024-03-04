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



    # Fonction pour extraire, lire et afficher le contenu d'un fichier CSV :
    def lire_fichier_csv(self):
        try:
            self.df = pd.read_csv(self.nom_fichier, delimiter= ';', encoding = 'Latin-1')
            print(self.df)
            print("\n-----Extraction réussi !-----\n")
            return self.df

        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
        except Exception as e:
            print("Une erreur s'est produite :", e)


    # Fonction pour découper le champ Heure - Durée :
    def traitementDateDuree(self):
        df_temps = self.df['Heure - Durée ']

        # Création de nouvelles colonnes pour stocker les valeurs découpées
        self.df['Jour_Semaine'] = ""
        self.df['Date'] = ""
        self.df['Heure'] = ""
        self.df['Durée'] = ""

        # Parcours de chaque valeur de la colonne
        for index, ligne in enumerate(df_temps):
            # Découper la valeur en mots en utilisant l'espace comme séparateur
            mots = ligne.split()

            # Assigner les mots aux nouvelles colonnes
            self.df.at[index, 'Jour_Semaine'] = mots[0]
            self.df.at[index, 'Date'] = " ".join(mots[1:4])
            self.df.at[index, 'Heure'] = mots[4]
            self.df.at[index, 'Durée'] = " ".join(mots[6:])

        #Création d'une colonne pour avoir la date au format numérique
        self.df['DD/MM/YYYY'] = ""

        for index, ligne in enumerate(self.df['Date']):

            mots = ligne.split()

            if mots[1] in self.mois_numeriques:
                mots[1] = self.mois_numeriques[mots[1]]

            self.df.at[index, 'DD/MM/YYYY'] = " ".join(mots)

        print("-----Test réussi-----")
        self.df.columns = [col.strip() for col in self.df.columns]
        return self.df
    
    def get_df(self):
        return self.df


if __name__ == "__main__":
    TD = TraitementData("BerneProject/extraction-2021-2022-anonyme.csv")
    TD.lire_fichier_csv()
    df = TD.traitementDateDuree()
    print(df.columns)






