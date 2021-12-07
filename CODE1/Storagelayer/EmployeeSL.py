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
                    row['gsm'], row['afangastadurID'].lower(), row['staða'], row['active']))
            return employeelist
        except FileNotFoundError:
            return None

    def has_empty_end_line(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines[-1][-1] == '\n'


    def create_new_employee(self, emp):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            if not self.has_empty_end_line():
                csvfile.write('\n')
            fieldnames = ["id", "nafn", "netfang", "heimilisfang", "heimasimi", "gsm", "afangastadurID", "staða", "active"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id": emp.id,"nafn": emp.nafn, "netfang": emp.netfang,"heimilisfang": emp.heimilisfang, "heimasimi": emp.heimasimi,
<<<<<<< HEAD
            "gsm": emp.gsm, "afangastadurID": emp.afangastadurID, "staða": emp.stada, "active": emp.active})
=======
            "gsm": emp.gsm, "afangastadur": emp.afangastadur, "staða": emp.stada, "active": emp.active})

    def update(self, employee):
        # Við þurfum að fá allan listann yfir starfsmenn til að geta breytt honum síðan
        employees = self.open_file()
        # Í þessari for lykkju erum við að breyta stakinu sem við ætlum að breyta
        # x verður númer á staki, en ekki stakið sjálft
        for x in range(len(employees)):
            if employees[x].id == employees.id:
                employees[x] = employee
                break
        # Þegar við erum búnir að uppfæra listann, þá þurfum við að yfirskrifa allt í skránni
        with open(self.filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            for emp in len(employees):
                writer.writerow({"id": emp.id,"nafn": emp.nafn, "netfang": emp.netfang,"heimilisfang": emp.heimilisfang, "heimasimi": emp.heimasimi,
                "gsm": emp.gsm, "afangastadur": emp.afangastadur, "staða": emp.stada, "active": emp.active})
>>>>>>> 116c839e0f11492440d1c4265bdde0b87ce5f94a
