from LogicLayer.LLAPI import LLAPI

class WorkRequestListScreen:
    def __init__(self):
        self.options = """
(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""
        self.llapi = LLAPI()

    def render(self):
        '''Það prentar work requests'''
        print(self.options)
        properties = self.llapi.work_request_list()
        print("Verkefni\n")
        print('\n'.join([x.titill for x in properties]))

    def sort_by_property(self, property_id):
        """Sýnir verkbeiðnir sem er skellt á ákveðna fasteign (eftir peoperty id)"""
        work_request_list = self.llapi.work_request_list()
        properties = self.llapi.get_filtered_list_by_destination()

        print(properties)

        for work_request in work_request_list:
            #if work_request.fasteignid == property_id:
            print(work_request.titill)

    def sort_by_employee(self, employee_id):
        '''Raðar work requests eftir starfsmanni'''
        employees = self.llapi.employee_list()
        work_request_list = self.llapi.work_request_list()

        for work_request in work_request_list:
            for id in employee_id:
                if id == employee_id:
                    print(work_request.titill)

    def mark_work_request_as_done(self, work_request_id, employee_id):
        '''Breytir stöðu verkbeiðnar í lokið'''
        employee = self.llapi.employee_list()
        work_request_list = self.llapi.work_request_list()

        for work_request in work_request_list:
            for active in work_request:
                work_request_list[6] = "Done"
                print(work_request_list)
