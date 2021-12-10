from ui_layer.Information import InformationScreen
from ui_layer.ProfileScreen import ProfileScreen
from ui_layer.WorkRequest import WorkRequestListScreen
from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen
from ui_layer.WorkReport import WorkReportListScreen
from LogicLayer.LLAPI import LLAPI

UNKNOWN_COMMAND = "Óþekkt aðgerð"
CANT_USE_COMMAND_HERE = "Þessi skipun keyrist ekki hér"
ONLY_MANAGERS = "Aðgerð aðeins fyrir yfirmenn"
ONLY_CHUCK_NORRIS = "Aðgerð aðeins fyrir Chuck Norris"

MANAGER_STRING = "yfirmaður"
CHUCK_NORRIS_STRING = "eignadi"

class Main_menu:
    def __init__(self,user) -> None:
        self.llapi = LLAPI()
        self.llapi.set_current_user(user)
        self.menu = f"""
(P)rófíll    (V)erkbeiðnir    (F)asteignir    (S)tarfsmenn        {"<(C) Bæta við>" if self.llapi.get_current_user().stada == MANAGER_STRING or "eigandi" else (' ' * 12)}   <(Q) Hætta>
---------------------------------------------------------------------------------------------
                                                                            (i) upplýsingar"""
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
            if self.llapi.get_current_user().stada == MANAGER_STRING or CHUCK_NORRIS_STRING:
                if last == 's':
                    screens['s'].create_new_employee()
                elif last == 'v':
                    screens['v'].create_new_work_request()
                elif last == 'f':
                    screens['f'].create_new_property()
            else:
                print(ONLY_MANAGERS)



        screens = {
            "a": lambda: screens[last_selected].show_all() if self.llapi.get_current_user().stada == MANAGER_STRING or "eigandi" else print(UNKNOWN_COMMAND), #Á bara við um yfirmenn og eigendur
            "b": lambda: screens[last_selected].update(input("ID: ")),
            "c": lambda: switch_creations(last_selected),
            "p": ProfileScreen(self.llapi),
            "f": PropertyListScreen(self.llapi),
            "i": InformationScreen(),
            "l": lambda: screens[last_selected].search_in_list(),
            "q": False,
            "r": lambda: screens[last_selected].sort_list(),
            "s": EmployeeListScreen(self.llapi),
            "v": WorkRequestListScreen(self.llapi),
            "vs": WorkReportListScreen(self.llapi),
            "cvs": lambda: screens["vs"].create_new_work_report(input("Verkbeiðni ID: ")),# if self.llapi.get_current_user().stada == MANAGER_STRING else print(ONLY_MANAGERS),
            "bvs": lambda: screens["vs"].update(input("Verkskýrsla ID: ")),
        }

        while selected != "q":
            screen = screens.get(selected)

            #
            if len(selected) > 0 and selected[0].isdigit():
                screen = True

            # Prentar menu skjáinn
            print(self.menu)


            # Ef skipunin er óþekkt
            if screen is None or len(selected) == 0:
                print(UNKNOWN_COMMAND)
            # ef skipunin er einhver af þessum störum í if statementinu
            elif selected in "rlxwcba" or selected == 'cvs' or selected == 'bvs':
                screen()

            elif selected == "i":
                InformationScreen().render()

            #elif selected == 'cvs':
                #screens["vs"].create_new_work_report(input("Verkbeiðni ID: "))
                #screens[selected]()
            #ef skipunin er bara tala
            elif selected.isdigit():
                if last_selected == "s":
                    EmployeeListScreen(self.llapi).show_emp_with_id(selected)
                elif last_selected == "f":
                    PropertyListScreen(self.llapi).show_property_info(selected)
                elif last_selected == "v":
                    WorkRequestListScreen(self.llapi).show_work_request_with_id(selected)
                elif last_selected == "vs":
                    WorkReportListScreen(self.llapi).get_work_report_by_id(selected)


            # Ef skipunin er til dæmis 6vs eða 2p en ekki bara 8
            elif selected[0].isdigit() and not selected.isdigit():
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
                    else:
                        print(CANT_USE_COMMAND_HERE)
                elif command == 'p':
                    if self.llapi.get_current_user().stada == MANAGER_STRING or "eigandi":
                        if last_selected == 's':
                            screens['p'].render_user(self.llapi.get_employee_by_id(number))
                        else:
                            print(ONLY_MANAGERS)
                elif command == 'cvs':
                    if last_selected == 'v':
                        screens["vs"].create_new_work_report(number)
                elif command == 'bvs':
                    screens["vs"].update(number)
                elif command == 'b':
                    screens[last_selected].update(number)
                else:
                    print(UNKNOWN_COMMAND)

            else:
                screen.render()
                last_selected = selected
            selected = input("\nSlá inn aðgerð: ").lower()
