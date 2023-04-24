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
        ("POS5","96_wellplate","Source plate 5","",False,True,"HigherPosition"),
        ("POS6","96_wellplate","Source plate 6","",False,True,""),
        ("POS7","TipGEBAF250A","Sample tips plate 1","",False,True,""),
        ("POS8","TipGEBAF250A","Sample tips plate 2","",False,True,""),
        ("POS9","TipGEBAF250A","Sample tips plate 3","",False,True,""),
        ("POS10","TipGEBAF250A","Sample tips plate 4","",False,True,""),
        ("POS11","TipGEBAF250A","Sample tips plate 5","",False,True,""),
        ("POS12","TipGEBAF250A","Sample tips plate 6","",False,True,""),
        ("POS13","96_wellplate","Target plate 1","",False,True,""),
        ("POS14","96_wellplate","Target plate 2","",False,True,""),
        ("POS15","96_wellplate","Target plate 3","",False,True,""),
        ("POS16","96_wellplate","Target plate 4","",False,True,""),
        ("POS17","96_wellplate","Target plate 5","",False,True,""),
        ("POS18","","","",False,True,"Trash"),
        ("POS19","","","",False,True,""),
        ("POS20","Teleshake","","",False,True,""),
        ("POS21","Heat block","","",False,True,""),
        ("POS22","TipGEBAF250A","Diluent tips","",False,True,""),
        ("POS23","SuzhouChenxuCAR-190NS","Diluent reservoir","",False,True,""),
        ("POS24","96_wellplate","Target plate 6","",False,True,"")
    ]

binding_map({
    "POS1":["96_wellplate", None, None],
    "POS2":["96_wellplate", None, None],
    "POS3":["96_wellplate", None, None],
    "POS4":["96_wellplate", None, None],
    "POS5":["96_wellplate", None, None],
    "POS6":["96_wellplate", None, None],
    "POS7":["TipGEBAF250A", None, None],
    "POS8":["TipGEBAF250A", None, None],
    "POS9":["TipGEBAF250A", None, None],
    "POS10":["TipGEBAF250A", None, None],
    "POS11":["TipGEBAF250A", None, None],
    "POS12":["TipGEBAF250A", None, None],
    "POS13":["96_wellplate", None, None],
    "POS14":["96_wellplate", None, None],
    "POS15":["96_wellplate", None, None],
    "POS16":["96_wellplate", None, None],
    "POS17":["96_wellplate", None, None],
    "POS18":["96_wellplate", None, None],
    "POS19":[None, None, None],
    "POS20":[None, None, None],
    "POS21":[None, None, None],
    "POS22":["TipGEBAF250A", None, None],
    "POS23":["SuzhouChenxuCAR-190NS", None, None],
    "POS24":["96_wellplate", None, "trash"]
})
#deck block end

# The source plate positions containing 25 ul of lysate
source_plates_list = ["POS1", "POS2", "POS3", "POS4", "POS5", "POS6"]
# Tip positions for the liquid handling
tips_list = ["POS7", "POS8", "POS9", "POS10", "POS11", "POS12"]
# The target plate positions (plates to have the assay applied to them)
target_plates_list = ["POS13", "POS14", "POS15", "POS16", "POS17", "POS24"]

#Takes user unput and as appropriate converts to the relevent data type
num_plates = 1 #
s_require3_result = require3([],[{"number plates":[""]},{"shake choice (y/n)":[""]}])
number_plates = int((s_require3_result.Item2[0]))
shake_choice = (s_require3_result.Item2[1])

#workflow block begin
home()
#ASSUMING STARTING WITH 25 UL OF CELL LYSATE
#Loading the tips for diluting
load_tips({"Module":"POS22","Tips":8,"Col":9,"Row":1})
#Calculating the aspiration volume of the diluent depending on the number of plates, plus 5 ul excess
aspirate_vol = (number_plates*25) +5 
# Aspirating the required volume
aspirate({"Module":"POS23","Tips":96,"Col":1,"Row":1,"AspirateVolume":aspirate_vol,"BottomOffsetOfZ":1,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":0.5,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
#Dispensing 25 ul of diluent to every lysate plate to achieve a 1 in 2 dilution
for plate in range(number_plates):
    dispense({"Module":source_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":25,"BottomOffsetOfZ":10,"DispenseRateOfP":100,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
unload_tips({"Module":"POS22","Tips":8,"Col":9,"Row":1})
#taking 40 ul from source plate to the target plate
for plate in range(number_plates):
    load_tips({"Module":tips_list[plate],"Tips":8,"Col":9,"Row":1})
    aspirate({"Module":source_plates_list[plate],"Tips":96,"Col":1,"Row":1,"AspirateVolume":10,"BottomOffsetOfZ":0.5,"AspirateRateOfP":100,"PreAirVolume":5,"PostAirVolume":0,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10})
    dispense({"Module":target_plates_list[plate],"Tips":96,"Col":1,"Row":1,"DispenseVolume":10,"BottomOffsetOfZ":1,"DispenseRateOfP":250,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"SecondRouteRate":10,"EmptyForDispense":False,"EmptyForDispenseOffsetOfZ":10,"EmptyForDispenseDely":0.5})
    #have added mixing step here as there were concerns that the solution is not being mixed well. With a 25 ul volume of mixture
    mix({"Module":target_plates_list[plate],"Tips":96,"Col":1,"Row":1,"SubMixLoopCounts":4,"MixLoopVolume":25,"BottomOffsetOfZ":1,"MixLoopAspirateRate":50,"MixOffsetOfZInLoop":0.5,"MixLoopDispenseRate":50,"MixOffsetOfZAfterLoop":0.5,"DispenseRateAfterSubmixLoop":100,"PreAirVolume":5,"SubMixLoopCompletedDely":0.5,"SecondRouteRate":10,"IfTipTouch":True,"TipTouchHeight":10,"TipTouchOffsetOfX":3,"MixLoopAspirateDely":0.5,"MixLoopDispenseDely":0.5,"DelyAfterSubmixLoopCompleted":0.5})
    empty({"Module":target_plates_list[plate],"Tips":96,"Col":1,"Row":1,"BottomOffsetOfZ":10,"DispenseRateOfP":1000,"DelySeconds":0.5,"IfTipTouch":True,"TipTouchHeight":1,"TipTouchOffsetOfX":5,"SecondRouteRate":10})
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
