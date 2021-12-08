from LogicLayer.LLAPI import LLAPI
from Model.Employee import Employee
from ui_layer.WorkRequest import WorkRequestListScreen
from ui_layer.WorkReport import WorkReportListScreen


class EmployeeListScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def render(self):
        '''Prentar út nöfn starfsmanna'''
        employees = self.llapi.employee_list()
        print("Starfsmenn\n")
        print('\n'.join([x.id + '. ' + x.nafn for x in employees]))
        print("\n(L)eita     (R)aða")
        print("Sláðu inn númer starsmanns til að sjá upplýsingar")

    def search_in_list(self):
        '''leitar eftir starfsmanni og prentar út upplýsingar um starfsmannin, ef starfsmaður finnst ekki þá prentar fallið villu skilaboð'''
        word = input("Leita: ")
        results = self.llapi.search_employees(word)
        for employee in results:
            self.show_emp_with_id(employee.id)
        
    def show_emp_with_id(self, id):    
        employees = self.llapi.search_employees(id)
        for employee in employees:
            print("\nID:", employee.id)
            print("Nafn:", employee.nafn)
            print("GSM:", employee.gsm)
            print("Netfang:", employee.netfang)
            # Skoða varkefnalista starfsmanns
            verkbeidnir = input("Sjá verkskýrslur starfsmanns ((J)á / (N)ei)")
            if verkbeidnir.lower() == "j":
                verk_listi = "\n\t".join([x.id+". "+x.titill for x in self.llapi.get_work_request_list_by_employee_id(employee.id)])
                if len(verk_listi)>0:
                    print("\t"+verk_listi)
                    opna = (int(input("Opna skýrslu nr: ")))
                    WorkReportListScreen(self.llapi).render_work_report(opna)
                else:
                    print("Engar verkskýrslur skráðar.")                
            print()

    def sort_list(self):
        '''Skrifar út röðuðum lista af starfsmönnum eftir Áfangastöðum'''
        place = input("Áfangastaður: ")
        employee_list = self.llapi.get_filtered_employee_list_by_destination(place)
        for emp in employee_list:
            print("\nID:", emp.id)
            print("Nafn:",emp.nafn)
            print("Gsm:", emp.gsm)
            print("Netfang:", emp.netfang)
            print()

    def create_new_employee(self):
        id = str(int(self.llapi.employee_list()[-1].id)+1) # Breytti þessu til að koma í veg fyrir yfirskrif á ID
        nafn = input("Nafn: ")
        netfang = input("Netfang: ")
        heimilsfang = input("Heimilsfang: ")
        heimasimi = input("Heimasími: ")
        gsm = input("Gsm: ")
        afangastadurID = self.llapi.get_current_user().afangastadurID #sjálfsvirkt, yfirmaður skráir ekki starfsmann fyrir annan stað
        stada = "starfsmaður" # Sjálfsvirkt, yfirmaður skráir ekki starfsmann sem Chuck Norris sko
        emp = Employee(id,nafn,netfang,heimilsfang,heimasimi,gsm,afangastadurID,stada,active="True")
        self.llapi.create_new_employee(emp)
#-----------------------Update föll-----------------------------------------------------
    def update(self,id):
        employee = self.llapi.get_employee_by_id(id)
        print("-- Uppfæra upplýsingar um starfsmenn --")
        print("    Gamla gildið er í sviga, skildu")
        print("     tómt eftir til að breyta ekki")
        print()

        nafn = input(f"Nýtt nafn ({employee.nafn}): ") or employee.nafn
        netfang = input(f"Nýtt netfang ({employee.netfang}): ") or employee.netfang
        heimilisfang = input(f"Nýtt heimilisfang ({employee.heimilisfang}): ") or employee.heimilisfang
        heimasimi = input(f"Nýr heimasími ({employee.heimasimi}): ") or employee.heimasimi
        gsm = input(f"Nýr gsm ({employee.gsm}): ") or employee.gsm
        afangastadurID = input(f"Hver er réttur áfangastaður? ({employee.afangastadurID}): ") or employee.afangastadurID
        stada = employee.stada
        active = input(f"Er starfsmaður active, true/false ({employee.active})?") or employee.active
        new_employee = Employee(employee.id,nafn,netfang,heimilisfang,heimasimi,gsm,afangastadurID,stada,active)
        self.llapi.update_employee(new_employee)

#id,nafn,netfang,heimilisfang,heimasimi,gsm,afangastadurID,staða,active

#-----------------------------------------------------------------------------------------
