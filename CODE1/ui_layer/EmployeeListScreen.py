from LogicLayer.LLAPI import LLAPI
from Model.Employee import Employee


class EmployeeListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        '''Prentar út nöfn starfsmanna'''
        employees = self.llapi.employee_list()
        print("Starfsmenn\n")
        print('\n'.join([x.nafn for x in employees]))
        print("\n(L)eita     (R)aða")

    ### FÆRA VIRKNI Í LOGIC!!!!
    def search_in_list(self):
        '''leitar eftir starfsmanni og prentar út upplýsingar um starfsmannin, ef starfsmaður finnst ekki þá prentar fallið villu skilaboð'''
        word = input("Áfangastaður: ")
        employee_list = self.llapi.employee_list()
        found = False
        for name in employee_list:
            look_up = [name.id, name.nafn, name.netfang, name.heimilisfang, name.heimasimi, name.gsm, name.afangastadur, name.stada, name.active]
            if word in look_up:
                found = True
                print()
                print(f"Nafn: {name.nafn}")
                print(f"Netfang: {name.netfang}")
                print(f"Heimilisfang: {name.heimilisfang}")
                print(f"GSM: {name.gsm}")
                print(f"Áfangastaður: {name.afangastadur}")
                print(f"Starfsheiti: {name.stada}")
                print()
        if not found:
            print("Starfsmaður fannst ekki")

    def sort_list(self):
        '''raðar employee list eftir áfangastað'''
        place = input("Áfangastaður: ")
        employee_list = self.llapi.employee_list()
        sorted_list = []
        #færa í logic
        for stadur in employee_list:
            if place.strip() == stadur.afangastadur.strip():
                sorted_list.append((stadur.nafn, stadur.gsm, stadur.netfang))
        for emp in sorted_list:
            print("Nafn:",emp[0])
            print("Gsm:", emp[1])
            print("Netfang:", emp[2])
            print()

    def create_new_employee(self):
        id = len([x.id for x in self.llapi.employee_list()])+1
        nafn = input("Nafn: ")
        netfang = input("Netfang: ")
        heimilsfang = input("Heimilsfang: ")
        heimasimi = input("Heimasími: ")
        gsm = input("Gsm: ")
        afangastadur = input("Áfangastaður: ")
        stada = input("Staða: ")
        emp = Employee(id,nafn,netfang,heimilsfang,heimasimi,gsm,afangastadur,stada,active="True")
        self.llapi.create_new_employee(emp)
