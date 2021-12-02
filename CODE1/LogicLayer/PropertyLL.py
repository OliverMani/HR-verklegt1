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

    def get_filtered_list_by_work_request(self, work_request):
        pass
