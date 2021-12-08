from Storagelayer.SLAPI import Slapi
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.WorkRequestLL import WorkRequestLL
from LogicLayer.PropertyLL import PropertyLL
from LogicLayer.WorkReportLL import WorkReportLL
from LogicLayer.MainMenuLL import MainMenuLL



class LLAPI:
    def __init__(self):
        self.slapi = Slapi()
        self.destination_ll = DestinationLL(self.slapi)
        self.employeell = EmployeeLL(self.slapi, self)
        self.work_requestll = WorkRequestLL(self.slapi, self)
        self.property_ll = PropertyLL(self.slapi, self)
        self.work_reportll = WorkReportLL(self)
        self.main_menu_ll = MainMenuLL(self, None)


    def employee_list(self):
        '''sendir employee list í UI layer'''
        return self.employeell.employee_list()

    def work_request_list(self):
        '''sendir work request list í UI layer'''
        return self.work_requestll.work_request_list()

    def employee_profile(self):
        '''sendir employee profile í UI layer'''
        return self.employeell.employee_profile()
#----------------------------Create föll -----------------------------------------
    def create_new_employee(self,emp):
        return self.employeell.create_new_employee(emp)

    def create_new_property(self, prop):
        return self.property_ll.create_new_property(prop)

    def create_new_work_report(self, report):
        return self.work_reportll.create_new_work_report(report)

    def create_new_work_request(self, req):
        return self.work_requestll.create_new_work_request(req)
#-----------------------------------------------------------------------------------
    def get_destination_list(self):
        """Sækjir lista yfir áfangastaði í Logic layer"""
        return self.destination_ll.destination_list()

    def get_destination_by_name(self, name):
        return self.destination_ll.get_dest_by_name(name)
        
    def get_property_list(self):
        '''sendir property list í UI layer'''
        return self.property_ll.get_property_list()

    def get_work_report_list(self):
        '''sendir work report list í UI layer'''
        return self.work_reportll.get_work_report_list()

    def get_employee_by_name(self, name): #Setja í ll
        return self.employeell.get_employee_by_name(name)

    def get_employee_id_by_name(self, name): #Setja í ll
        return self.employeell.get_employee_id_by_name(name)

    def get_employee_by_id(self, id):
        return self.employeell.get_employee_by_id(id)

    def get_report_by_employee(self, employee):
        '''sendir work report list eftir hvaða starfsmaður vann hana'''
        return self.work_reportll.get_report_by_employee(employee)

    def get_property_by_id(self, property_id):
        '''skilar fasteign eftir auðkenni'''
        return self.property_ll.get_property_by_id(property_id)

    def get_property_id_from_input(self, property_name):
        """ Fall sem tekur inn hvaða fasteign var skráð í verkbeiðnina og finnur hvaða ID hún hefur"""
        return self.property_ll.get_property_id_from_input(property_name)

    def get_work_request_list_by_property_id(self, property_id):
        '''skilar work request list eftir fasteign'''
        return self.work_requestll.get_list_by_property(property_id)

    def get_work_reports_by_property(self, property_id):
        '''skilar work reports eftir fasteignum'''
        return self.work_reportll.get_work_reports_by_property(property_id)

    def get_employee_by_work_report_id(self, work_id):
        return self.work_reportll.get_employee_by_work_report_id(work_id)

    def get_work_report_by_work_report_id(self, work_report_id):
        return self.work_reportll.get_work_report_by_work_report_id(work_report_id)

    def get_work_request_by_id(self, id):
        return self.work_requestll.get_work_request_by_id(id)

#------------------------[ Search ]---------------------------------------------
    def search_properties(self, search):
        return self.property_ll.search(search)

    def search_employees(self, search):
        return self.employeell.search(search)

    def search_work_requests(self, search):
        return self.work_requestll.search(search)

#-------------------------------------------------------------------------------
#--------------------------[ Sort/Filter ]---------------------------------------
    def get_filtered_property_list_by_destination(self, destination):
        '''skilar filtered list af áfangastöðum'''
        return self.property_ll.get_filtered_list_by_destination(destination)

    def get_filtered_employee_list_by_destination(self, destination):
        '''Skilar starfsmönnum eftir áfangastað'''
        return self.employeell.get_filtered_list_by_destination(destination)

    def get_filtered_work_request_list_by_destination(self, destination):
        return self.work_requestll.get_filtered_list_by_destination(destination)

#-------------------------------------------------------------------------------
#--------------------------[ Main Menu LL ]---------------------------------------

    def set_current_user(self, user):
        return self.main_menu_ll.set_current_user(user)

    def get_current_user(self):
        return self.main_menu_ll.get_current_user()

#---------------------- Update Föll----------------------------------------------

    def update_employee(self, emp):
        return self.employeell.update_employee(emp)
