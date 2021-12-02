from ui_layer.ProfileScreen import ProfileScreen
from ui_layer.WorkRequest import WorkRequestListScreen
from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen


class Main_menu:
    def __init__(self) -> None:
        self.menu = """
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""

    def leita(self, selected, leit):
        pass

    def menubar(self):
        print(self.menu)
        selected = input("\nSlá inn aðgerð: ").lower()
        #self.screens[self.current_screen].render()
        last_selected = selected

        screens = {
            "p": ProfileScreen(),
            "v": WorkRequestListScreen(),
            "f": PropertyListScreen(),
            "s": EmployeeListScreen(),
            "t": False,
            "q": False,
            "r": lambda: screens[last_selected].sort_list(input("Áfangastaður: ")),
            "l": lambda: screens[last_selected].search_in_list(input("Leita: ")),
            "x": lambda: screens["v"].filter(input("ID: "))
        }

        while selected != "q":
            screen = screens.get(selected)
            if screen == False:
                return
            print(self.menu)
            
            if screen is None:
                print("Óþekkt aðgerð")
            elif selected in "rlx":
                screen()
            else:
                screen.render()
                last_selected = selected
            selected = input("\nSlá inn aðgerð: ").lower()
