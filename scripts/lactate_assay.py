# -*- coding: utf-8 -*-
#head block begin
spx96 = globals().get("Spx96")
from spredo import *
#init,most important
init(spx96)
#head block end

#deck block begin

def first_feature():
    """
    在初次加载脚本时，读取
    在此函数中定义向导指示UI矩阵。每一个位置pos[x] 由如下字段组成：
        1. [可选] 板位试剂/耗材名称。字符串，比如Deep well plate* 此名字需要有对应的图片文件
        2. [可选] 试剂/耗材功能描述。字符串，
        3, [可选] 试剂/耗材特性描述。字符串，比如 340μl/W。
        4, [可选] 是否有盖板。布尔型，True or False
        5, [可选] 是否需要更换。布尔型， True or False
        6, [可选]
        板位名称
    * 顺序不要弄乱了。否则识别错误
    """
    return [
        ("POS1","TipGEBAF250A","Buffer A","",False,True,""),
        ("POS2","TipGEBAF250A","Buffer B","",False,True,""),
        ("POS3","","","",False,True,""),
        ("POS4","","","",False,True,""),
        ("POS5","","","",False,True,""),
        ("POS6","","","",False,True,""),
        ("POS7","","","",False,True,""),
        ("POS8","","","",False,True,""),
        ("POS9","","96_wellplate","Samples plate 1",False,True,""),
        ("POS10","","96_wellplate","Samples plate 2",False,True,""),
        ("POS11","","96_wellplate","Samples plate 3",False,True,""),
        ("POS12","","96_wellplate","Samples plate 4",False,True,""),
        ("POS13","","96_wellplate","Samples plate 5",False,True,""),
        ("POS14","","96_wellplate","Samples plate 6",False,True,""),
        ("POS15","","96_wellplate","Samples plate 7",False,True,""),
        ("POS16","","96_wellplate","Samples plate 8",False,True,""),
        ("POS17","TipGEBAF250A","Tips for standard curve","",False,True,""),
        ("POS18","","","",False,True,"Magnet"),
        ("POS19","TipGEBAF250A","Waste","",False,True,""),
        ("POS20","","Teleshake","",False,True,"Shaker"),
        ("POS21","","Heat block","",False,True,"Temp"),
        ("POS22","96_wellplate","Standard curve plate","",False,True,""),
        ("POS23","SuzhouChenxuCAR-190NS","Buffer A","",False,True,""),
        ("POS24","SuzhouChenxuCAR-190NS","Buffer B","",False,True,"")
    ]

binding_map({
    "POS1":["TipGEBAF250A", None, None],
    "POS2":["TipGEBAF250A", None, None],
    "POS3":["useless", None, None],
    "POS4":["useless", None, None],
    "POS5":["useless", None, None],
    "POS6":["useless", None, None],
    "POS7":["useless", None, None],
    "POS8":["useless", None, None],
    "POS9":["96_wellplate", None, None]
    "POS10":["96_wellplate", None, None],
    "POS11":["96_wellplate", None, None],
    "POS12":["96_wellplate", None, None],
    "POS13":["96_wellplate", None, None],
    "POS14":["96_wellplate", None, None],
    "POS15":["96_wellplate", None, None],
    "POS16":["96_wellplate", None, None],
    "POS17":["TipGEBAF250A", None, None],
    "POS18":[None, None, None],
    "POS19":["TipGEBAF250A", None, None],
    "POS20":[None, None, "shake"],
    "POS21":[None, None, None],
    "POS22":["96_wellplate", None, None],
    "POS23":["SuzhouChenxuCAR-190NS", None, None],
    "POS24":["SuzhouChenxuCAR-190NS", None, None]
})
#deck block end
#defining the user inputed variable num_plates as number_plates
number_plates = 1 #
shake_choice = "n" #
incubation_time = 0 #
s_require3_result = require3([],[{"number plates":[""]},{"incubation time (min)":[""]},{"shake choice (y/n)":[""]}])
number_plates = int(s_require3_result.Item2[0])
incubation_time = int(s_require3_result.Item2[1])
shake_choice = s_require3_result.Item2[2]
incubation_time = incubation_time*60

#workflow block begins
tips_list_reagent_1 = ["POS1"]
tips_list_reagent_2 = ["POS2"]
start_standard_curve_column_list = [1,2,3,4,5,6,7,8,9,10,11,12]
bin_start_standard_curve_column_list = [12,11,10,9,8,7,6,5,4,3,2,1]
target_standard_curve_column_list = [1,2,3]
cells_list =["POS13", "POS14", "POS15", "POS16"]
home()
#loading std curve 
for plate in range(int(number_plates)):
    load_tips({"Module":"POS22","Tips":8,"Col":start_standard_curve_column_list[plate],"Row":1})
    aspirate({"Module":"POS17","Tips":8,"Col":start_standard_curve_column_list[plate],"Row":1,"AspirateVolume":160,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[0],"Row":1,"DispenseVolume":50,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[1],"Row":1,"DispenseVolume":50,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[2],"Row":1,"DispenseVolume":50,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    #empty({"Module":"POS22","Tips":8,"Col":1,"Row":1,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":False,"TipTouchHeight":20,"TipTouchOffsetOfX":0,"SecondRouteRate":10})
    unload_tips({"Module":"POS19","Tips":8,"Col":6,"Row":1})

# Adding assay buffer
load_tips({"Module":tips_list_reagent_1[0],"Tips":96,"Col":1,"Row":1})  
buffer_a_counter = 0
for plate in range(int(number_plates)):
    aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":200,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
    dispense({"Module":cells_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":190,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    #changed dispense rate from 100 to 1000
    empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":1,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
    buffer_a_counter += 1
    if buffer_a_counter == int(number_plates):
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":0.1,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
unload_tips({"Module":tips_list_reagent_1[0],"Tips":96,"Col":1,"Row":1})
    
# This is for the incubation: unnecessary for glucose assay
    # mvkit("POS13","POS21")
    # temp_a(37)
    # dely(incubation_duration_secs)
    # mvkit(cells_list[plate],"POS13")

#waiting for the incubation time
dely(incubation_time)

# Adding stop solution to the plate
load_tips({"Module":tips_list_reagent_2[0],"Tips":96,"Col":1,"Row":1})
buffer_b_counter = 0
for plate in range(int(number_plates)):
    aspirate({"Module":"POS24","Tips":96,"Col":1,"Row":1,"AspirateVolume":60,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":30,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    dispense({"Module":cells_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":50,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    empty({"Module":"POS24","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":1,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
    if buffer_b_counter == int(number_plates):
        aspirate({"Module":"POS24","Tips":96,"Col":1,"Row":1,"AspirateVolume":0.1,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
unload_tips({"Module":tips_list_reagent_2[0],"Tips":96,"Col":1,"Row":1})

if shake_choice == 'y':
    for plate in range(int(number_plates)):
        mvkit(cells_list[plate],"POS20")
        shake_on(1000,1)
        dely(3)
        shake_off()
        mvkit("POS20", cells_list[plate])
home()
#workflow block end
