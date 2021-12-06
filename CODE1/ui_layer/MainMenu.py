from ui_layer.ProfileScreen import ProfileScreen
from ui_layer.WorkRequest import WorkRequestListScreen
from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen
from ui_layer.WorkReport import WorkReportListScreen
from LogicLayer.LLAPI import LLAPI

UNKNOWN_COMMAND = "Óþekkt aðgerð"
ONLY_MANAGERS = "Aðgerð aðeins fyrir yfirmenn"
ONLY_CHUCK_NORRIS = "Aðgerð aðeins fyrir Chuck Norris"

class Main_menu:
    def __init__(self,user) -> None:
        self.user = user
        self.menu = """
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""

    def parse_digital_commands(self, command) -> tuple:
        """Þetta fall slítur í sundur tölu og skipun (t.d 13v) og skilar í túplu númeri og skipun"""
        nums = ''
        i = 0
        while command[i].isdigit():
            nums += command[i]
            i += 1
        return (nums, command[i:])


    def menubar(self):
        '''Prentar út menu og tekur inn skipanir og framkvæmir skipun'''
        selected = "p"
        #self.screens[self.current_screen].render()
        last_selected = selected


        screens = {
            "p": ProfileScreen(self.user),
            "v": WorkRequestListScreen(),
            "vs": WorkReportListScreen(),
            "f": PropertyListScreen(),
            "s": EmployeeListScreen(),
            "t": False,
            "q": False,
            "r": lambda: screens[last_selected].sort_list(),
            "l": lambda: screens[last_selected].search_in_list(),
            "x": lambda: screens["v"].sort_by_property(input("ID: ")),
            "ce": lambda: screens["s"].create_new_employee(),
            "cp": lambda: screens["f"].create_new_property(),
            "cvr": lambda: screens["v"].create_new_work_report(),

            "w": lambda: screens["v"].get_reports_by_employee(input("Starfsmaður: ")),
        }

        while selected != "q":
            screen = screens.get(selected)
            if selected[0].isdigit():
                screen = True
            if screen == False:
                return
            print(self.menu)

            if screen is None:
                print("Óþekkt aðgerð")
            elif selected in "rlx":
                screen()
            elif selected == "ce" or selected == "cp":
                screen()
            elif selected == 'cvr':
                WorkReportListScreen().create_new_work_report()
            elif selected[0].isdigit():
                # Skilast í túplu
                number, command = self.parse_digital_commands(selected)

                if command == 'v':
                    if last_selected == 'f':
                        screens[command].sort_by_property(number)
                    elif last_selected == 's':
                        screens[command].sort_by_employee(number)
                    else:
                        print("Skipun ekki framkvæmanleg hér.")
                elif command == 'vs':
                    #if last_selected == 'v':
                    screens[command].get_work_report_by_id(number)
                else:
                    print(UNKNOWN_COMMAND)
            else:
                screen.render()
                last_selected = selected
            selected = input("\nSlá inn aðgerð: ").lower()
