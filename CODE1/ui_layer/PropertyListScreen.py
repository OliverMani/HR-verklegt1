from LogicLayer.LLAPI import LLAPI

class PropertyListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        properties = self.llapi.get_property_list()
        print("Fasteignir\n")
        print('\n'.join([(x.id + '. ' + x.heimilisfang) for x in properties]))

    def search_in_list(self):
        pass

    #filter
    def sort_list(self):
        pass
