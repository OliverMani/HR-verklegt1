import csv
from Model.Property import Property


class PropertyData:
    def __init__(self):
        self.filename = "csv_files/fasteignir.csv"

    def open_file(self):
        propertylist = []
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                propertylist.append(Employee(row['id'], row['staður'], row['heimilisfang'], row['fm'], row['herbergi'], row['tegund'], row['fasteignanúmer'], row['active']))
        return propertylist
