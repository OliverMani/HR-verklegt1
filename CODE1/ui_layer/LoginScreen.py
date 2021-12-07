from LogicLayer.LLAPI import LLAPI

class Login:
    def __init__(self, username):
        self.user =  username
        self.llapi = LLAPI()

    def login(self):
        """ Fer í gegnum emloyee listan og athugar hvort nafnið á notendanum er skráð þar
        skilar bool True/False """
        return self.llapi.get_employee_by_name(self.user)
