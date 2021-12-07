class WorkRequest:
    """klasi sem tekur inn allar upplýsingar varðandi Verkbeiðnir"""
    def __init__(self,id,titill,stadurID,fasteignID,lysing,skyrslaID,active):
        self.id = id
        self.titill = titill
        self.stadurID = stadurID
        self.fasteignID = fasteignID
        self.lysing = lysing
        self.skyrslaID = skyrslaID
        self.active = active


# id, staðurID,fasteignID,skýrslaID,titill,lýsing, active

    def __str__(self) -> str:
        return "id: {},stadurID: {}, fasteignID: {},skyrslaID: {}, titill: {},  lysing: {}, active: {}".format(self.id,self.stadurID,self.fasteignID,self.skyrslaID,self.titill,self.lysing,self.active)
