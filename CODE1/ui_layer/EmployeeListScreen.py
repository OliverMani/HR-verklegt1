from LogicLayer.LLAPI import LLAPI
from Model.Employee import Employee


class EmployeeListScreen:
    def __init__(self, llapi):
        self.llapi = llapi

    def render(self):
        '''Prentar út nöfn starfsmanna'''
        employees = self.llapi.employee_list()
        print("Starfsmenn\n")

        print('\n'.join([x.id + '. ' + x.nafn for x in employees]))
        if (self.llapi.get_current_user().stada).lower() == "yfirmaður":
            print("\n\n(ce) Skrá nýjan starfsmann")

        print("\n(L)eita     (R)aða")

    def search_in_list(self):
        '''leitar eftir starfsmanni og prentar út upplýsingar um starfsmannin, ef starfsmaður finnst ekki þá prentar fallið villu skilaboð'''
        word = input("Leita: ")
        results = self.llapi.search_employees(word)
        for employee in results:
            print("ID:", emp.id)
            print("Nafn:", employee.nafn)
            print("GSM:", employee.gsm)
            print("Netfang:", employee.netfang)
            print()

    def sort_list(self):
        '''Skrifar út raðaðan lista af starfsmönnum eftir Áfangastöðum'''
        place = input("Áfangastaður: ")
        employee_list = self.llapi.get_filtered_employee_list_by_destination(place)
        for emp in employee_list:
            print("ID:", emp.id)
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
        afangastadur = self.llapi.get_current_user().afangastadur #sjálfsvirkt, yfirmaður skráir ekki starfsmann fyrir annan stað
        stada = "starfsmaður" # Sjálfsvirkt, yfirmaður skráir ekki starfsmann sem Chuck Norris sko
        emp = Employee(id,nafn,netfang,heimilsfang,heimasimi,gsm,afangastadur,stada,active="True")
        self.llapi.create_new_employee(emp)
