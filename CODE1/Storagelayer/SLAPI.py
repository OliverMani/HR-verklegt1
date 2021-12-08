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

#----------------------- Get föll ------------------------------#

    def get_destination_list(self):
        ''' skilar destination list '''
        return self.destSL.open_file()

    def get_employee_list(self):
        ''' skilar employee list '''
        return self.empSL.open_file()

    def get_work_request_list(self):
        ''' skilar work request list '''
        return self.wrSL.open_file()

    def get_property_list(self):
        ''' skilar property list '''
        return self.proSL.open_file()

    def get_work_report_list(self):
        ''' skilar work report list '''
        return self.workrepSL.open_file()

#----------------------- Create föll ------------------------------#

    def create_new_employee(self,emp):
        ''' Býr til nýjan starfsmann '''
        return self.empSL.create_new_employee(emp)

    def create_new_property(self, prop):
        """ Skráir inn nýjar fasteignir """
        return self.proSL.create_new_property(prop)

    def create_new_work_report(self,report):
        ''' Setur inn nýja verkskýrslu '''
        return self.workrepSL.create_new_work_report(report)

    def create_new_work_request(self, req):
        """ Setur inn nýja verkbeiðni """
        return self.wrSL.create_new_work_request(req)

#----------------------- update föll ------------------------------#

    def update_employee(self, employee):
        ''' uppfærir employee csv skránna '''
        return self.empSL.update(employee)

    def update_property(self, property):
        ''' uppfærir upplýsingar sem notandi breytir um fasteign í property csv skránni '''
        return self.proSL.update(property)

    def update_work_report(self, work_report):
        ''' uppfærir upplýsingar varðandi work report sem notandi vildi uppfæra í work report csv skránni '''
        return self.workrepSL.update(work_report)

    def update_work_request(self, work_request):
        ''' uppfærir upplýsingar um work request sem notandi vill uppfæra '''
        return self.wrSL.update(work_request)
