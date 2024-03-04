import sqlite3
import pandas as pd

class GestionDB:
    def __init__(self, df) -> None:
        # Création de la DB
        conn = sqlite3.connect("DBBibliotheque.db") 
        df = df

    def ajoutDF(self):
        self.df.to_sql("Biblotheque",self.conn, if_exists='replace',index=False)

    def fermetureDB(self):
        self.conn.close()




