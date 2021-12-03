from Storagelayer.EmployeeSL import EmployeeData
from Storagelayer.WorkRequestSL import WorkRequestData
from Storagelayer.PropertySL import PropertyData
from Storagelayer.WorkReportSL import WorkReportData


class Slapi:
    def __init__(self):
        self.empSL = EmployeeData()
        self.wrSL = WorkRequestData()
        self.proSL = PropertyData()
        self.workrepSL = WorkReportData()

    def get_employee_list(self):
        '''skilar employee list'''
        return self.empSL.open_file()

    def get_work_request_list(self):
        '''skilar work request list'''
        return self.wrSL.open_file()

    def get_property_list(self):
        '''skilar property list'''
        return self.proSL.open_file()

    def get_work_report_list(self):
        '''skilar work report list'''
        return self.workrepSL.open_file()

    def create_new_employee(self,emp):
        '''Býr til nýjan starfsmann'''
        return self.empSL.create_new_employee(emp)

