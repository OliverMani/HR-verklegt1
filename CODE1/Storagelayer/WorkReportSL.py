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
<<<<<<< HEAD
                    work_request_list.append(WorkReport(row['id'], row['titill'], row['vbId'], row['starfsmaður'],row['verktaki'], row['lýsing'], row['dags'],row['tími'],
                    row['kostnaður'], row['heimilisfang'], row['lokið'], row['samþykkt']))
=======
                    work_request_list.append(WorkReport(row['id'], row['titill'], row['vbID'], row['starfsmaðurID'],row['verktaki'], row['lýsing'], row['dags'],row['tími'],
                    row['keyptur hlutur'], row['kostnaður'], row['samanlagður kostnaður'], row['heimilisfang'], row['lokið'], row['samþykkt']))
>>>>>>> 1a0d6fa73d9bcbb9b817dd43d0b130675a989366
            return work_request_list
        except FileNotFoundError:
            return None


    def create_new_work_report(self, report):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            #csvfile.write("\n")

            fieldnames = ["id", "titill","verkbeidniID", "starfsmaðurID","verktaki", "lýsing", "dags","timi","kostnadur","heimilsfang", "lokid", "samtykkt"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": report.id,"titill": report.titill,"verkbeidniID":report.vbID, "starfsmaðurID": report.starfsmadurID,"verktaki":report.verktaki,"lýsing": report.lysing,
            "dags": report.dags, "timi": report.timi, "kostnadur": report.kostnadur, "heimilsfang":report.heimilisfang, "lokid": report.lokid, "samtykkt": report.samtykkt})
