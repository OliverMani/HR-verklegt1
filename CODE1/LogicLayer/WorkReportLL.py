from Storagelayer.SLAPI import Slapi
from Storagelayer.WorkRequestSL import WorkRequestData
from Model.WorkRequest import WorkRequest

class WorkReportLL:

    def __init__(self,slapi) -> None:
        self.slapi = slapi

    def get_work_report_list(self):
        '''fær work report skránna frá SLAPI og skilar henni í LLAPI'''
        return self.slapi.get_work_report_list()
