from ui_layer.MainMenu import Main_menu
from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from ui_layer.LoginScreen import Login


if __name__ == "__main__":
    """ Ef notandinn er til þá opnar forritið annars er aftur beðið um innskráningu"""
    user = input("Nafn: ")
    logged_in = Login(user).login()
    
    while logged_in == None:
        user = input("Nafn: ")
        logged_in = Login(user).login()
    
    main_menu = Main_menu()
    main_menu.menubar()


    
    
