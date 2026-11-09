

from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = None
        cnx = DBConnect.get_connection()

        if cnx is not None:
            query = "SELECT * FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)

            result = []
            for row in cursor:
                biblioteche = Biblioteca(*row)
                result.append(biblioteche)

            cursor.close()
            cnx.close()
            return result