from LogicLayer.LLAPI import LLAPI

class PropertyListScreen:
    def __init__(self):
        self.llapi = LLAPI()

    def render(self):
        #print(self.options)
        properties = self.llapi.employee_list()
        print("Fasteignir\n")
        print('\n'.join([x.heimilisfang for x in properties]))


    """def select(self):
        self.render()

        print(self.options)
        selected = input("Slá inn aðgerð: ").lower()
        while selected != "q":



            if selected == "p":
                print("Prófíll")
            elif selected == "v":
                print("Verkefni")
            elif selected == "s":
                screen = EmployeeListScreen()
                screen.render()
            elif selected == "t":
                return
            elif selected == "q":
                return
            else:
                print("Aðgerð ekki til ")
            selected = input("Slá inn aðgerð: ").lower()
"""