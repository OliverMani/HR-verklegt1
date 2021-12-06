import csv
from Model.WorkRequest import WorkRequest



class WorkRequestData:
    def __init__(self):
        self.filename = "csv_files/WorkRequests.csv"

    def open_file(self):
        '''opnar work request skránna og skilar lista af tilvikum'''
        try:
            work_request_list = []
            with open(self.filename, newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    fasteignid = row['fasteignid']
                    if ',' in fasteignid:
                        fasteignid = fasteignid.split(',')
                    else:
                        fasteignid = [fasteignid]
                    work_request_list.append(WorkRequest(row['id'], row['titill'], row['staður'], row['fasteign'], row['lýsing'], row['skýrslaid'], row['fasteignid'], row['active']))
            return work_request_list
        except FileNotFoundError:
            return None

    def has_empty_end_line(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(lines)
            return lines[-1][-1] == '\n'

    def create_new_work_request(self, req):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            if not self.has_empty_end_line():
                csvfile.write('\n')
            fieldnames = ["id","titill","staður","fasteign","lýsing","skýrslaid","fasteignid","active"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": req.id ,"titill": req.titill,"staður": req.stadur,"fasteign": req.fasteign,
            "lýsing": req.lysing,"skýrslaid": req.skyrslaid,"fasteignid": req.fasteignid,"active": req.active})
