import csv
from Model.Property import Property


class PropertyData:
    def __init__(self):
        self.filename = "csv_files/Properties.csv"

    def open_file(self):
        '''opnar property skránna og skilar lista af tilvikum'''
        propertylist = []
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                propertylist.append(Property(row['id'], row['staður'], row['heimilisfang'], row['fm'], row['herbergi'], row['tegund'], row['fasteignanúmer'], row['active']))
        return propertylist

    def create_new_property(self, prop):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "staður", "heimilisfang", "fm", "herbergi", "tegund", "fasteignanúmer", "active"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": prop.id, "staður": prop.stadur, "heimilisfang": prop.heimilisfang, "fm": prop.fm, 
            "herbergi": prop.herbergi, "tegund": prop.tegund, "fasteignanúmer": prop.fasteignanumer, "active": prop.active})
                                     