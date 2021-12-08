from Storagelayer.SLAPI import Slapi
from Storagelayer.WorkRequestSL import WorkRequestData
from Model.WorkRequest import WorkRequest

class WorkReportLL:

    def __init__(self, llapi):
        self.slapi = Slapi()
        self.llapi = llapi

    def get_work_report_list(self):
        '''fær work report skránna frá SLAPI og skilar henni í LLAPI'''
        return self.slapi.get_work_report_list()

    def get_report_by_employee(self, starfsmadur_id):
        '''vill fá tilbaka lista af skýrslum sem starfsmaður skrifaði'''
        work_report_list = self.slapi.get_work_report_list()
        new_list = []
        for workreport in work_report_list:
            if starfsmadur_id == workreport.starfsmadurID:
                new_list.append(workreport)
        return new_list

    def create_new_work_report(self,report):
        '''býr til nýja verkskýrslu'''
        self.slapi.create_new_work_report(report)


    def get_work_reports_by_property(self, property_id):
        '''skilar öllum work reports sem tengjast ákveðinni fasteign'''
        work_report_list = self.slapi.get_work_report_list()
        property_list = self.slapi.get_property_list()
        wr_by_property_list = []
        if property_id in property_list:
            for property in work_report_list:
                wr_by_property_list.append(self.titill, self.heimilisfang)
        return wr_by_property_list

    def get_work_report_by_work_report_id(self, work_report_id):
        work_report_list = self.get_work_report_list()
        for work_request in work_report_list:
            if work_report_id == work_request.id:
                return work_request
        return None

    def get_employee_by_work_report_id(self, work_id):
        '''Tekur inn ID og finnur hvaða starfsmaður vann verkið'''
        work_report = self.get_work_report_by_work_report_id(work_id)
        return self.llapi.get_employee_by_id(work_report.starfsmadurID)
