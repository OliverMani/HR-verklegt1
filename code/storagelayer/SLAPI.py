from storagelayer.afangastadir import *
from storagelayer.fasteignir import *
from storagelayer.starfsmenn import *
from storagelayer.verkbeidnir import *
from storagelayer.verkskyrslur import *
from storagelayer.yfirmenn import *

class SLAPI:
    """Storage Layer API"""
    def __init__(self):
        self.afangastadir = AfangastadirData()
        self.fasteignir = FasteignirData()
        self.starfsmenn = StarfsmennData()
        self.verkbeidnir = VerkbeidnirData()
        self.verkskyrslur = VerkSkyrslurData()
        self.yfirmenn = YfirmennData()

    def fa_alla_afangastadi(self):
        pass

    def fa_allar_fasteignir(self):
        pass

    def fa_alla_starfsmenn(self):
        return self.starfsmenn.data
