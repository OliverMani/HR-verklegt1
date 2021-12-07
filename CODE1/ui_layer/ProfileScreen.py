from LogicLayer.LLAPI import LLAPI

class ProfileScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def render(self):
        '''Prentar strafsmanns upplýsingar'''
        self.render_user(self.llapi.get_current_user())

    def render_user(self, user):
        print("Prófíll", user.nafn)
        print()
        print("Nafn: ",user.nafn)
        print("Heililisfang: ",user.heimilisfang.capitalize())
        print("GSM: ",user.gsm)
        print("Ntfang: ",user.netfang)
        print("Staður: ",self.llapi.get_destination_from_id(user.afangastadurID))
        print("Starfsheiti: ",user.stada.capitalize())

    def search_in_list(self):
        print("Þú getur ekki leitað í prófíl")

    def sort_list(self):
        print("Þú getur ekki raðað í prófíl")
