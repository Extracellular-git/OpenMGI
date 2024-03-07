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
        ("POS1","96_wellplate","Source plate 1","",False,True,""),
        ("POS2","96_wellplate","Source plate 2","",False,True,""),
        ("POS3","96_wellplate","Source plate 3","",False,True,""),
        ("POS4","96_wellplate","Source plate 4","",False,True,""),
        ("POS5","TipGEBAF250A","Sample tips plate 1","",False,True,"HigherPosition"),
        ("POS6","TipGEBAF250A","Sample tips plate 2","",False,True,""),
        ("POS7","TipGEBAF250A","Sample tips plate 3","",False,True,""),
        ("POS8","TipGEBAF250A","Sample tips plate 4","",False,True,""),
        ("POS9","VDeepwellPlateDN07350501","Dilution plate 1","",False,True,""),
        ("POS10","VDeepwellPlateDN07350501","Dilution plate 2","",False,True,""),
        ("POS11","VDeepwellPlateDN07350501","Dilution plate 3","",False,True,""),
        ("POS12","VDeepwellPlateDN07350501","Dilution plate 4","",False,True,""),
        ("POS13","96_wellplate","Target plate 1","",False,True,""),
        ("POS14","96_wellplate","Target plate 2","",False,True,""),
        ("POS15","96_wellplate","Target plate 3","",False,True,""),
        ("POS16","96_wellplate","Target plate 4","",False,True,""),
        ("POS17","","","",False,True,""),
        ("POS18","","","",False,True,""),
        ("POS19","","","",False,True,""),
        ("POS20","Teleshake","","",False,True,""),
        ("POS21","Heat block","","",False,True,""),
        ("POS22","TipGEBAF250A","Diluent tips","",False,True,""),
        ("POS23","SuzhouChenxuCAR-190NS","Diluent reservoir","",False,True,""),
        ("POS24","","","",False,True,"Trash")
    ]

binding_map({
    "POS1":["96_wellplate", None, None],
    "POS2":["96_wellplate", None, None],
    "POS3":["96_wellplate", None, None],
    "POS4":["96_wellplate", None, None],
    "POS5":["TipGEBAF250A", None, None],
    "POS6":["TipGEBAF250A", None, None],
    "POS7":["TipGEBAF250A", None, None],
    "POS8":["TipGEBAF250A", None, None],
    "POS9":["VDeepwellPlateDN07350501", None, None],
    "POS10":["VDeepwellPlateDN07350501", None, None],
    "POS11":["VDeepwellPlateDN07350501", None, None],
    "POS12":["VDeepwellPlateDN07350501", None, None],
    "POS13":["96_wellplate", None, None],
    "POS14":["96_wellplate", None, None],
    "POS15":["96_wellplate", None, None],
    "POS16":["96_wellplate", None, None],
    "POS17":["TipGEBAF250A", None, None],
    "POS18":[None, None, None],
    "POS19":[None, None, None],
    "POS20":[None, None, None],
    "POS21":[None, None, None],
    "POS22":["TipGEBAF250A", None, None],
    "POS23":["SuzhouChenxuCAR-190NS", None, None],
    "POS24":[None, None, "trash"]
})

#deck block end
source_plates_list = ["POS1", "POS2", "POS3", "POS4"]
tips_list = ["POS5", "POS6", "POS7", "POS8"]
intermediary_DW_plates_list = ["POS9", "POS10", "POS11", "POS12"]
target_plates_list = ["POS13", "POS14", "POS15", "POS16"]
#workflow block begin
num_plates = 1 #
s_require3_result = require3([],[{"number plates (4 max)":[""]},{"shake choice (y/n)":[""]}, {"Dilution (30, 40, 50, 60 only)":[""]}])
number_plates = int((s_require3_result.Item2[0]))
shake_choice = (s_require3_result.Item2[1])
dilution_choice = str(s_require3_result.Item2[2])

home()
#using fresh tips each time, adding the substance of interest to the dilution plate, then mixing, then adding 50 ul to the target plate

load_tips({"Module":"POS22","Tips":8,"Col":9,"Row":1})

dilution_options = ["30", "40", "50", "60"]
if dilution_choice not in dilution_options:
    raise Exception('dilution options not in the available options {}'.format(dilution_choice))

# using the same tips, dispensing the diluent into all of the plates. This code can now handle diifferent dilution ranges
if dilution_choice == "30":
    for plate in range(number_plates):
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":155,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":145,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":148,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":145,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})

if dilution_choice == "40":
    for plate in range(number_plates):
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":135,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":130,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":135,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":130,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":135,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":130,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})

if dilution_choice == "50":
    for plate in range(number_plates):
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":125,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":122.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":125,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":122.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":125,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":122.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":125,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":122.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})

if dilution_choice == "60":
    for plate in range(number_plates):
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":150,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":35,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":147.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":150,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":147.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":150,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":147.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
        aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":150,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
        dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":147.5,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":40,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
        empty({"Module":"POS23","Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":35,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})

unload_tips({"Module":"POS22","Tips":8,"Col":9,"Row":1})

for plate in range(number_plates):
    load_tips({"Module":tips_list[plate],"Tips":8,"Col":9,"Row":1})
    aspirate({"Module":source_plates_list[plate],"Tips":96,"Col":1,"Row":1,"AspirateVolume":10,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    dispense({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":1,"DispenseRateOfP":250,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    mix({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"SubMixLoopCounts":4,"MixLoopVolume":50,"BottomOffsetOfZ":1,"MixLoopAspirateRate":50,"MixOffsetOfZInLoop":0.5,"MixLoopDispenseRate":50,"MixOffsetOfZAfterLoop":0.5,"DispenseRateAfterSubmixLoop":100,"PreAirVolume":5,"SubMixLoopCompletedDely":0.5,"SecondRouteRate":10,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"MixLoopAspirateDely":0.5,"MixLoopDispenseDely":0.5,"DelyAfterSubmixLoopCompleted":0.5})
    empty({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":10,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    aspirate({"Module":intermediary_DW_plates_list[plate],"Tips":96,"Col":1,"Row":1,"AspirateVolume":30,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    dispense({"Module":target_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":30,"BottomOffsetOfZ":3,"DispenseRateOfP":250,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    
    
    unload_tips({"Module":tips_list[plate],"Tips":8,"Col":9,"Row":1})

if shake_choice == 'y':
    for plate in range(int(number_plates)):
        mvkit(target_plates_list[plate],"POS20")
        shake_on(1000,1)
        dely(3)
        shake_off()
        mvkit("POS20", target_plates_list[plate])

home()
#workflow block end
