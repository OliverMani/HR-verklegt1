class Property:
    """Heldur utan um upplýsingar um fasteign"""
    def __init__(self, id, stadurID, heimilisfang, fm, herbergi, tegund, fasteignanumer, active):
        self.id = id
        self.stadurID = stadurID
        self.heimilisfang = heimilisfang
        self.fm = fm
        self.herbergi = herbergi
        self.tegund = tegund
        self.fasteignanumer = fasteignanumer
        self.active = active

    def __str__(self):
        return f"id: {self.id}, stadurID: {self.stadurID}, heimilisfang {self.heimilisfang}, fm: {self.fm}, herbergi: {self.herbergi}, tegund: {self.tegund}, fasteignarnumer: {self.fasteignanumer}, sctive: {self.active}"
