class WorkReport:
    """klasi sem tekur inn allar upplýsingar varðandi Verkskýrslum"""
    def __init__(self, id, titill, vbId, starfsmadur, verktaki, lysing, dags, timi, kostnadur, heimilisfang, lokid, samtykkt):
        self.id = id
        self.titill = titill
        self.vbId = vbId
        self.starfsmadur = starfsmadur
        self.verktaki = verktaki
        self.lysing = lysing
        self.dags = dags
        self.timi = timi
        self.kostnadur = kostnadur
        self.heimilisfang = heimilisfang
        self.lokid = lokid
        self.samtykkt = samtykkt

