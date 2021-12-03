from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from Storagelayer.SLAPI import Slapi

class EmployeeLL:
    def __init__(self, slapi):
        self.slapi = slapi

    def employee_list(self):
        '''fær employee list frá SLAPI og sendir hann í LLAPI'''
        return self.slapi.get_employee_list()

    """def employee_profile(self, user):
        '''tekur inn employee list og skilar nöfnum'''
        employee_list = self.employee_list()
        for names in employee_list:
            if names.nafn == user.nafn:
                return names
        return None"""

    def get_employee_by_name(self, name): 
        """ er hann til eða ekki"""
        employee_list = self.employee_list()
        for user in employee_list:
            if name == user.nafn:
                return user
        return None

    def create_new_employee(self,emp):
        self.slapi.create_new_employee(emp)
