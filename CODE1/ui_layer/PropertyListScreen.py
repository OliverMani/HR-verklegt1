from LogicLayer.LLAPI import LLAPI
from Model.Property import Property

class PropertyListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        '''Prentar Fasteignir'''
        properties = self.llapi.get_property_list()
        print("Fasteignir\n")
        print('\n'.join([(x.id + '. ' + x.heimilisfang) for x in properties]))

    ### FÆRA VIRKNI Í LOGIC!!!!
    def search_in_list(self):
        '''Leitar að hverju sem er í property list og skilar True ef input er fundið annars False'''
        word = input("Leita: ")
        found = False
        properties = self.llapi.get_property_list()
        for property in properties:
            look_up = [property.id,property.stadur, property.heimilisfang, property.fm, property.herbergi,property.tegund, property.fasteignanumer ]
            if word in look_up:
                found = True
                self.print_result(property)
        if not found:
            print("Ekkert fannst")


    def print_result(self, property):
        '''Prentar heimilisfang fasteignar, stað fasteignar og fasteignarnúmer'''
        print("\n"+property.heimilisfang)
        print(property.stadur)
        print("Fasteignarnúmer", property.fasteignanumer)
        print()

    #filter
    def sort_list(self):
        '''raðar employee list eftir áfangastað'''
        place = input("Áfangastaður: ")
        property_list = self.llapi.get_property_list()
        sorted_list = self.llapi.get_filtered_list_by_destination(place)
        for prop in sorted_list:
            print("Nafn:",prop.heimilisfang)
            print("Staður:", prop.stadur)
            #print("Netfang:", prop.netfang)
            print()

    def create_new_property(self):
        '''býr til nýja fasteign og appendar því í fasteignar csv skánni'''
        id = len([x.id for x in self.llapi.get_property_list()])+1
        stadur = input("Áfangastaður: ")
        heimilisfang = input("Heimilisfang: ")
        fm = input("Fermetrar: ")
        herbergi = input("Herbergi: ")
        tegund = input("Tegund: ")
        fasteignanumer = input("Fasteignanúmer: ")
        active = "True"
        prop = Property(id,stadur,heimilisfang, fm, herbergi, tegund, fasteignanumer, active )
        return self.llapi.create_new_property(prop)
