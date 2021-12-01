from LogicLayer.LLAPI import LLAPI


class EmployeeListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        employees = self.llapi.employee_list()
        print("Starfsmenn\n")
        print('\n'.join([x.nafn for x in employees]))
        print("\n(L)eita     (R)aða")

    def search_in_list(self, word):
        employee_list = self.llapi.employee_list()
        found = False
        for name in employee_list:
            if word == name.nafn:
                found = True
                result = f"""
Nafn: {name.nafn}
Netfang: {name.netfang}
Heimilisfang: {name.heimilisfang}
GSM: {name.gsm}
Áfangastaður: {name.afangastadur}
Starfsheiti: {name.staða}"""
                print(result)
        if not found:
            print("Starfsmaður fannst ekki")

    def sort_list(self,place):
        employee_list = self.llapi.employee_list()
        sorted_list = []
        for stadur in employee_list:
          if place.strip() == stadur.afangastadur.strip():
                sorted_list.append((stadur.nafn, stadur.gsm, stadur.netfang))
        for emp in sorted_list:
            print("Nafn:",emp[0])
            print("Gsm:", emp[1])
            print("Netfang:", emp[2])
            print()
