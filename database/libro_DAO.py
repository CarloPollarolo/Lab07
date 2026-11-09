from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = None
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = "SELECT DISTINCT genere FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)

            result = []
            for row in cursor:
                generi = row[0]
                result.append(generi)

            cursor.close()
            cnx.close()
            return result

    def get_libri_filtrati(self, nome_biblioteca, genere):
        cnx = None
        cnx = DBConnect.get_connection()

        if cnx is not None:
            query = """SELECT l.*
                     FROM libro l, biblioteca b 
                     WHERE l.id_biblioteca = b.id
                     AND b.nome = COALESCE(%s,b.nome)   
                     AND l.genere = COALESCE(%s,l.genere)"""  #coalesce permette di ricevere in input b.nome e l.genere
            cursor = cnx.cursor()
            cursor.execute(query,(nome_biblioteca, genere))

            result = []
            for row in cursor:
                libri = Libro(*row)
                result.append(libri)

            cursor.close()
            cnx.close()
            return result