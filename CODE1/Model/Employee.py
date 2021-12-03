class Employee:
    """klasi sem tekur inn allar nauðsynlegu upplýsingar um starfsmann"""
    def __init__(self, id, nafn, netfang, heimilisfang, heimasimi, gsm, afangastadur, stada, active):
        self.nafn = nafn
        self.id = id
        self.netfang = netfang
        self.heimilisfang = heimilisfang
        self.heimasimi = heimasimi
        self.gsm = gsm
        self.afangastadur = afangastadur
        self.stada = stada
        self.active = active

    def __str__(self) -> str:
        return "id: {}, nafn: {}, netfang: {}, heimilisfang: {}, heimasimi: {} gsm: {}, afangastadur: {}, staða: {}, active: {}".format(self.id, self.nafn, self.netfang, self.heimilisfang, self.heimasimi, self.gsm, self.afangastadur, self.stada, self.active)