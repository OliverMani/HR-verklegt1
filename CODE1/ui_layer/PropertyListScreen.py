from LogicLayer.LLAPI import LLAPI
from Model.Property import Property

class PropertyListScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def render(self):
        '''Prentar Fasteignir'''
        properties = self.llapi.get_property_list()
        print("Fasteignir\n")
        print('\n'.join([(x.id + '. ' + x.heimilisfang) for x in properties]))

        #if (self.llapi.get_current_user().stada).lower() == "yfirmaður":
        #    print("\n\n(cf) Skrá nýja fasteign\n")

        print("(L)eita      (R)aða")

    def search_in_list(self):
        '''Leitar að hverju sem er í property list og skilar True ef input er fundið annars False'''
        word = input("Leita: ")
        results = self.llapi.search_properties(word)
        for property in results:
            self.print_result(property)



    def print_result(self, property):
        '''Prentar heimilisfang fasteignar, stað fasteignar og fasteignarnúmer'''
        print("\n"+property.heimilisfang)
        print(self.llapi.get_destination_from_id(property.stadurID))
        print("Fasteignarnúmer", property.fasteignanumer)
        print()

    #filter
    def sort_list(self):
        '''raðar employee list eftir áfangastað'''
        place = input("Áfangastaður: ").lower()
        property_list = self.llapi.get_property_list()
        sorted_list = self.llapi.get_filtered_property_list_by_destination(place)
        for prop in sorted_list:
            print("Nafn:",prop.heimilisfang)
            print("Staður:", prop.stadurID)
            #print("Netfang:", prop.netfang)
            print()

    def create_new_property(self):
        '''býr til nýja fasteign og appendar því í fasteignar csv skánni'''
        id = str(int(self.llapi.get_property_list()[-1].id)+1) # Breytti þessu til að koma í veg fyrir yfirskrif á ID
        stadurID = self.llapi.get_current_user().afangastadurID # breytti í sjálfsvirkt þannig að það fer sjálfkrafa á staðinn sem yfirmaðurinn er yfir
        heimilisfang = input("Heimilisfang: ")
        fm = input("Fermetrar: ")
        herbergi = input("Herbergi: ")
        tegund = input("Tegund: ")
        fasteignanumer = input("Fasteignanúmer: ")
        active = "True"
        prop = Property(id,stadurID,heimilisfang, fm, herbergi, tegund, fasteignanumer, active )
        return self.llapi.create_new_property(prop)
