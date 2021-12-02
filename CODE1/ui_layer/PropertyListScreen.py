from LogicLayer.LLAPI import LLAPI

class PropertyListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        properties = self.llapi.get_property_list()
        print("Fasteignir\n")
        print('\n'.join([(x.id + '. ' + x.heimilisfang) for x in properties]))

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
