from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen


class Main_menu:
    def __init__(self) -> None:
        self.menu = """
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""

    def menubar(self):
        print(self.menu)
        selected = input("Slá inn aðgerð: ").lower()
        while selected != "q":
            print(self.menu)
            if selected == "p":
                print("Prófíll")
            elif selected == "v":
                print("Verkefni")
            elif selected == "f":
                screen = PropertyListScreen()
                screen.render()
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
