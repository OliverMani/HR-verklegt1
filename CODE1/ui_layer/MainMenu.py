from ui_layer.ProfileScreen import ProfileScreen
from ui_layer.WorkRequest import WorkRequestListScreen
from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen


class Main_menu:
    def __init__(self) -> None:
        self.menu = """
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""
        # Hér er listi af instances af skjám, gerum þetta til að þurfa ekki
        # að gera ný og ný instances í hvert skipti sem við flökkum á milli skjáa
        #self.screens = [EmployeeListScreen(), PropertyListScreen()]
        #self.current_screen = 0

    def menubar(self):
        print(self.menu)
        selected = input("\nSlá inn aðgerð: ").lower()
        #self.screens[self.current_screen].render()
        while selected != "q":
            print(self.menu)
            if selected == "p":
                screen = ProfileScreen()
                screen.render()
            elif selected == "v":
                screen = WorkRequestListScreen()
                screen.render()
            elif selected == "f":
                #self.current_screen = 1
                #self.render()
                screen = PropertyListScreen()
                screen.render()
            elif selected == "s":
                #self.current_screen = 0
                #self.menubar()
                screen = EmployeeListScreen()
                screen.render()
            elif selected == "t":
                return
            elif selected == "q":
                return
            else:
                print("Aðgerð ekki til ")
            selected = input("\nSlá inn aðgerð: ").lower()
