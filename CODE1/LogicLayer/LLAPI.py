from Storagelayer.SLAPI import Slapi
from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.WorkRequestLL import WorkRequestLL
from LogicLayer.PropertyLL import PropertyLL
from LogicLayer.WorkReportLL import WorkReportLL





class LLAPI:
    def __init__(self):
        self.slapi = Slapi()
        self.employeell = EmployeeLL(self.slapi)
        self.work_requestll = WorkRequestLL(self.slapi)
        self.property_ll = PropertyLL(self.slapi)
<<<<<<< HEAD
        
=======
        self.work_reportll = WorkReportLL(self.slapi)
>>>>>>> ea48b1cdb991839b77f3459fdd596a8cc74df234

    def employee_list(self):
        return self.employeell.employee_list()

    def work_request_list(self):
        return self.work_requestll.work_request_list()

    def employee_profile(self):
        return self.employeell.employee_profile()

    def get_property_list(self):
        return self.property_ll.get_property_list()

<<<<<<< HEAD
    
    
=======
    def get_work_report_list(self):
        return self.work_reportll.get_employee_list()
>>>>>>> ea48b1cdb991839b77f3459fdd596a8cc74df234
