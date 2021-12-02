import csv
from Model.Property import Property


class PropertyData:
    def __init__(self):
        self.filename = "csv_files/fasteignir.csv"

    def open_file(self):
        '''opnar property skránna og skilar lista af tilvikum'''
        propertylist = []
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                propertylist.append(Property(row['id'], row['staður'], row['heimilisfang'], row['fm'], row['herbergi'], row['tegund'], row['fasteignanúmer'], row['active']))
        return propertylist
