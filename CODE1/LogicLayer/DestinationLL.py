from Storagelayer.DestinationSL import DestinationData
from Storagelayer.SLAPI import Slapi

class DestinationLL:
    def __init__(self, slapi):
        self.slapi = slapi
    
    def destination_list(self):
        return self.slapi.get_destination_list()
        
        

