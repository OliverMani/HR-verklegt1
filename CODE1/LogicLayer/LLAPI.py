from Storagelayer.SLAPI import Slapi
from LogicLayer.EmployeeLL import EmployeeLL

class LLAPI:
    def __init__(self):
        self.slapi = Slapi()
        self.employeell = EmployeeLL(self.slapi)

    def employee_list(self):
        return self.employeell.employee_list()
