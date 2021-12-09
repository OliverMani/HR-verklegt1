class WorkReport:
    """klasi sem tekur inn allar upplýsingar varðandi Verkskýrslum"""
    def __init__(self, id, titill, verkbeidniID, starfsmadurID, verktaki, lysing, dags, timi, kostnadur, heimilisfang, lokid, samthykkt):
        self.id = id
        self.titill = titill
        self.verkbeidniID = verkbeidniID
        self.starfsmadurID = starfsmadurID
        self.verktaki = verktaki
        self.lysing = lysing
        self.dags = dags
        self.timi = timi
        self.kostnadur = kostnadur
        self.heimilisfang = heimilisfang
        self.lokid = lokid
        self.samthykkt = samthykkt
    
    def __str__(self):
        return f"id:{self.id}, titill:{self.titill}, verkbeidniID:{self.verbeidniID}, starfsmadurID: {self.starfsmadurID}, verktaki: {self.verktaki}, lysing: {self.lysing}, dags: {self.dags}, timi: {self.timi}, kostnadur: {self.kostnadur}, heimilisfang: {self.heimilisfang}, lokid: {self.lokid}, samtykkt: {self.samtykkt}"

