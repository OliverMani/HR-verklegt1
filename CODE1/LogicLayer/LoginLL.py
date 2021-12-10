from Model.Employee import Employee
from Storagelayer.SLAPI import Slapi

#Skjal ekki í notkun

class LoginLL:
    def __init__(self, slapi, username):
        self.slapi = slapi
        self.user = username

    def check_login(self):
        print("Check login")
        if self.user in self.slapi:
            print(":)")
