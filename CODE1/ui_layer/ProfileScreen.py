from LogicLayer.LLAPI import LLAPI

class ProfileScreen:
    def __init__(self,user):
        self.llapi = LLAPI()
        self.user = user

    def render(self):
        '''Prentar strafsmanns upplýsingar'''
        print("Prófíll")
        print()
        print("Nafn: ",(self.user.nafn).capitalize())
        print("Heililisfang: ",(self.user.heimilisfang).capitalize())
        print("GSM: ",self.user.gsm)
        print("Ntfang: ",self.user.netfang)
        print("Staður: ",(self.user.afangastadur).capitalize())
        print("Starfsheiti: ",(self.user.staða).capitalize())




