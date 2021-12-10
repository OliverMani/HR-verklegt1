from Storagelayer.SLAPI import Slapi

class DestinationLL:
    def __init__(self, slapi):
        self.slapi = slapi

    def destination_list(self):
        ''' sækir og skilar destination list'''
        return self.slapi.get_destination_list()

    def get_dest_by_name(self, nafn):
        ''' skilar destination eftir nafni '''
        destinations = self.destination_list()
        for dest in destinations:
            if dest.borg.lower() == nafn.lower() or dest.land.lower() == nafn.lower():
                return dest

    def get_destination_from_id(self, id_inp):
        ''' skilar áfangastað eftir auðkenni '''
        dest_list = self.slapi.get_destination_list()
        for destination in dest_list:
            if destination.id.strip() == id_inp.strip():
                return f"{destination.borg}, {destination.land}"
        return None
