from ui_layer.EmployeeListScreen import EmployeeListScreen
from ui_layer.PropertyListScreen import PropertyListScreen
from ui_layer.WorkReport import WorkReportListScreen
from ui_layer.WorkRequest import WorkRequestListScreen

from ui_layer.LoginScreen import Login




user_input = input("Nafn: ")
#user_input = "Jan Jacobsen"
user = Login(user_input).login()

while user == None:
    user_input = input("Nafn: ")
    user = Login(user_input).login()

print(user)

WorkReportListScreen().create_new_work_report(user)

    
