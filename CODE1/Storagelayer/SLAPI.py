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
        return self.empSL.open_file()

    def get_work_request_list(self):
        return self.wrSL.open_file()

    def get_property_list(self):
        return self.proSL.open_file()

    def get_work_report_list(self):
        return self.workrepSL.open_file()
