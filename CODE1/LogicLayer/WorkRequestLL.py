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

    def create_new_work_request(self, req):
        self.slapi.create_new_work_request(req)


    def get_list_by_employee(self, employee_id):
        """**Ekki komið** (en....) Fá lista af verkbeiðnum fyrir ákveðinn starfsmann"""
        pass

    def get_filtered_list_by_destination(self, destination_name):
        '''Skilar lista af verkbeiðnum á ákveðnum áfangastað'''
        return [req for req in self.work_request_list() if destination_name.lower() in req.stadur.lower()]

    def search(self, word):
        work_requests = self.work_request_list()
        result = []
        for work_request in work_requests:
            look_ups = [work_request.id, work_request.titill, work_request.stadur, work_request.fasteign, work_request.lysing, work_request. skyrslaid, work_request.fasteignid, work_request.active]
            for look_up in look_ups:
                if word.lower() in str(look_up).lower():
                    result.append(work_request.titill)
                    break #brjóta lookup svo niðurstaðan komi ekki oftar en einu sinni
        return result
