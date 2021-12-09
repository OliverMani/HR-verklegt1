from LogicLayer.LLAPI import LLAPI
from Model.WorkRequest import WorkRequest
#from ui_layer.PropertyListScreen import PropertyListScreen
from ui_layer.WorkReport import WorkReportListScreen
from ui_layer.Color import Color

from datetime import datetime

class WorkRequestListScreen:
    def __init__(self, llapi):
        self.options = """

(P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
-------------------------------------------------------------------------------------------"""
        self.llapi = llapi

    def print_wr(self, wr):
        # Ef það sé engin skýrsla gerum við stjörnu
        has_report = self.llapi.work_request_has_report(wr.id)
        report = self.llapi.get_work_report_by_work_report_id(wr.skyrslaID)
        if not has_report :
            print(wr.id+". "+wr.titill + "*")
        elif has_report and report.samthykkt.lower() == "true":
            print(Color.GREEN + Color.BOLD+ wr.id+". " +wr.titill + Color.END )
        else:
            print(Color.RED + Color.BOLD+ wr.id+". " +wr.titill + Color.END )

    def search_in_list(self):
        word = input("Leita: ")
        self.basic_info(word)

    def basic_info(self, word):
        results = self.llapi.search_work_requests(word)
        for request in results:
            stadur = self.llapi.get_destination_from_id(request.stadurID)
            fasteign = self.llapi.get_property_by_id(request.fasteignID).heimilisfang
            print("\nID: ",request.id)
            print("Titill: ",request.titill)
            print(f"Staður: ({fasteign}) {stadur} ")


    def show_work_request_with_id(self, id):
        self.basic_info(id)
        results = self.llapi.search_work_requests(id)
        for request in results:
            print("Lýsing: ", request.lysing)
            print("Verkadagur: ", request.verkadagur)
            print()
            print("Skýrsla: ")
            skyrsla = self.llapi.get_work_report_by_work_report_id(request.skyrslaID)
            if skyrsla == None:
                print("Skýrsla hefur ekki verið skráð")
                bua_til_vs = input("Viltu bæta við skýrslu við verkbeiðnina? <(J)á / (N)ei>: ")
                if bua_til_vs.lower() == "j":
                    WorkReportListScreen(self.llapi).create_new_work_report(request.id)

            else:
                WorkReportListScreen(self.llapi).render_work_report(skyrsla)




    def sort_list(self):
        '''Prentar út verkbeiðnir á ákveðnum áfangastað'''
        word = input("Áfangastaður: ")
        results = self.llapi.get_filtered_work_request_list_by_destination(word)
        for request in results:
            # Prentar út beiðni og (heimilisfang)
            self.print_wr(request)
            print(f"({self.llapi.get_property_by_id(request.stadurID).heimilisfang})\n")


    def render(self):
        '''Það prentar work requests'''
        properties = self.llapi.work_request_list()
        user = self.llapi.get_current_user()
        print("Verkbeiðnir: \t\t (VS) Verkskýrslur\n")
        # Starfsmaður sér bara þær sem eru á hanns svæði
        for workrequest in properties:
            if workrequest.stadurID == user.afangastadurID:
                self.print_wr(workrequest)
        print("\n(L) Leita\t\t(R)aða eftir áfangastað")

        #---------- Má taka flest út... held ég  -------
        #print("\n\n (vs) Til að skoða verkskýrslur") # er hægt með því að slá bara inn id
        '''Yfirmaður sér þessi skilaboð bara'''
<<<<<<< HEAD
        if (self.llapi.get_current_user().stada).lower() == ("yfirmaður" or "eigandi"):
            print("(A) Sjá allar skráðar verkbeiðnir")
            print("(C) Búa til nýja verkebiðni ")
            # print("ID + (CVS) búa til nýja verkebiðni fyrir fasteign")
            # print("(B) Breyta verkbeiðni fyrir fasteign")

=======
        if (self.llapi.get_current_user().stada).lower() == "yfirmaður":
            print("(BVS) Breyta verkskýrslu")
>>>>>>> 86b8e11d0d86d18e8fa9509dad4594c1c47fef08
            # print("(undefined) Loka verkefni ")
            # print("(undefined) Breyta verkbeiðni fyrir fasteign")
            # print("(undefined) ")

    def show_all(self):
        properties = self.llapi.work_request_list()
        print("Verkefni\n")
        for workrequest in properties:
            self.print_wr(workrequest)
        print("\n(L)eita") # er hægt að raða?


    def sort_by_property(self, property_id):
        """Sýnir verkbeiðnir sem er skellt á ákveðna fasteign (eftir property id)"""
        work_request_list = self.llapi.get_work_request_list_by_property_id(property_id)
        for work_request in work_request_list:
            #if work_request.fasteignid == property_id:
            self.print_wr(work_request)

    def sort_by_employee(self, employee_id):
        '''Raðar work requests eftir starfsmanni'''
        work_request_list = self.llapi.work_request_list()

        for work_request in work_request_list:
            for id in employee_id:
                if id == employee_id:
                    self.print_wr(work_request)

    # def mark_work_request_as_done(self, work_request_id, employee_id):
    #     '''Breytir stöðu verkbeiðnar í lokið'''
    #     work_request_list = self.llapi.work_request_list()
    #     for work_request in work_request_list:
    #             work_request[6] = "Done"
    #             print(work_request_list)

    def create_new_work_request(self):
        '''býr til nýja vinnubeiðni og appendar henni í WorkRequest.csv skránni'''
        id = str(int(self.llapi.work_request_list()[-1].id)+1) # Breytti þessu til að koma í veg fyrir yfirskrif á ID
        titill = input("\nTitill: ")
        stadurID = self.llapi.get_current_user().afangastadurID # Breytti í staðsetningu starfsmanns
        afangastadur = self.llapi.get_destination_from_id(stadurID)
        fasteignID = "0"
        while self.llapi.get_property_by_id(fasteignID) is None:
            print("Fasteignir í", afangastadur)
            fasteign = self.llapi.get_properties_by_stadur_id(stadurID.strip())
            for i in fasteign:
                print(i[0]+". "+i[1])  # Laga ef við viljum
            fasteignID = input("Nr. á fasteign: ")

        lysing = input("Lýsing á verkefni: ")
        skyrslaID = "0" # SJÁLFSVIRKT
        try:
            verkadagur = input("Dagur til að vinna verkefnið (YYYY/mm/dd): ").split('/')
            dagatal = datetime(int(verkadagur[0]), int(verkadagur[1]), int(verkadagur[2]))
            verkadagur_str = dagatal.strftime("%Y/%m/%d")

            #fasteignID = self.llapi.get_property_id_from_input(fasteign)
            if fasteignID:
                req = WorkRequest(id,stadurID,fasteignID,skyrslaID,titill,lysing,verkadagur_str,active="True")
                self.llapi.create_new_work_request(req)
            else:
                print("\nFasteign ekki til!\nEkki tókst að skrá beiðni!")
        except:
            print("Ekki gildur verkadagur!")
            print("Verkbeiðni ekki gerð!")

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
        try:
            verkadagur = input("Dagur til að vinna verkefnið (YYYY/mm/dd): ").split('/')
            dagatal = datetime(int(verkadagur[0]), int(verkadagur[1]), int(verkadagur[2]))
            verkadagur_str = dagatal.strftime("%Y/%m/%d")
            active = input(f"Active true/false ({work_request.active}): ")

            updated_work = WorkRequest(work_request.id, stadurID, fasteignID, skyrslaID, titill, lysing, verkadagur, active)
            self.llapi.update_work_request(updated_work)
        except:
            print("Ekki gildur verkadagur!")
            print("Verkbeiðni ekki gerð!")



#id,stadurID,fasteignID,skyrslaID,titill,lysing,active
