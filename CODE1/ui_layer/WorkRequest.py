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
        report = self.llapi.get_work_report_by_work_report_id(wr.id)
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
            print("Skýrsla: ")  #get_work_report_by_work_request_id 
            skyrsla = self.llapi.get_work_report_by_work_report_id(request.id)
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
        if (self.llapi.get_current_user().stada).lower() == "yfirmaður" or "eigandi":
            print("(A) Sjá allar skráðar verkbeiðnir")
            print("(C) Búa til nýja verkbeiðni fyrir fasteign")
            print("ID + (CVS) búa til nýja verkbeiðni fyrir fasteign")
            print("(B) Breyta verkbeiðni fyrir fasteign")
            print("ID + (BVS) breyta verkskýrslu fyrir verkbeiðni")

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



    def get_input(self, id=None):
        creating = id is None #Breyta sem segir hvort verið sé að búa til eða uppfæra
        old_request = None
        stadurID = None # skilgreina stadurID...
        if creating: # Basically ef við séum að búa til
            id = str(int(self.llapi.work_request_list()[-1].id)+1)
            stadurID = self.llapi.get_current_user().afangastadurID
            old_request = WorkRequest(id, '', '', '', '', '', '', '')
        else:
            old_request = self.llapi.get_work_request_by_id(id)
            if old_request is None:
                print("Verkbeiðnin fannst ekki!")
                return None
            stadurID = input(f"Staður ID ({old_request.stadurID}): ") or old_request.stadurID


        # Sameiginlegur kóði
        fasteignID = "0"
        gildar_fasteignir = self.llapi.get_properties_by_stadur_id(stadurID.strip())
        # Fá út öll ID til að bera saman
        gildar_fasteignir_ids = [fasteign[0] for fasteign in gildar_fasteignir]
        while fasteignID not in gildar_fasteignir_ids:
            for fasteign in gildar_fasteignir:
                print(f"{fasteign[0]}. {fasteign[1]}")
            fasteignID = input(f"Nr. á fasteign ({old_request.fasteignID}): ") or old_request.fasteignID
        skyrslaID = "0"
        titill = input(f"Titill (\"{old_request.titill}\"): ") or old_request.titill
        lysing = input(f"Lýsing: (\"{old_request.lysing}\"): ") or old_request.lysing
        #if True:
        try:
            verkadagur = (input(f"Dagur til að vinna verkefnið (YYYY/mm/dd) ({old_request.verkadagur}): ") or old_request.verkadagur).split('/')
            dagatal = datetime(int(verkadagur[0]), int(verkadagur[1]), int(verkadagur[2]))
            verkadagur_str = dagatal.strftime("%Y/%m/%d")
            active = input(f"Active true/false ({old_request.active}): ") or old_request.active

            return WorkRequest(old_request.id, stadurID, fasteignID, skyrslaID, titill, lysing, verkadagur, active)
        except:
            print("Ekki gildur verkadagur!")
            print("Verkbeiðni ekki gerð!")


        #id, stadurID, fasteignID, skyrslaID, titill, lysing, verkadagur, active

    def create_new_work_request(self):
        '''býr til nýja vinnubeiðni og appendar henni í WorkRequest.csv skránni'''
        info = self.get_input()
        if info:
            self.llapi.create_new_work_request(info)

    def update(self,id):
        info = self.get_input(id)
        if info:
            self.llapi.update_work_request(info)
