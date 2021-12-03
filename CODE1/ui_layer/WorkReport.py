from LogicLayer.LLAPI import LLAPI

class WorkReportListScreen:
    def __init__(self):
        self.llapi = LLAPI()
        
    def get_work_report_by_wrID(self, work_request):
        '''Á að skila work report eftir work request id'''
        self.options = f"""
A {work_request.titill}

Verk unnið af: 
    {work_request.starfsmadur}

Verktaki: 
    {work_request.Verktaki}

Tími sem fór í verk í klukkustundum: 
    {work_request.timi}

Kostnaður: 
    {work_request.keyptur_hlutur} = {work_request.kostnadur}
    ---------------------
    Samtals: {work_request.samanlagdur_kostnadur}

Staðsetning: 
    {work_request.heimilisfang}

< (S)amþykkja >

"""
        self.work_request = work_request

    def render(self):
        '''Prentar work reports'''
        work_reports = self.llapi.get_work_report_list()
        print("Skýrslur\n")
        print('\n'.join([x.titill for x in work_reports]))


    def get_reports_by_employee(self):
        '''prentar work reports eftir starfsmanni'''
        emp_report = LLAPI.get_report_by_employee()
        print(f"Nafn: {emp_report[0]}\nTitill: {emp_report[1]}")

    def get_wr_by_property(self, property_id):
        '''prentar work reports eftir fasteign'''
        prop_reports = LLAPI.get_work_reports_by_property(property_id)
        print(f"Titill: {prop_reports[0]}\nHeimilisfang: {prop_reports[1]}")


