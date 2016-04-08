import sqlite3
import Bean.video

class mainDAO:

    def __init__(self):
        self.conn = sqlite3.connect('darelpub.db')

    def initDB(self):
        try:
            cursor = self.conn.cursor()
            for line in open('../script.sql'):
                cursor.execute(line)
            self.conn.commit()
        except Exception as e:
            print("Erreur d'execution du script")
            conn.rollback()
db = video(1,'test','','')