import mysql.connector
from modello.voto_dto import VotoDto


class VotiDao:
    def get_voti(self):
        try:
            cnx = mysql.connector.connect(user='root',
                                          password='',
                                          host='127.0.0.1',
                                          database='libretto')
            cursor = cnx.cursor(dictionary=True)
            query = """select *
             from voti"""

            cursor.execute(query)
            result = []
            for row in cursor.fetchall():
                result.append(VotoDto(row["nome"],
                                      row["cfu"],
                                      row["punteggio"],
                                      row["lode"],
                                      bool(row["lode"]),
                                      row["data"]))
            cursor.close()
            return result

        except mysql.connector.Error as err:
            print(err)
        else:
            cnx.close()


if __name__ == '__main__':
    voti_dao = VotiDao()
    voti_dao.get_voti()
