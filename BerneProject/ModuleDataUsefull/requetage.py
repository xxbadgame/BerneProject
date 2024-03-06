import sqlite3

class Requetage:
    def __init__(self, db):
        self.db = db
        self.conn = None

    def connect(self):
        """Établit une connexion à la base de données."""
        self.conn = sqlite3.connect(self.db)

    def close(self):
        """Ferme la connexion à la base de données."""
        if self.conn:
            self.conn.close()

    def TauxEmpruntDansleTemps(self, debutDate, finDate, domaine, ressource):
        """Retourne le taux d'emprunt par domaines."""
        query = """
        SELECT 
            Date(Date) AS Jour, 
            (SUM(CASE WHEN Type = 'Emprunt ' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS TauxEmprunt
        FROM 
            Bibliotheque
        WHERE
            Date >= ? AND Date <= ? AND Domaines = ? AND Ressource = ?
        GROUP BY 
            Jour;
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (debutDate, finDate, domaine, ressource))
        return cursor.fetchall()
    
    def DomainesUniques(self):
        """Retourne les domaines."""
        query = """
        SELECT DISTINCT Domaines FROM Bibliotheque;
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    
    # def testRequete(self):
    #     query = """
    #     SELECT DISTINCT Type FROM Bibliotheque;
    #     """

if __name__ == "__main__":
    rq = Requetage("BerneProject/DBBibliotheque.db")
    rq.connect()
    print(rq.testRequete())
    print(rq.TauxEmpruntDansleTemps())
    rq.close()