class WorkReport:
    """klasi sem tekur inn allar upplýsingar varðandi Verkskýrslum"""
    def __init__(self, id, titill, starfsmadur, lysing, dags, lokid, samtykkt):
        self.id = id
        self.titill = titill
        self.starfsmadur = starfsmadur
        self.lysing = lysing
        self.dags = dags
        self.lokid = lokid
        self.samtykkt = samtykkt
