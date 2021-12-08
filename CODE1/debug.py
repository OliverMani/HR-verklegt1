from LogicLayer.LLAPI import LLAPI
from ui_layer.WorkReport import WorkReportListScreen as A
from ui_layer.WorkRequest import WorkRequestListScreen as W

# print(W.sort_by_property("2"))
print(LLAPI().get_work_request_list_by_property_id("2"))
    