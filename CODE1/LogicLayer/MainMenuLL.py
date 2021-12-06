from LogicLayer.LLAPI import LLAPI

class MainMenuLL:
    def __init__(self, llapi, user):
        self.llapi = llapi
        self.user = user

    def set_current_user(self, user):
        self.user = user

    def get_current_user(self):
        return self.user
