from LogicLayer.LLAPI import LLAPI

class ProfileScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        '''Prentar strafsmanns upplýsingar'''
        print("Prófíll")
        employee = self.llapi.employee_profile()
        print(employee.nafn)
        print(employee.heimilisfang)
        print(employee.gsm)
        print(employee.netfang)
        print(employee.afangastadur)
        print(employee.staða)




