from Storagelayer.SLAPI import Slapi
from Storagelayer.WorkRequestSL import WorkRequestData
from Model.WorkRequest import WorkRequest

class WorkReportLL:

    def __init__(self,slapi) -> None:
        self.slapi = slapi

    def get_work_report_list(self):
        return self.slapi.get_work_report_list()
