from LogicLayer.LLAPI import LLAPI

class Login:
    def __init__(self, username):
        self.user =  username
        self.llapi = LLAPI()

    def login(self):
        employee_list = self.llapi.employee_list()
        for users in employee_list:
            if self.user == users.nafn:
                return True
        
        print("Óþekktur notandi")
        return False