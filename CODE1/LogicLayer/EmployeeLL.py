from Storagelayer.EmployeeSL import EmployeeData
from Model.Employee import Employee
from Storagelayer.SLAPI import Slapi

class EmployeeLL:
    def __init__(self, slapi, llapi):
        self.slapi = slapi
        self.llapi = llapi

    def employee_list(self):
        '''fær employee list frá SLAPI og sendir hann í LLAPI'''
        return self.slapi.get_employee_list()

    
    def search(self, word):
        ''' tékkar á því hvort user input (staður) er í destinations og skilar lista af employees eftir stað '''
        employees = self.employee_list()
        result = []
        for employee in employees:
            if word.isdigit():
                if word == employee.id:
                    result.append(employee)
                    break
            else:
                # Leita eftir id,nafn,netfang,heimilisfang,heimasimi,gsm,afangastadurID,staða,active
                look_ups = [employee.id, employee.nafn, employee.netfang, employee.heimilisfang, employee.heimasimi, employee.gsm, employee.afangastadurID, employee.stada, employee.active]                
                for look_up in look_ups:
                    if word.lower() in str(look_up).lower(): #str til öryggis ef look_up skilar int
                        result.append(employee)
                        break
        return result

    """def employee_profile(self, user):
        '''tekur inn employee list og skilar nöfnum'''
        employee_list = self.employee_list()
        for names in employee_list:
            if names.nafn == user.nafn:
                 return names
        return None"""

    def get_employee_by_name(self, name):
        """ er hann til eða ekki """
        employee_list = self.employee_list()
        for user in employee_list:
            if name == user.nafn:
                return user
        return None

    def get_employee_id_by_name(self, name):
        """ er hann til eða ekki """
        employee_list = self.employee_list()
        for user in employee_list:
            if name == user.nafn:
                return user.id
        return None

    def create_new_employee(self,emp):
        ''' notar slapi til að búa til nýjan starfsmann '''
        self.slapi.create_new_employee(emp)

    def get_filtered_list_by_destination(self, destination):
        ''' Skilar lista af starfsmönnum á ákveðnum áfangastað '''
        employees = self.employee_list()
        dest = self.llapi.get_destination_by_name(destination)
        if dest == None:
            return []
        result = []
        for employee in employees:
            if employee.afangastadurID == dest.id:
                result.append(employee)
        return result

    def get_employee_by_id(self, id):
        ''' Finnur Starfsmann eftir ID '''
        employees = self.employee_list()
        for employee in employees:
            if id == employee.id:
                return employee
        return None

    def update_employee(self, emp):
        ''' notar slapi til að uppfæra upplýsingar um starfsmann '''
        self.slapi.update_employee(emp)
