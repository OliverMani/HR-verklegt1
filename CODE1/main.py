from ui_layer.MainMenu import Main_menu
from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from ui_layer.LoginScreen import Login



if __name__ == "__main__":
    """ Ef notandinn er til þá opnar forritið annars er aftur beðið um innskráningu"""
    user_input = input("Nafn: ")
    user = Login(user_input).login()
    
    while user == None:
        user_input = input("Nafn: ")
        user = Login(user_input).login()
    
    main_menu = Main_menu(user)
    main_menu.menubar()


    
    
