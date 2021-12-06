import csv
from Model.Employee import Employee


class EmployeeData:
    """Starfsmenn Data, les og skrifar í skrána í """
    def __init__(self):
        self.filename = "csv_files/Employees.csv"

    def open_file(self):
        '''opnar employee skránna og skilar lista af tilvikum'''
        try:
            employeelist = []
            with open(self.filename, newline='', encoding="UTF-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    employeelist.append(Employee(row['id'], row['nafn'], row['netfang'], row['heimilisfang'], row['heimasimi'],
                    row['gsm'], row['afangastadur'], row['staða'], row['active']))
            return employeelist
        except FileNotFoundError:
            return None

    def has_empty_end_line(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(lines)
            return lines[-1][-1] == '\n'


    def create_new_employee(self, emp):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            if not self.has_empty_end_line():
                csvfile.write('\n')
            fieldnames = ["id", "nafn", "netfang", "heimilisfang", "heimasimi", "gsm", "afangastadur", "staða", "active"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": emp.id,"nafn": emp.nafn, "netfang": emp.netfang,"heimilisfang": emp.heimilisfang, "heimasimi": emp.heimasimi,
            "gsm": emp.gsm, "afangastadur": emp.afangastadur, "staða": emp.stada, "active": emp.active})
