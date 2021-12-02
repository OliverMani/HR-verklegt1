from Storagelayer.SLAPI import Slapi
from Storagelayer.WorkRequestSL import WorkRequestData
from Model.WorkRequest import WorkRequest

class WorkRequestLL:

    def __init__(self,slapi) -> None:
        self.slapi = slapi

    def work_request_list(self):
        '''skilar work request list frá SLAPI í LLAPI'''
        return self.slapi.get_work_request_list()