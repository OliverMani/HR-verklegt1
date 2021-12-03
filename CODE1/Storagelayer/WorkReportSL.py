import csv
from Model.WorkReport import WorkReport

class WorkReportData:
    def __init__(self):
        self.filename = "csv_files/WorkReports.csv"

    def open_file(self):
        '''opnar work reports skránna og skilar lista af tilvikum'''
        work_request_list = []
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                work_request_list.append(WorkReport(row['id'], row['titill'], row['vbId'], row['starfsmaður'],row['verktaki'], row['lýsing'], row['dags'],row['tími'], row['keyptur hlutur'], row['kostnaður'], row['samanlagður kostnaður'], row['heimilisfang'], row['lokið'], row['samþykkt']))
        return work_request_list                        
