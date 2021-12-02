from LogicLayer.LLAPI import LLAPI

class PropertyListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        properties = self.llapi.get_property_list()
        print("Fasteignir\n")
        print('\n'.join([(x.id + '. ' + x.heimilisfang) for x in properties]))

    def search_in_list(self, word):
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

        print("\n"+property.heimilisfang)
        print(property.stadur)
        print("Fasteignarnúmer", property.fasteignanumer)
        print()






    #filter
    def sort_list(self, word):
        pass
