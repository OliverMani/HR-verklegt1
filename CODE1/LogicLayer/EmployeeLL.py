from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from Storagelayer.SLAPI import Slapi

class EmployeeLL:
    def __init__(self, slapi):
        self.slapi = slapi

    def employee_list(self):
        return self.slapi.get_employee_list()

    def employee_profile(self):
        employee_list = self.employee_list()
        name = "Jan Jacobsen"
        for names in employee_list:
            if names.nafn == name:
                return names
        return None