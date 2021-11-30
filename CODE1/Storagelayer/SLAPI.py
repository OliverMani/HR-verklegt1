from Storagelayer.EmployeeSL import EmployeeData


class Slapi:
    def __init__(self):
        self.empSL = EmployeeData()

    def get_employee_list(self):
        return self.empSL.open_file()
