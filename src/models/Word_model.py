from database.db import get_connection
from .entities.Word import Word



class WordModel():

    @classmethod
    def get_words(self):
        try:
            connection = get_connection()
            words = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, word, accept FROM words ORDER BY word ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    word = Word(row[0], row[1])
                    words.append(word.to_JSON())

            connection.close()
            return words
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_word(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, word, accept FROM words WHERE id = %s",(id,))
                row = cursor.fetchone()

                word = None
                if (row != None):
                    word = Word(row[0], row[1],row[2])
                    word = word.to_JSON()

            connection.close()
            return word
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_word(self, word):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO words (id, word, accept) 
                               VALUES (%s, %s, %s)""", (word.id, word.word, word.accept))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_word(self, word):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM words WHERE id = %s ", (word.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)