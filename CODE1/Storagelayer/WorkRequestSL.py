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
                work_request_list.append(WorkRequest(row['id'], row['titill'], row['staður'], row['fasteign'], row['lýsing'], row['skyrslaid'], row['fasteignid'], row['active']))
        return work_request_list
    
    def create_new_work_request(self, req):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id","titill","staður","fasteign","lýsing","skýrslaid","fasteignid","active"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": req.id ,"titill": req.titill,"staður": req.stadur,"fasteign": req.fasteign,
            "lýsing": req.lysing,"skýrslaid": req.skyrslaid,"fasteignid": req.fasteignid,"active": req.active})
                                                       