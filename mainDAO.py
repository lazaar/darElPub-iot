import sqlite3

class mainDAO:
    def __init__(self):
        self.conn = sqlite3.connect('darelpub.db')

    def initDB(self):
        try:
            cursor = self.conn.cursor()
            for line in open('./script.sql'):
                cursor.execute(line)
            self.conn.commit()
        except Exception as e:
            print("Erreur d'execution du script", e)
            self.conn.rollback()
    def executeQuery(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return cursor
        except Exception as e:
            print("Erreur d'execution du query :", query, e)
            self.conn.rollback()

    def insertVideo(self, videos):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO video (name, qte, show) VALUES (?,?,?)', videos)
            self.conn.commit()
        except Exception as e:
            print("Erreur d'execution du query", e)
            self.conn.rollback()
    def getShowVideos(self):
        c = self.executeQuery('SELECT * FROM video WHERE show = 1')
        rows =  c.fetchall()
        return rows
    def insertDiffusion(self,diffusion ):
        try:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO diffusion VALUES (?,?,?)', diffusion)
            self.conn.commit()
        except Exception as e:
            print("Erreur d'execution du query", e)
            self.conn.rollback()
    def getData(self,cle):
        c = self.executeQuery("SELECT valeur FROM data WHERE cle = '"+cle+"'")
        return c.fetchall()[0][0]
    def setData(self, cle, valeur):
        c = self.executeQuery("UPDATE data SET valeur='"+valeur+"' WHERE cle='"+cle+"'")