class Employee:
    """klasi sem tekur inn allar nauðsynlegu upplýsingar um starfsmann"""
    def __init__(self, id, nafn, netfang, heimilisfang, gsm, afangastadur, staða, active):
        self.nafn = nafn
        self.id = id
        self.netfang = netfang
        self.heimilisfang = heimilisfang
        self.gsm = gsm
        self.afangastadur = afangastadur
        self.staða = staða
        self.active = active

    def __str__(self) -> str:
        return "id: {}, nafn: {}, netfang: {}, heimilisfang: {}, gsm: {}, afangastadur: {}, staða: {}, active: {}".format(self.id, self.nafn, self.netfang, self.heimilisfang, self.gsm, self.afangastadur, self.staða, self.active)