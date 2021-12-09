from LogicLayer.LLAPI import LLAPI
from Model.WorkReport import WorkReport
import datetime

class WorkReportListScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def get_work_report_by_id(self, work_report_id):
        '''Á að skila work report eftir work request id'''
        work_report = self.llapi.get_work_report_by_work_report_id(work_report_id)
        if work_report_id == "":
            return
        elif work_report is None:
            print("Engin skýrsla fannst við þessari beiðni")
            if work_report_id:
                print("\nTil að búa til verkskýrslu,")
                print(f"Skrifaðu \"{work_report_id}cvs\" og fylltu út")
        else:
            self.render_work_report(work_report)
# LAGA ÞESSI FÖLL _________________________________________________________
    def render_work_report_by_employee_id(self, employee_id):
        employee = self.llapi.get_employee_by_id(employee_id)
        if employee is None:
            print("Starfsmaður fannst ekki")
        else:
            work_reports = self.llapi.get_report_by_employee(employee.id)
            if len(work_reports) == 0:
                print("Það er engin verkskýrsla skráð á þennan starfsmann!")
            for report in work_reports:
                self.render_work_report(report)

    def render_work_report_by_property_id(self, property_id):
        property = self.llapi.get_property_by_id(property_id)
        if property is None:
            print("Fasteign finnst ekki")
        else:
            work_reports = self.llapi.get_work_reports_by_property(property.id)
            if len(work_reports) == 0:
                print("Það er engin verkskýrsla skráð á þessa fasteign!")
            for report in work_reports:
                self.render_work_report(report)
#______________________________________________________________________________


    def render_work_report(self, work_report):
        employee = self.llapi.get_employee_by_work_report_id(work_report.id)
        employee_name = 'Ekki vitað'
        if employee is not None:
            employee_name = employee.nafn

        work_report_str = f"""
A {work_report.titill}
Verk unnið af:
    {employee_name}
Verktaki:
    {work_report.verktaki}
Tími sem fór í verk í klukkustundum:
    {work_report.timi}
Kostnaður:
    {work_report.kostnadur}
Staðsetning:
    {work_report.heimilisfang}
"""
        print(work_report_str)
        if self.llapi.get_current_user().stada.lower() == "yfirmaður":
            accept = input("Viltu samþykkja þessa verkskýrslu? (j/n): ")
            if accept.lower() == 'j':
                self.llapi.accept_work_report_by_id(work_report.id) #Keyra ferli sem samþykkir skýrslu
                print("Samþykkti skýrslu")
            #print("< (S)amþykkja >")
        print("-------------------------")
        return work_report_str


    def render(self):
        ''' Prentar work reports'''
        user = self.llapi.get_current_user()
        return_list = []
        print("Verkskýrslur: \t\t (V)erkbeiðnir \n")
        if user.stada.lower() == "starfsmaður":
            return_list = self.llapi.get_report_by_employee(user.id)
        elif user.stada.lower() == "yfirmaður":
            return_list = self.llapi.get_report_by_destination_id(user.afangastadurID)
        for report in return_list:
            print(report.id+". "+ report.lysing)

        print("(cvr) Skrá nýja skýrslu")
        if (self.llapi.get_current_user().stada).lower() == "yfirmaður":
            print("(sv) Samþykkja verkskýrslu")




    def get_reports_by_employee(self,employee):
        '''prentar work reports eftir starfsmanni'''
        emp_report = self.llapi.get_report_by_employee(employee)
        for report in emp_report:
            print(f"Titill: {report.titill}\n")

    def create_new_work_report(self, verkbeidni_id):
        '''Býr til nýja vinnuskýrslu og appendar hana í WorkReports csv skránni'''
        current_user = self.llapi.get_current_user()
        #ef verkbeiðnin er ekki til þá keyrum við ekki fallið
        if self.llapi.get_work_request_by_id(verkbeidni_id) is None:
            print("Verkbeiðni", verkbeidni_id, "er ekki til!")
            return #Stoppa fallið
        id = verkbeidni_id
        titill = None #Sjálfvirkt #input("Titill: ")
        verkbeidniID = verkbeidni_id #input("Verkbeiðni ID: ")
        # Starfsmaður ID er sjálfvirkt
        starfsmadurID = current_user.id
        verktaki = input("Verktaki: ")
        if verktaki == "":
            verktaki = "Enginn"
        lysing = input("Lýsing: ")
        dags = datetime.datetime.now().strftime("%Y/%m/%d") #input("Dags: ") # geri sjálfvirkt
        timi = input("Tími: ")
        kostnadur = "0"
        if current_user.stada == "yfirmaður":
            kostnadur = input("Kostnaður: ")
        #heimilisfang = input("Heimilisfang: ")
        lokið = "true"#input("Lokið: ")#Sjálfkrafa
        samtykkt = "false"# input("Samþykkt: ")#Sjálfkrafa

        report = WorkReport(id,titill,verkbeidniID,starfsmadurID, verktaki,lysing,dags,timi,kostnadur,None,lokið,samtykkt)
        self.llapi.create_new_work_report(report)

    def get_work_report_by_property(self, property_id):
        '''prentar work reports eftir fasteign'''
        prop_reports = LLAPI.get_work_reports_by_property(property_id)
        print(f"Titill: {prop_reports[0]}\nHeimilisfang: {prop_reports[1]}")
