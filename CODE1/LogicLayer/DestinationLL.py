from Storagelayer.DestinationSL import DestinationData
from Storagelayer.SLAPI import Slapi

class DestinationLL:
    def __init__(self, slapi):
        self.slapi = slapi
    
    def destination_list(self):
        return self.slapi.get_destination_list()
    
    def get_dest_by_name(self, nafn):
        destinations = self.destination_list()
        for dest in destinations:
            if dest.borg.lower() == nafn.lower() or dest.land.lower() == nafn.lower():
                return dest


        