import sqlite3

class Requetage:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """Établit une connexion à la base de données."""
        self.conn = sqlite3.connect(self.db_path)

    def close(self):
        """Ferme la connexion à la base de données."""
        if self.conn:
            self.conn.close()

    def analyse_prets_par_domaine(self):
        """Effectue une analyse des prêts par domaine."""
        query = """
        SELECT Domaines, COUNT(*) AS Nombre_Prets
        FROM prets
        GROUP BY Domaines
        ORDER BY Nombre_Prets DESC
        """
        return self._execute_query(query)

    def tendance_prets_selon_jour_semaine(self):
        """Analyse la tendance des prêts selon le jour de la semaine."""
        query = """
        SELECT Jour_Semaine, COUNT(*) AS Nombre_Prets
        FROM prets
        GROUP BY Jour_Semaine
        ORDER BY CASE Jour_Semaine
            WHEN 'Lundi' THEN 1
            WHEN 'Mardi' THEN 2
            WHEN 'Mercredi' THEN 3
            WHEN 'Jeudi' THEN 4
            WHEN 'Vendredi' THEN 5
            WHEN 'Samedi' THEN 6
            WHEN 'Dimanche' THEN 7
        END
        """
        return self._execute_query(query)

    def duree_moyenne_prets_selon_type_ressource(self):
        """Calcule la durée moyenne des prêts selon le type de ressource."""
        query = """
        SELECT Type, AVG(Durée) AS Duree_Moyenne
        FROM prets
        GROUP BY Type
        """
        return self._execute_query(query)

    def _execute_query(self, query):
        """Exécute une requête SQL et retourne les résultats."""
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
