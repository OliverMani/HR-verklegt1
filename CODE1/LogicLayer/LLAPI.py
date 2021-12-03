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
        self.work_reportll = WorkReportLL(self.slapi)

    def employee_list(self):
        '''sendir employee list í UI layer'''
        return self.employeell.employee_list()

    def work_request_list(self):
        '''sendir work request list í UI layer'''
        return self.work_requestll.work_request_list()

    def employee_profile(self):
        '''sendir employee profile í UI layer'''
        return self.employeell.employee_profile()

    def get_property_list(self):
        '''sendir property list í UI layer'''
        return self.property_ll.get_property_list()

    def get_work_report_list(self):
        '''sendir work report list í UI layer'''
        return self.work_reportll.get_employee_list()

    def get_employee_by_name(self, name): #Setja í ll
        return self.employeell.get_employee_by_name(name)

    def get_filtered_list_by_destination(self, destination):
        '''skilar filtered list af áfangastöðum'''
        return self.property_ll.get_filtered_list_by_destination(destination)

    def get_report_by_employee(self, employee):
        '''sendir work report list eftir hvaða starfsmaður vann hana'''
        return self.work_reportll.get_report_by_employee(employee)
