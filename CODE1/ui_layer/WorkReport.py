from LogicLayer.LLAPI import LLAPI
from Model.WorkReport import WorkReport

class WorkReportListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def get_work_report_by_work_request_id(self, work_request_id):
        '''Á að skila work report eftir work request id'''
        work_request = self.llapi.get_work_request_by_id(work_request_id)
        work_report = self.llapi.get_work_report_by_work_report_id(work_request)
        work_report = f"""
A {work_report.titill}

Verk unnið af:
    {work_report.starfsmadur}

Verktaki:
    {work_report.verktaki}

Tími sem fór í verk í klukkustundum:
    {work_report.timi}

Kostnaður:
    {work_report.keyptur_hlutur} = {work_report.kostnadur}
    ---------------------
    Samtals: {work_report.samanlagdur_kostnadur}

Staðsetning:
    {work_report.heimilisfang}

< (S)amþykkja >

"""
        return work_report

    def render(self):
        '''Prentar work reports'''
        work_reports = self.llapi.get_work_report_list()
        print("Skýrslur\n")
        print('\n'.join([x.titill for x in work_reports]))


    def get_reports_by_employee(self):
        '''prentar work reports eftir starfsmanni'''
        emp_report = LLAPI.get_report_by_employee()
        print(f"Nafn: {emp_report[0]}\nTitill: {emp_report[1]}")

    def create_new_work_report(self):
        id = input("ID: ")
        titill = input("Titill: ")
        starfsmadur = input("Starfsmaður: ")
        lysing = input("Lýsing: ")
        dags = input("Dags: ")
        lokið = input("Lokið: ")
        samtykkt = input("Samþykkt: ")
        report = WorkReport(id,titill,starfsmadur,lysing,dags,lokið,samtykkt)
        self.llapi.create_new_work_report(report)

    def get_wr_by_property(self, property_id):
        '''prentar work reports eftir fasteign'''
        prop_reports = LLAPI.get_work_reports_by_property(property_id)
        print(f"Titill: {prop_reports[0]}\nHeimilisfang: {prop_reports[1]}")
