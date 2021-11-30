from Storagelayer.SLAPI import Slapi
from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.WorkRequestLL import WorkRequestLL

class LLAPI:
    def __init__(self):
        self.slapi = Slapi()
        self.employeell = EmployeeLL(self.slapi)
        self.work_requestll = WorkRequestLL(self.slapi)

    def employee_list(self):
        return self.employeell.employee_list()

    def work_request_list(self):
        return self.work_requestll.work_request_list()

