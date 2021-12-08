from LogicLayer.LLAPI import LLAPI
from Model.WorkRequest import WorkRequest
from ui_layer.PropertyListScreen import PropertyListScreen
from ui_layer.WorkReport import WorkReportListScreen
from ui_layer.Color import Color

class WorkRequestListScreen:
    def __init__(self, llapi):
        self.options = """

(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""
        self.llapi = llapi

    def print_wr(self, wr):
        if wr.skyrslaID == "0":
            print(wr.id+". "+wr.titill)
        else:
            print(Color.GREEN + Color.BOLD+ wr.id+". " +wr.titill + Color.END)

    def search_in_list(self):
        word = input("Leita: ")
        results = self.llapi.search_work_requests(word)
        for request in results:
            print("ID: ",request.id)
            print("Titill: ",request.titill)
            print("Staður: ", self.llapi.get_destination_from_id(request.stadurID))
            print("Fasteign: ",self.llapi.get_property_by_id(request.fasteignID))
            print("Lýsing: ", request.lysing)
            print()
            print("Skýrsla: ")
            skyrsla = self.llapi.get_work_report_by_work_report_id(request.skyrslaID)
            if skyrsla == None:
                print("Skýrsla hefur ekki verið skráð")
            else:
                WorkReportListScreen(self.llapi).render_work_report(skyrsla)




    def sort_list(self):
        '''Prentar út verkbeiðnir á ákveðnum áfangastað'''
        word = input("Áfangastaður: ")
        results = self.llapi.get_filtered_work_request_list_by_destination(word)
        for request in results:
            self.print_wr(request)
            print("Staður: ",request.stadurID)
            #print(f"ID: {request.id}\nTitill: {request.titill}\nStaður: {request.stadurID}\n")

    def render(self):
        '''Það prentar work requests'''

        properties = self.llapi.work_request_list()
        print("Verkefni\n")
        #print('\n'.join([x.id + '. ' + x.titill  for x in properties]))
        for workrequest in properties:
            self.print_wr(workrequest)
        print("\n(L)eita")
        print("\n\n (vs) Til að skoða verkskýrslur")
        '''Yfirmaður sér þessi skilaboð bara'''
        if (self.llapi.get_current_user().stada).lower() == "yfirmaður":
            print("(undefined) Loka verkefni ")
            print("(undefined) Breyta verkbeiðni fyrir fasteign")
            print("(undefined) ")



    def sort_by_property(self, property_id):
        """Sýnir verkbeiðnir sem er skellt á ákveðna fasteign (eftir property id)"""
        work_request_list = self.llapi.get_work_request_list_by_property_id(property_id)
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

    def create_new_work_request(self):
        '''býr til nýja vinnubeiðni og appendar henni í WorkRequest.csv skránni'''
        id = str(int(self.llapi.work_request_list()[-1].id)+1) # Breytti þessu til að koma í veg fyrir yfirskrif á ID
        titill = input("\nTitill: ")
        stadurID = self.llapi.get_current_user().afangastadurID # Breytti í staðsetningu starfsmanns
        afangastadur = self.llapi.get_destination_from_id(stadurID)
        print("Fasteignir í", afangastadur)
        fasteign = self.llapi.get_properties_by_stadur_id(stadurID.strip())
        for i in fasteign:
            print(i[0]+". "+i[1])  # Laga ef við viljum
        fasteignID = (input("Nr. á fasteign: "))
        lysing = input("Lýsing á verkefni: ")
        skyrslaID = id # SJÁLFSVIRKT
        #fasteignID = self.llapi.get_property_id_from_input(fasteign)
        if fasteignID:
            req = WorkRequest(id,stadurID,fasteignID,skyrslaID,titill,lysing,active="True")
            self.llapi.create_new_work_request(req)
        else:
            print("\nFasteign ekki til!\nEkki tókst að skrá beiðni!")


    def update(self,id):
        work_request = self.llapi.get_work_request_by_id(id)
        print("-- Uppfæra upplýsingar um verkbeiðnir --")
        print("    Gamla gildið er í sviga, skildu")
        print("     tómt eftir til að breyta ekki")
        print()

        stadurID = work_request.stadurID
        fasteignID = work_request.fasteignID
        skyrslaID = work_request.skyrslaID
        titill = input(f"Nýr titill (\"{work_request.titill}\"): ")
        lysing = input(f"Ný lýsing (\"{work_request.lysing}\"): ")
        active = input(f"Active true/false ({work_request.active}): ")

        updated_work = WorkRequest(work_request.id, stadurID, fasteignID, skyrslaID, titill, lysing, active)
        self.llapi.update_work_request(updated_work)


#id,stadurID,fasteignID,skyrslaID,titill,lysing,active
