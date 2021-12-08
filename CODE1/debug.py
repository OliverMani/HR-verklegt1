from LogicLayer.LLAPI import LLAPI
from Storagelayer.SLAPI import Slapi

work_report_list = Slapi().get_work_report_list()
property_list = Slapi().get_property_list()


print(LLAPI().get_work_reports_by_property("3"))

print(work_report_list)
print(property_list)

    
