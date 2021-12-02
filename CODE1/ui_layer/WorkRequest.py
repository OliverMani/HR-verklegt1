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

    def sort_by_property(self, property_id):
        """Sýnir verkbeiðnir sem er skellt á ákveðna fasteign (eftir peoperty id)"""
        work_request_list = self.llapi.work_request_list()
        properties = self.llapi.get_property_list()

        for work_request in work_request_list:
            for id in work_request.fasteignid:
                if id == property_id:
                    print(work_request.titill)
