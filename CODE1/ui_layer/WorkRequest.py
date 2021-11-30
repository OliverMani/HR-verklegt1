from LogicLayer.LLAPI import LLAPI

class WorkRequestListScreen:
    def __init__(self):
        self.options = """
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""
        self.llapi = LLAPI()

    def render(self):
        print(self.options)
        properties = self.llapi.work_request_list()
        print("Verkefni\n")
        print('\n'.join([x.titill for x in properties]))


    def select(self):
        self.render()

        print(self.options)
        selected = input("Slá inn aðgerð: ").lower()
        while selected != "q":



            if selected == "p":
                print("Prófíll")
            elif selected == "v":
                screen = WorkRequestListScreen
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