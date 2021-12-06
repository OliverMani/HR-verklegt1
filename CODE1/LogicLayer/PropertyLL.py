from Storagelayer.PropertySL import PropertyData
from Model.Property import Property
from Storagelayer.SLAPI import Slapi

class PropertyLL:
    """PropertyLL, """
    def __init__(self, slapi):
        self.slapi = slapi

    def get_property_list(self):
        '''fær property list frá SLAPI og skilar honum Í LLAPI'''
        return self.slapi.get_property_list()

    def get_filtered_list_by_destination(self, destination):
        return [dest for dest in self.slapi.get_property_list() if dest.stadur == destination]

    def get_property_by_id(self, property_id):
        properties = self.get_property_list()
        for property in properties:
            if property.id == property_id:
                return property
        return None

    def search(self, word):
        properties = self.get_property_list()
        result = []
        for property in properties:
            if word.lower() in property.heimilisfang.lower():
                result.append(property)
        return result

    def create_new_property(self, prop):
        self.slapi.create_new_property(prop)
