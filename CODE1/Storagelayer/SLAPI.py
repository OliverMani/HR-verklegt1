from Storagelayer.EmployeeSL import EmployeeData
from Storagelayer.WorkRequestSL import WorkRequestData
from Storagelayer.PropertySL import PropertyData
from Storagelayer.WorkReportSL import WorkReportData
from Storagelayer.DestinationSL import DestinationData


class Slapi:
    def __init__(self):
        self.empSL = EmployeeData()
        self.wrSL = WorkRequestData()
        self.proSL = PropertyData()
        self.workrepSL = WorkReportData()
        self.destSL = DestinationData()

    def get_destination_list(self):
        return self.destSL.open_file()

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

    def create_new_property(self, prop):
        """ Skráir inn nýjar fasteignir"""
        return self.proSL.create_new_property(prop)

    def create_new_work_report(self,report):
        '''Setur inn nýja verkskýrslu'''
        return self.workrepSL.create_new_work_report(report)

    def create_new_work_request(self, req):
        """ Setur inn nýja verkbeiðni"""
        return self.wrSL.create_new_work_request(req)

    def update_employee(self, employee):
        return self.empLL.update(employee)

    def update_property(self, property):
        return self.proSL.update(property)

    def update_work_report(self, work_report):
        return self.workrepSL.update(work_report)

    def update_work_request(self, work_request):
        return self.wrSL.update(work_request)
