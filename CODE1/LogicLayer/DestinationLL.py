from Storagelayer.DestinationSL import DestinationData
from Storagelayer.SLAPI import Slapi

class DestinationLL:
    def __init__(self, slapi):
        self.slapi = slapi
    
    def destination_list(self):
        return self.slapi.get_destination_list()

    def get_destination_from_id(self, id_inp):
        dest_list = self.slapi.get_destination_list()
        for destination in dest_list:
            if destination.id.strip() == id_inp.strip():
                return f"{destination.borg}, {destination.land}"
        return None



        


