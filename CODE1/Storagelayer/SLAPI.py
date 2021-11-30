from Storagelayer.EmployeeSL import EmployeeData
from Storagelayer.WorkRequestSL import WorkRequestData

class Slapi:
    def __init__(self):
        self.empSL = EmployeeData()
        self.wrSL = WorkRequestData()

    def get_employee_list(self):
        return self.empSL.open_file()

    def get_work_request_list(self):
        return self.wrSL.open_file()