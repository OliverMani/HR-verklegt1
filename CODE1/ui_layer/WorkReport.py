from LogicLayer.LLAPI import LLAPI
from Model.WorkReport import WorkReport

class WorkReportListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def get_work_report_by_id(self, work_report_id):
        '''Á að skila work report eftir work request id'''
        work_report = self.llapi.get_work_report_by_work_report_id(work_report_id)
        work_report = f"""
A {work_report.titill}

Verk unnið af:
    {work_report.starfsmadur}

Verktaki:
    {work_report.verktaki}

Tími sem fór í verk í klukkustundum:
    {work_report.timi}

Kostnaður:
    {work_report.kostnadur}

Staðsetning:
    {work_report.heimilisfang}

< (S)amþykkja >
"""
        print(work_report)
        return work_report

    def render(self):
        '''Prentar work reports'''
        work_reports = self.llapi.get_work_report_list()
        print("Skýrslur\n")
        print('\n'.join([x.titill for x in work_reports]))


    def get_reports_by_employee(self,employee):
        '''prentar work reports eftir starfsmanni'''
        emp_report = self.llapi.get_report_by_employee(employee)
        for report in emp_report:
            print(f"Titill: {report.titill}\n")

    def create_new_work_report(self, starfsmaður):
        '''Býr til nýja vinnuskýrslu og appendar hana í WorkReports csv skránni'''
        id = len([x.id for x in self.llapi.get_work_report_list()])+1
        titill = input("Titill: ")
        verkbeidniID = input("Verkbeiðni ID: ")
        starfsmadurID = self.llapi.get_employee_id_by_name(starfsmaður)
        print(starfsmaður)
        verktaki = input("Verktaki: ")
        lysing = input("Lýsing: ")
        dags = input("Dags: ")
        timi = input("Tími: ")
        kostnadur = input("Kostnaður: ")
        heimilisfang = input("Heimilisfang: ")
        lokið = input("Lokið: ")
        samtykkt = input("Samþykkt: ")

        report = WorkReport(id,titill,verkbeidniID,starfsmadurID, verktaki,lysing,dags,timi,kostnadur,heimilisfang,lokið,samtykkt)
        self.llapi.create_new_work_report(report)

    def get_work_report_by_property(self, property_id):
        '''prentar work reports eftir fasteign'''
        prop_reports = LLAPI.get_work_reports_by_property(property_id)
        print(f"Titill: {prop_reports[0]}\nHeimilisfang: {prop_reports[1]}")
