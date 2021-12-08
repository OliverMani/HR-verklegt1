from LogicLayer.LLAPI import LLAPI


prop_list = (LLAPI().get_properties_by_stadur_id("3"))

for i in prop_list:
    print(i[0]+". "+i[1])


    
