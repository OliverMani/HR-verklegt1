class Employee:
    """klasi sem tekur inn allar nauðsynlegu upplýsingar um starfsmann"""
    def __init__(self, id, nafn, netfang, heimilisfang, heimasimi, gsm, afangastadurID, stada, active):
        self.id = id
        self.nafn = nafn
        self.netfang = netfang
        self.heimilisfang = heimilisfang
        self.heimasimi = heimasimi
        self.gsm = gsm
        self.afangastadurID = afangastadurID
        self.stada = stada
        self.active = active

    def __str__(self) -> str:
        return "id: {}, nafn: {}, netfang: {}, heimilisfang: {}, heimasimi: {} gsm: {}, afangastadurID: {}, stada: {}, active: {}".format(self.id, self.nafn, self.netfang, self.heimilisfang, self.heimasimi, self.gsm, self.afangastadurID, self.stada, self.active)