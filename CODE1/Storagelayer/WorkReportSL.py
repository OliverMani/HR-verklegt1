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
                    work_request_list.append(WorkReport(row['id'], row['titill'], row['vbID'], row['starfsmaðurID'],row['verktaki'], row['lýsing'], row['dags'],row['tími'],
                    row['kostnaður'], row['heimilisfang'], row['lokið'], row['samþykkt']))
            return work_request_list
        except FileNotFoundError:
            return None

    def has_empty_end_line(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines[-1][-1] == '\n'

    def create_new_work_report(self, report):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            if not self.has_empty_end_line():
                csvfile.write("\n")

            fieldnames = ["id", "titill","verkbeidniID", "starfsmaðurID","verktaki", "lýsing", "dags","timi","kostnadur","heimilsfang", "lokid", "samtykkt"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": report.id,"titill": report.titill,"verkbeidniID":report.vbID, "starfsmaðurID": report.starfsmadurID,"verktaki":report.verktaki,"lýsing": report.lysing,
            "dags": report.dags, "timi": report.timi, "kostnadur": report.kostnadur, "heimilsfang":report.heimilisfang, "lokid": report.lokid, "samtykkt": report.samtykkt})

    def update(self, work_report):
        # Við þurfum að fá allan listann yfir verkskýrslur til að geta breytt honum síðan
        work_reports = self.open_file()
        # Í þessari for lykkju erum við að breyta stakinu sem við ætlum að breyta
        # x verður númer á staki, en ekki stakið sjálft
        for x in range(len(work_reports)):
            if work_reports[x].id == work_reports.id:
                work_reports[x] = work_report
                break
        # Þegar við erum búnir að uppfæra listann, þá þurfum við að yfirskrifa allt í skránni
        with open(self.filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            for report in len(work_reports):
                writer.writerow({"id": report.id,"titill": report.titill,"verkbeidniID":report.vbID, "starfsmaðurID": report.starfsmadurID,"verktaki":report.verktaki,"lýsing": report.lysing,
                "dags": report.dags, "timi": report.timi, "kostnadur": report.kostnadur, "heimilsfang":report.heimilisfang, "lokid": report.lokid, "samtykkt": report.samtykkt})
