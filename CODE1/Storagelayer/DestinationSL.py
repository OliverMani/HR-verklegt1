import csv
from Model.Destination import Destination


class DestinationData:
    """Starfsmenn Data, les og skrifar í skrána í """
    def __init__(self):
        self.filename = "csv_files/Destinations.csv"

    def open_file(self):
        '''opnar employee skránna og skilar lista af tilvikum'''
        try:
            destination_list = []
            with open(self.filename, newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    destination_list.append(Destination(row['id'], row['nafn'], row['netfang'], row['heimilisfang'], row['heimasimi'], row['gsm'], row['afangastadur'], row['staða'], row['active']))
            return destination_list
        except FileNotFoundError:
            return None
