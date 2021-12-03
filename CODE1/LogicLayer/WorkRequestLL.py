from Storagelayer.SLAPI import Slapi
#from LogicLayer.LLAPI import LLAPI
from Storagelayer.WorkRequestSL import WorkRequestData
from Model.WorkRequest import WorkRequest

class WorkRequestLL:
    def __init__(self, slapi, llapi) -> None:
        self.slapi = slapi
        self.llapi = llapi

    def work_request_list(self):
        '''skilar work request list frá SLAPI í LLAPI'''
        return self.slapi.get_work_request_list()

    def get_list_by_property(self, property_id):
        """Fá lista af verkbeiðnum á ákveðinni fasteign"""
        property = self.llapi.get_property_by_id(property_id)
        work_requests = self.work_request_list()
        filtered = []
        for work_request in work_requests:
            for id in work_request.fasteignid:
                if id == property_id:
                    filtered.append(work_request)
        return filtered

    def get_list_by_employee(self, employee_id):
        """**Ekki komið** (en....) Fá lista af verkbeiðnum fyrir ákveðinn starfsmann"""
        pass

    def get_list_by_destination(self, destination_name):
        pass
