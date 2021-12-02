from Storagelayer.SLAPI import Slapi
from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.WorkRequestLL import WorkRequestLL
from LogicLayer.PropertyLL import PropertyLL





class LLAPI:
    def __init__(self):
        self.slapi = Slapi()
        self.employeell = EmployeeLL(self.slapi)
        self.work_requestll = WorkRequestLL(self.slapi)
        self.property_ll = PropertyLL(self.slapi)
        

    def employee_list(self):
        return self.employeell.employee_list()

    def work_request_list(self):
        return self.work_requestll.work_request_list()

    def employee_profile(self):
        return self.employeell.employee_profile()

    def get_property_list(self):
        return self.property_ll.get_property_list()

    
    
