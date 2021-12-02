import csv
from Model.WorkRequest import WorkRequest



class WorkRequestData:
    def __init__(self):
        self.filename = "csv_files/WorkRequests.csv"

    def open_file(self):
        '''opnar work request skránna og skilar lista af tilvikum'''
        work_request_list = []
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fasteignid = row['fasteignid']
                if ',' in fasteignid:
                    fasteignid = fasteignid.split(',')
                else:
                    fasteignid = [fasteignid]
                work_request_list.append(WorkRequest(row['id'], row['titill'], row['staður'], row['fasteign'], row['lýsing'], fasteignid, row['active']))
        return work_request_list
