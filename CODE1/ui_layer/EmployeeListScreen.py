from LogicLayer.LLAPI import LLAPI

class EmployeeListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        employees = self.llapi.employee_list()
        print("Starfsmenn\n")
        print('\n'.join([x.nafn for x in employees]))
        print("\n(L)eita")

    def search_in_list(self, word):
        employee_list = self.llapi.employee_list()
        for name in employee_list:
            if word == name.nafn:
                result = f"""
Nafn: {name.nafn}
Netfang: {name.netfang}
Heimilisfang: {name.heimilisfang}
GSM: {name.gsm}
Áfangastaður: {name.afangastadur}
Starfsheiti: {name.staða}"""
                return result
        return None

    def select(self):
        self.render()
        selected = input("Slá inn aðgerð: ").lower()
        while selected != "q":
            if selected == "p":
                print("Prófíll")
            elif selected == "v":
                print("Verkefni")
            elif selected == "f":
                screen = PropertyListScreen()
                screen.render()
            elif selected == "t":
                return
            elif selected == "q":
                return
            elif selected == "l":
                search = input("Leita: ")
                print(self.search_in_list(search))
            else:
                print("Aðgerð ekki til ")
            selected = input("Slá inn aðgerð: ").lower()

    

 