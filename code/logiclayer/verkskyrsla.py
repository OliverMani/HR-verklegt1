class VerkSkyrslaLL:
    """Höndlar allt varðandi Verkskýrslur"""
    def __init__(self, titill, starfsmadur, lysing, dags, lokid, samtykkt):
        pass

    def skra_verkskyrslu(self, upplysingar):
        """Bætir við nýrri verkskýrslu í verkskýrsluskránna"""
        pass

    def uppfaera_verkskyrslu(self, starfsmadur):
        """bætir við einhverjum upplýsingum í sérstaka verkskýrslu,
        þarf starfsmannsauðkenni"""
        pass

    def samtykkja_verkskyrslu(self, audkenni):
        """Skilar að verkskýrsla er samþykkt ef auðkenni er rétt"""
        pass

    def finna_verkskyrslu(self, titill):
        """tekur við skráarnafni, fær síðan skránna frá data layer og
        skilar verkskýrslunni ef hún er fundin"""
        pass

    def rada_verkskyrslu(self, verkskyrsla):
        """raðar verkskýrslunum úr data layer skránni og skilar henni sorted"""
        pass

    def loka_verkskyrslu(self, audkenni):
        """lokar verkskýrslu ef rétt auðkenni er notað"""
        pass
