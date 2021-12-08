from ui_layer.MainMenu import Main_menu
from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from ui_layer.LoginScreen import Login

if __name__ == "__main__":
    """ Ef notandinn er til þá opnar forritið annars er aftur beðið um innskráningu"""
    user_input = "Jan Jacobsen"
    user = Login(user_input).login()
    
    while user == None:
        user_input = input("Nafn: ")
        user = Login(user_input).login()
    
    main_menu = Main_menu(user)
    main_menu.menubar()

# LAGA:

    # 6. Starfsmaður skal geta leitað eftir öðru starfsfólki
	# Það þarf að setja þetta upp þannig að það sé hægt að leita eftir nafni starfsmans líka en ekki 	bara id 
