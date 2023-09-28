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
        ("POS1","TipGEBAF250A","Tips for Buffer","",False,True,""),
        ("POS2","","","",False,True,""),
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
        ("POS22","VDeepwellPlateDN07350501","Standard curve DW plate","",False,True,""),
        ("POS23","SuzhouChenxuCAR-190NS","Buffer A","",False,True,""),
        ("POS24","","","",False,True,"")
    ]

binding_map({
    "POS1":["TipGEBAF250A", None, None],
    "POS2":["useless", None, None],
    "POS3":["useless", None, None],
    "POS4":["useless", None, None],
    "POS5":["useless", None, None],
    "POS6":["useless", None, None],
    "POS7":["useless", None, None],
    "POS8":["useless", None, None],
    "POS9":["96_wellplate", None, None],
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
    "POS22":["VDeepwellPlateDN07350501", None, None],
    "POS23":["SuzhouChenxuCAR-190NS", None, None],
    "POS24":["SuzhouChenxuCAR-190NS", None, None]
})
#deck block end
#defining the default user inputed variables 
number_plates = 1 #
shake_choice = "n" #
incubation_time = 0 #
#asks the user for the inputs
first_require3_result = require3([],[{"number plates":[""]},{"incubation time (min)":[""]},{"Would you like to shake after assay? (y/n)":["y", "n"]}])
#indexes the provided user inputs and converts data type as appropriate
number_plates = int(first_require3_result.Item2[0])
incubation_time = int(first_require3_result.Item2[1])
shake_choice = first_require3_result.Item2[2]
# second set of questions
col_question = require3([],[{"How many columns from left for standard curve?":[3,""]},{"How many empty columns on right?":[0, ""]}])
std_col = int(col_question.Item2[0])
emp_col = int(col_question.Item2[1])
#Turns minutes into seconds
incubation_time = incubation_time*60

#defining the different iterable parameters required for the assay
#Where the tips for the diluent are stored
tips_list_reagent_1 = ["POS1"]

# The columns of the plate in which the standard curve are dispensed
target_standard_curve_column_list = list(range(1, std_col + 1))
# List of positions in which the plates are placed (8 total)
cells_list =["POS9", "POS10", "POS11", "POS12", "POS13", "POS14", "POS15", "POS16"]
#workflow block begins
home()
#This block of code loads standard curves to the plates
# Load tips from the tips position 
load_tips({"Module":"POS17","Tips":8,"Col":1,"Row":1})
#If there are 4 or fewer plates, all of the standards can be dispensed from the same aspiration event
if number_plates <= 4:   
    #calculates how much aspiration volume is needed. There is 30 ul per plate, plus 10 ul excess
    aspiration_volume = (number_plates * 30) + 10
    aspirate({"Module":"POS22","Tips":8,"Col":1,"Row":1,"AspirateVolume":aspiration_volume,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    for plate in range(number_plates):
        for col in target_standard_curve_column_list:
            dispense({"Module":cells_list[plate],"Tips":8,"Col":col,"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
            #unload tips without emptying as emptying is not necessary here
    unload_tips({"Module":"POS19","Tips":8,"Col":6,"Row":1})

#if there are more than 4 plates, then 2 aspiration events are required to cover all the plates
if number_plates > 4:
    #this is the first aspiration for 4 plates, 120 + 10 excess
    aspiration_volume = 130
    aspirate({"Module":"POS22","Tips":8,"Col":1,"Row":1,"AspirateVolume":aspiration_volume,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})

    for plate in range(4):
        dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[0],"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[1],"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[2],"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    #need to empty in the event of more than one aspiration event, to allow reuse of the tips
    empty({"Module":"POS22","Tips":8,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
    #the maths to calculate what remaining volume is required, with the previously aliquoted 4 plates taken off
    aspiration_volume = ((number_plates-4) * 30) + 10
    aspirate({"Module":"POS22","Tips":8,"Col":1,"Row":1,"AspirateVolume":aspiration_volume,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})

    for plate in range(number_plates-4):
        #given that 4 plates will have already been completed, this index begins +4 to account for this
        plate = plate + 4
        dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[0],"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[1],"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        dispense({"Module":cells_list[plate],"Tips":8,"Col":target_standard_curve_column_list[2],"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    unload_tips({"Module":"POS19","Tips":8,"Col":6,"Row":1})

# Adding assay buffer
# To account for empty cols on the right, we need to adjust the load tips col.
offset_col = 1 + emp_col
load_tips({"Module":tips_list_reagent_1[0],"Tips":96,"Col":offset_col,"Row":1})  
for plate in range(int(number_plates)):
    aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":130,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
    dispense({"Module":cells_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":125,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    #Reusing tips so need to empty between uses, changed dispense rate from 100 to 1000 for all empty events for more complete residue clearance
    empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":False,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
    
unload_tips({"Module":tips_list_reagent_1[0],"Tips":96,"Col":offset_col,"Row":1})
    
#waiting for the incubation time as defined by the user
dely(incubation_time)

#if the user has decided to shake the plates at the end, there is the option here
if shake_choice == 'y':
    for plate in range(int(number_plates)):
        mvkit(cells_list[plate],"POS20")
        shake_on(1000,1)
        dely(3)
        shake_off()
        mvkit("POS20", cells_list[plate])
home()
#workflow block end
