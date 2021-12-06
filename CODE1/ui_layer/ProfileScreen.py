from LogicLayer.LLAPI import LLAPI

class ProfileScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def render(self):
        '''Prentar strafsmanns upplýsingar'''
        print("Prófíll")
        print()
        print("Nafn: ",(self.llapi.get_current_user().nafn).capitalize())
        print("Heililisfang: ",(self.llapi.get_current_user().heimilisfang).capitalize())
        print("GSM: ",self.llapi.get_current_user().gsm)
        print("Ntfang: ",self.llapi.get_current_user().netfang)
        print("Staður: ",(self.llapi.get_current_user().afangastadur).capitalize())
        print("Starfsheiti: ",(self.llapi.get_current_user().stada).capitalize())

    def search_in_list(self):
        print("Þú getur ekki leitað í prófíl")

    def sort_list(self):
        print("Þú getur ekki raðað í prófíl")
