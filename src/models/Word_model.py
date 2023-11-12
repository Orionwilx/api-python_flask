from database.db import get_connection
from .entities.Word import Word



class WordModel():

    @classmethod
    def get_words(self):
        try:
            connection = get_connection()
            words = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, tarea, completada FROM tareas_db ORDER BY tarea ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    word = Word(row[0], row[1])
                    words.append(word.to_JSON())

            connection.close()
            return words
        except Exception as ex:
            raise Exception(ex)
