import csv
from Model.Employee import Employee


class EmployeeData:
    def __init__(self):
        self.filename = "HR-VERKLEGT1/csv_files/staff.csv"

    def open_file(self):
        employeelist = [] 
        with open(self.filename, newline='', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employeelist.append(Employee(row['id'], row['name'], row['e-mail'], row['heim.'], row['sími'], row['staður'], row['staða'], row['active']))
        return employeelist