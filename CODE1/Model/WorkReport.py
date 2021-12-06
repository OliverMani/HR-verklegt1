class WorkReport:
    """klasi sem tekur inn allar upplýsingar varðandi Verkskýrslum"""
    def __init__(self, id, titill, vbID, starfsmadurID, verktaki, lysing, dags, timi, kostnadur, heimilisfang, lokid, samtykkt):
        self.id = id
        self.titill = titill
        self.vbID = vbID
        self.starfsmadurID = starfsmadurID
        self.verktaki = verktaki
        self.lysing = lysing
        self.dags = dags
        self.timi = timi
        self.kostnadur = kostnadur
        self.heimilisfang = heimilisfang
        self.lokid = lokid
        self.samtykkt = samtykkt

