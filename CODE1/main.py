from ui_layer.MainMenu import Main_menu
from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from ui_layer.LoginScreen import Login


if __name__ == "__main__":
    user = input("Nafn: ")
    logged_in = Login(user).login()
    
    while not logged_in:
        user = input("Nafn: ")
        logged_in = Login(user).login()
    
    main_menu = Main_menu()
    main_menu.menubar()


    
    
