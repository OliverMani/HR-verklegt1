from Storagelayer.PropertySL import PropertyData
from Model.Property import Property
from Storagelayer.SLAPI import Slapi

class PropertyLL:
    """PropertyLL, """
    def __init__(self, slapi, llapi):
        self.slapi = slapi
        self.llapi = llapi

    def get_property_list(self):
        '''fær property list frá SLAPI og skilar honum Í LLAPI'''
        return self.slapi.get_property_list()

    def get_filtered_list_by_destination(self, destination):
        '''Skilar lista af fasteignum á ákveðnum stað'''
        destinations = self.llapi.get_destination_by_name(destination)
        properties = self.slapi.get_property_list()
        if destinations == None:
            return []
        result = []
        for property in properties:
            if property.stadurID == destinations.id:
                result.append(property)
        return result


    def get_property_by_id(self, property_id):
        properties = self.get_property_list()
        for property in properties:
            if property.id == property_id:
                return property
        return None

    def get_property_id_from_input(self, fasteign_name):
        properties = self.get_property_list()
        for property in properties:
            if fasteign_name.lower() == property.heimilisfang.lower():
                found = True
                return property.id
        return None

    def search(self, word):
        properties = self.get_property_list()
        result = []
        for property in properties:
            if word.isdigit():
                if word == property.id:
                    result.append(property)
                    break
            else:
                look_ups = [property.id,property.stadur, property.heimilisfang, property.fm, property.herbergi,property.tegund, property.fasteignanumer ]
                for look_up in look_ups:
                    if word.lower() in str(look_up).lower():
                        result.append(property)
                        break #brjóta lookup svo niðurstaðan komi ekki oftar en einu sinni
        return result

    def create_new_property(self, prop):
        self.slapi.create_new_property(prop)

    def update_property(self, prop):
        self.slapi.update_property(prop)