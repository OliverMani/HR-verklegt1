import csv
from Model.Property import Property


class PropertyData:
    def __init__(self):
        self.filename = "csv_files/Properties.csv"

    def open_file(self):
        '''opnar property skránna og skilar lista af tilvikum'''
        try:
            propertylist = []
            with open(self.filename, newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    propertylist.append(Property(row['id'], row['staðurID'], row['heimilisfang'], row['fm'], row['herbergi'], row['tegund'], row['fasteignanúmer'], row['active']))
            return propertylist
        except FileNotFoundError:
            return None

    def has_empty_end_line(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines[-1][-1] == '\n'

    def create_new_property(self, prop):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            if not self.has_empty_end_line():
                csvfile.write('\n')
            fieldnames = ["id", "staðurID", "heimilisfang", "fm", "herbergi", "tegund", "fasteignanúmer", "active"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": prop.id, "staðurID": prop.stadurID, "heimilisfang": prop.heimilisfang, "fm": prop.fm,
            "herbergi": prop.herbergi, "tegund": prop.tegund, "fasteignanúmer": prop.fasteignanumer, "active": prop.active})
