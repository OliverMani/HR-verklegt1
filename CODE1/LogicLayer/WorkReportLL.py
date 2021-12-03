from Storagelayer.SLAPI import Slapi
from Storagelayer.WorkRequestSL import WorkRequestData
from Model.WorkRequest import WorkRequest

class WorkReportLL:

    def __init__(self):
        self.slapi = Slapi()

    def get_work_report_list(self):
        '''fær work report skránna frá SLAPI og skilar henni í LLAPI'''
        return self.slapi.get_work_report_list()

    def get_report_by_employee(self, starfsmadur):
        '''vill fá tilbaka lista af skýrslum sem starfsmaður skrifaði'''
        work_report_list = self.slapi.get_work_report_list()
        new_list = []
        for employee in work_report_list:
            if starfsmadur == employee.starfsmadur:
                new_list.append(self.starfsmadur, self.titill)
        for report in new_list:
            return report[0], report[1]
