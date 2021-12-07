from ui_layer.ProfileScreen import ProfileScreen
from ui_layer.WorkRequest import WorkRequestListScreen
from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen
from ui_layer.WorkReport import WorkReportListScreen
from LogicLayer.LLAPI import LLAPI

UNKNOWN_COMMAND = "Óþekkt aðgerð"
ONLY_MANAGERS = "Aðgerð aðeins fyrir yfirmenn"
ONLY_CHUCþK_NORRIS = "Aðgerð aðeins fyrir Chuck Norris"

MANAGER_STRING = "yfirmaður"

class Main_menu:
    def __init__(self,user) -> None:
        self.llapi = LLAPI()
        self.llapi.set_current_user(user)
        self.menu = f"""
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn        {"<(C) Bæta við>" if self.llapi.get_current_user().stada == MANAGER_STRING else (' ' * 12)}   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""
    ## Væri gott að færa þetta yfir í logic...
    def parse_digital_commands(self, command) -> tuple:
        """Þetta fall slítur í sundur tölu og skipun (t.d 13v) og skilar í túplu númeri og skipun"""
        # Ef skipunin er BARA tala (kemur í veg fyrir crash)
        if command.isdigit():
            return (command, '')

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

        def switch_creations(last):
            """Þetta fall á að vera inní menubar fallinu, þetta skiptir upp hvað 'c' skipuin gerir"""
            if self.llapi.get_current_user().stada == MANAGER_STRING:
                if last == 's':
                    screens['s'].create_new_employee()
                elif last == 'v':
                    screens['v'].create_new_work_request()
                elif last == 'f':
                    screens['f'].create_new_property()



        screens = {
            "p": ProfileScreen(self.llapi),
            "v": WorkRequestListScreen(self.llapi),
            "vs": WorkReportListScreen(self.llapi),
            "f": PropertyListScreen(self.llapi),
            "s": EmployeeListScreen(self.llapi),
            "t": False,
            "q": False,
            "r": lambda: screens[last_selected].sort_list(),
            "l": lambda: screens[last_selected].search_in_list(),
            "x": lambda: screens["v"].sort_by_property(input("ID: ")),
            "c": lambda: switch_creations(last_selected),
            #"ce": lambda: screens["s"].create_new_employee() if self.llapi.get_current_user().stada == MANAGER_STRING else print(ONLY_MANAGERS),
            "cvr": lambda: screens["v"].create_new_work_report(self.llapi.get_current_user()) if self.llapi.get_current_user().stada == MANAGER_STRING else print(ONLY_MANAGERS),
            #"cvb": lambda: screens["v"].create_new_work_request() if self.llapi.get_current_user().stada == MANAGER_STRING else print(ONLY_MANAGERS),
            #"cf": lambda: screens["f"].create_new_property() if self.llapi.get_current_user().stada == MANAGER_STRING else print(ONLY_MANAGERS),
            "y": lambda: screens["v"].get_requests_by_employee(input("Starfsmaður: ")),
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
            elif selected in "rlxwc":
                screen()
            elif selected == 'cvr':
                WorkReportListScreen().create_new_work_report(self.llapi.get_current_user().nafn)
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
                    if last_selected == 'v':
                        screens[command].get_work_report_by_id(number)
                    elif last_selected == 's':
                        screens[command].render_work_report_by_employee_id(number)
                    elif last_selected == 'f':
                        screens[command].render_work_report_by_property_id(number)
                elif command == 'p':
                    if self.llapi.get_current_user().stada == MANAGER_STRING:
                        if last_selected == 's':
                            screens['p'].render_user(self.llapi.get_employee_by_id(number))
                        else:
                            print(ONLY_MANAGERS)
                else:
                    print(UNKNOWN_COMMAND)
            else:
                screen.render()
                last_selected = selected
            selected = input("\nSlá inn aðgerð: ").lower()
