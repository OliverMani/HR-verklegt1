import csv
from Model.WorkReport import WorkReport

class WorkReportData:
    def __init__(self):
        self.filename = "csv_files/WorkReports.csv"

    def open_file(self):
        '''opnar work reports skránna og skilar lista af tilvikum'''
        try:
            work_request_list = []
            with open(self.filename, newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    work_request_list.append(WorkReport(row['id'], row['titill'], row['vbId'], row['starfsmaður'],row['verktaki'], row['lýsing'], row['dags'],row['tími'], 
                    row['keyptur hlutur'], row['kostnaður'], row['samanlagður kostnaður'], row['heimilisfang'], row['lokið'], row['samþykkt']))
            return work_request_list
        except FileNotFoundError:
            return None                        
    
    def create_new_work_report(self, report):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "titill","verkbeidni" "starfsmadur","verktaki", "lysing", "dags","timi","keyptur_hlutur","kostnadur","samtals_kostnadur","heimilsfang", "lokid", "samtykkt"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": report.id,"titill": report.titill, "verkbeidni": report.verkbeidni,
            "starfsmaður": report.starfsmadur,"verktaki":report.verktaki,"lysing": report.lysing,
            "dags": report.dags, "timi": report.timi ,"keyptur_hlutur":report.keyptur_hlutur,
            "kostnadur": report.kostnadur,"samtals_kostnadur": report.samtals_kostnadur, "heimilsfang":report.heimilsfang, 
            "lokid": report.lokid, "samtykkt": report.samtykkt})