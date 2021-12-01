class Property:
    """Heldur utan um upplýsingar um fasteign"""
    def __init__(self, id, stadur, heimilisfang, fm, herbergi, tegund, fasteignanumer, active):
        self.id = id
        self.stadur = stadur
        self.heimilisfang = heimilisfang
        self.fm = fm
        self.herbergi = herbergi
        self.tegund = tegund
        self.fasteignanumer = fasteignanumer
        self.active = active
