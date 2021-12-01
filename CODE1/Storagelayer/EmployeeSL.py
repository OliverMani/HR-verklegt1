import csv
from Model.Employee import Employee


class EmployeeData:
    """Starfsmenn Data, les og skrifar í skrána í """
    def __init__(self):
        self.filename = "csv_files/Employee.csv"

    def open_file(self):
        employeelist = []
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employeelist.append(Employee(row['id'], row['nafn'], row['netfang'], row['heimilisfang'], row['heimasimi'], row['gsm'], row['afangastadur'], row['staða'], row['active']))
        return employeelist
