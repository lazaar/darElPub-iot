class diffusion:
    def __init__(self, id, number, date, id_video):
        self.id =id;
        self.number =number;
        self.date =date;
        self.id_video =id_video;
    def getId(self):
        return self.id;
    def setId(self,id):
        self.id=id
    def getNumber(self):
        return self.number
    def setNumber(self, number):
        self.number = number
    def getDate(self):
        return self.date
    def setDate(self,date):
        self.date = date
    def getIdVideo(self):
        return self.id_video
    def setIdVideo(self,id_video):
        self.id_video = id_video