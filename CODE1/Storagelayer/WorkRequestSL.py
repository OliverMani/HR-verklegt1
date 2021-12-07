import csv
from Model.WorkRequest import WorkRequest



class WorkRequestData:
    def __init__(self):
        self.filename = "csv_files/WorkRequests.csv"
        self.fieldnames = ["id","staðurID","fasteignID","skýrslaID","titill","lýsing","active"]

    def open_file(self):
        '''opnar work request skránna og skilar lista af tilvikum'''
        try:
            work_request_list = []
            with open(self.filename, newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    fasteignID = row['fasteignID']
                    if ',' in fasteignID:
                        fasteignid = fasteignID.split(',')
                    else:
                        fasteignid = [fasteignid]
                    work_request_list.append(WorkRequest(row['id'], row['stadurID'], row['fasteignID'], row['skýrslaID'], row['titill'], row['lýsing'], row['active']))
            return work_request_list
        except FileNotFoundError:
            return None

    def has_empty_end_line(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines[-1][-1] == '\n'

    def create_new_work_request(self, req):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            if not self.has_empty_end_line():
                csvfile.write('\n')

            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({"id": req.id ,"staðurID": req.stadurID,"fasteignID": req.fasteignID,"skýrslaID": req.skyrslaID,"titill": req.titill,
            "lýsing": req.lysing,"active": req.active})

    def update(self, work_request):
        # Við þurfum að fá allan listann yfir verkbeiðnir til að geta breytt honum síðan
        work_requests = self.open_file()
        # Í þessari for lykkju erum við að breyta stakinu sem við ætlum að breyta
        # x verður númer á staki, en ekki stakið sjálft
        for x in range(len(work_requests)):
            if work_requests[x].id == work_request.id:
                work_requests[x] = work_request
                break
        # Þegar við erum búnir að uppfæra listann, þá þurfum við að yfirskrifa allt í skránni
        with open(self.filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            for req in len(work_requests):
                writer.writerow({"id": req.id ,"staðurID": req.stadurID,"fasteignID": req.fasteignID,"skýrslaID": req.skyrslaID,"titill": req.titill,
                "lýsing": req.lysing,"active": req.active})
