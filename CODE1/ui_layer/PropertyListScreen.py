from LogicLayer.LLAPI import LLAPI
from Model.Property import Property
from ui_layer.WorkReport import WorkReportListScreen

class PropertyListScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def render(self):
        '''Prentar Fasteignir'''
        properties = self.llapi.get_property_list()
        print("Fasteignir\n")
        print('\n'.join([(x.id + '. ' + x.heimilisfang) for x in properties]))
        print()

        #if (self.llapi.get_current_user().stada).lower() == "yfirmaður":
        #    print("\n\n(cf) Skrá nýja fasteign\n")

        print("(L)eita      (R)aða")

    def search_in_list(self):
        '''Leitar að hverju sem er í property list og skilar True ef input er fundið annars False'''
        word = input("Leita: ")
        self.show_property_with_id(word)

    def show_property_with_id(self, id):
        results = self.llapi.search_properties(id)
        for property in results:
            self.print_result(property)



    def print_result(self, property):
        '''Prentar heimilisfang fasteignar, stað fasteignar og fasteignarnúmer'''
        print("\n"+property.heimilisfang)
        print(self.llapi.get_destination_from_id(property.stadurID))
        print("Fasteignarnúmer", property.fasteignanumer)
        # Bæta við vali að byrta listann
        print("Verkbeiðnir:")
        verkbeidnir = "\n\t".join([x.id+". "+x.titill for x in self.llapi.get_work_request_list_by_property_id(property.id)])
        if len(verkbeidnir)>0:
            print("\t"+verkbeidnir)
            opna = (input("Opna verkbeiðni nr: "))
            WorkReportListScreen(self.llapi).get_work_report_by_id(opna)
        else:
            print("Engar verkskýrslur skráðar", len(verkbeidnir))
        print()

    #filter
    def sort_list(self):
        '''raðar employee list eftir áfangastað'''
        place = input("Áfangastaður: ").lower()
        sorted_list = self.llapi.get_filtered_property_list_by_destination(place)
        for prop in sorted_list:
            destinations = self.llapi.get_destination_from_id(prop.stadurID)
            print()
            print("Nafn:",prop.heimilisfang)
            print("Staður:", destinations)



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

#----------------------Update Property--------------------------------------------------------
    def update(self,id):
        property = self.llapi.get_property_by_id(id)
        print("-- Uppfæra upplýsingar um fasteign --")
        print("    Gamla gildið er í sviga, skildu")
        print("     tómt eftir til að breyta ekki")
        print()

        stadurID = property.stadurID
        heimilisfang = input(f"Nýtt heimilisfang ({property.heimilisfang}): ") or property.heimilisfang
        fm = input(f"Nýir fermetrar ({property.fm}): ") or property.fm
        herbergi = input(f"Nýr herbeggjafjöldi ({property.herbergi}): ") or property.herbergi
        tegund = input(f"Tegund herbergis ({property.tegund}): ") or property.tegund
        fasteignanumer = input(f"Fasteignanúmer ({property.fasteignanumer}): ") or property.fasteignanumer
        active = input(f"Er starfsmaður active, true/false ({property.active})?") or property.active
        new_property = Property(property.id,stadurID,heimilisfang,fm,herbergi,tegund,fasteignanumer,active)
        self.llapi.update_property(new_property)
        #id,staðurID,heimilisfang,fm,herbergi,tegund,fasteignanúmer,active
