class StarfsmadurLL:
    """tekur við upplýsingum um starfsmann eða reynir að finna starfsmann
    """
    def __init__(self, nafn, kennitala, heima, simi, gsm, email, afangastadur):
        """tekur inn allar upplýsingar"""
        self.nafn = nafn
        self.kennitala = kennitala
        self.heima = heima
        self.simi = simi
        self.gsm = gsm
        self.email = email
        self.afangastadur = afangastadur

    def skra_nyran_starfsmann(self):
        """skráir nýjan starfsmann og setur upplýsingar í Starfsmanna skránna"""
        pass #þarf að skrá allar upplýsingar

    def uppfaera_upplysingar(self):
        """breyta upplýsingum um starfsmann og kemur því í rétta skrá"""
        pass

    def fa_upplysingar(self):
        """skilar upplýsingum um starfsmann"""
        pass

    def setja_i_skra(self):
        """appenda inn í storage layer skránna"""
        pass
