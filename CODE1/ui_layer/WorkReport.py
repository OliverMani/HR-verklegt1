from LogicLayer.LLAPI import LLAPI
from Model.WorkReport import WorkReport

class WorkReportListScreen:
    def __init__(self, work_request):
        self.options = f"""
A {work_request.titill}

Verk unnið af:
    {work_request.starfsmaður}

Verktaki:
    {work_request.Verktaki}

Tími sem fór í verk í klukkustundum:
    {work_request.tími}

Kostnaður:
    {work_request.hlutur} = {work_request.kostnaður}
    ---------------------
    Samtals: {work_request.samanlagður_kostnaður}

Staðsetning:
    {work_request.heimilisfang}

< (S)amþykkja >

"""
        self.llapi = LLAPI()
        self.work_request = work_request

    def render(self):
        '''Prentar work reports'''
        print(self.options)
        work_reports = self.llapi.get_work_report_list()
        print("Skýrslur\n")
        print('\n'.join([x.titill for x in work_reports]))


    def get_reports_by_employee(self):
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
