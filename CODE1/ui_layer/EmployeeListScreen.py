from LogicLayer.LLAPI import LLAPI

class EmployeeListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        employees = self.llapi.employee_list()
        print("Starfsmenn\n")
        print('\n'.join([x.nafn for x in employees]))


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
            else:
                print("Aðgerð ekki til ")
            selected = input("Slá inn aðgerð: ").lower()
