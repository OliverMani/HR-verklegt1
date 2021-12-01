class WorkRequest:
    """klasi sem tekur inn allar upplýsingar varðandi Verkbeiðnir"""
    def __init__(self,id,titill,stadur,fasteign,lysing,fasteignid,active):
        self.id = id
        self.titill = titill
        self.stadur = stadur
        self.fasteign = fasteign
        self.lysing = lysing
        self.fasteignid = fasteignid
        self.active = active


# id,titill,staður,skýrsla/fasteign,lýsing,active

    def __str__(self) -> str:
        return "id: {}, titill: {}, stadur: {}, fasteign: {}, lysing: {}, fasteignid: {}, active: {}".format(self.id,self.titill,self.fasteign,self.lysing,self.fasteignid,self.active)
