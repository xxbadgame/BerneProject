import sqlite3
import pandas as pd

class GestionDB:
    def __init__(self, df):
        # Création de la DB
        self.conn = None
        self.df = df
    
    def connectionDB(self):
        self.conn = sqlite3.connect("BerneProject/DBBibliotheque.db")

    def ajoutDF(self):
        self.df.to_sql("Bibliotheque",self.conn, if_exists='replace',index=False)

    def fermetureDB(self):
        self.conn.close()


if __name__ == "__main__":
    pass




