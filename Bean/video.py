class video:
    def __init__(self, id, name, qte, show):
        self.id =id
        self.name =name
        self.qte =qte
        self.show = show

    def getId(self):
        return self.id;
    def setId(self,id):
        self.id=id
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getQte(self):
        return self.qte
    def setQte(self,qte):
        self.qte = qte
    def isShow(self):
        return self.show
    def setShow(self,show):
        self.show = show