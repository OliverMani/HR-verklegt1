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
            if property.id == word:
                self.print_result(property)
            elif property.staður == word:
                self.print_result(property)
            elif property.heimilisfang == word:
                self.print_result(property)
            elif property.fm == word:
                self.print_result(property)
            elif property.herbergi == word:
                self.print_result(property)
            elif property.tegund == word:
                self.print_result(property)
            elif property.fasteignanúmer == word:
                self.print_result(property)
            else:
                print("Ekkert fannst")
                
    def print_result(self, property):

        print("\n",property.heimilisfang)
        print(property.staður)
        print("fasteignarnúmer", property.fasteignanúmer)
        print()






    #filter
    def sort_list(self, word):
        pass
    # þarf að klára....
    def search_in_list(self, search):
        found = False
        properties = self.llapi.get_property_list()
        for property in properties:
            if property.heimilisfang == search:
                print(f'Property: {property.heimilisfang}')

    #filter
    def sort_list(self, sorted):
        print("Sort Property")
