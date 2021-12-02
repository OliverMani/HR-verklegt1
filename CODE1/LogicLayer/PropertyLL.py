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
