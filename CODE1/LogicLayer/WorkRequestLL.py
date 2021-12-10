from Storagelayer.SLAPI import Slapi
from Model.WorkRequest import WorkRequest

class WorkRequestLL:
    def __init__(self, slapi, llapi) -> None:
        self.slapi = slapi
        self.llapi = llapi

    def work_request_list(self):
        ''' skilar work request list frá SLAPI í LLAPI '''
        return self.slapi.get_work_request_list()

    def get_work_request_by_id(self, id):
        requests = self.work_request_list()
        for request in requests:
            if request.id == id:
                return request

    def get_list_by_property(self, property_id):
        """Fá lista af verkbeiðnum á ákveðinni fasteign"""
        work_requests = self.work_request_list()
        filtered = []
        for work_request in work_requests:
            if work_request.fasteignID == property_id:
                filtered.append(work_request)
        return filtered

    def create_new_work_request(self, req):
        ''' býr til nýja verkebiðni '''
        self.slapi.create_new_work_request(req)


    def get_list_by_employee(self, employee_id):
        """**Ekki komið** (en....) Fá lista af verkbeiðnum fyrir ákveðinn starfsmann"""
        req = self.slapi.get_work_request_list()
        rep = self.slapi.get_work_report_list()
        results = []
        for report in rep:
            if report.starfsmadurID == employee_id:
                for request in req:
                    if request.skyrslaID == report.id:
                        results.append(request)
        return results


    def get_filtered_list_by_destination(self, destination_name):
        ''' Skilar lista af verkbeiðnum á ákveðnum áfangastað '''
        destination = self.llapi.get_destination_by_name(destination_name)
        return [req for req in self.work_request_list() if destination.id in req.stadurID]

#--------------------- update ------------------------------#

    def update_work_request(self, work):
        return self.slapi.update_work_request(work)

#---------------------------------------------------------#
    def search(self, word):
        '''Leitar í verkbeiðnum og skilar lista af niðurstöðum'''
        work_requests = self.work_request_list()
        result = []
        for work_request in work_requests:
            if word.isdigit():
                if word == work_request.id:
                    result.append(work_request)
                    break
            else:
                look_ups = [work_request.id, work_request.stadurID, work_request.fasteignID, work_request.skyrslaID, work_request.titill, work_request.lysing, work_request.active]
                for look_up in look_ups:
                    if word.lower() in str(look_up).lower():
                        result.append(work_request)
                        break #brjóta lookup svo niðurstaðan komi ekki oftar en einu sinni
        return result

#------------------------------------------------------------

    def has_report(self, work_report_id):
        '''Skilar hvort verkbeiðnin sé með skýrslu'''
        work_request = self.get_work_request_by_id(work_report_id)
        work_report = self.slapi.get_work_report_list()
        for report in work_report:
            if report.verkbeidniID == work_report_id:
                return True
        return False
