# -*- coding: utf-8 -*-
# head block begin
spx96 = globals().get("Spx96")
from spredo import *

# init,most important
init(spx96)
# head block end

# deck block begin


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
        ("POS1", "TipGEBAF250A", "TrypLE tips", "", False, True, ""),
        ("POS2", "TipGEBAF250A", "PBS plate wash tips", "", False, True, ""),
        ("POS3", "", "free", "", False, True, ""),
        ("POS4", "", "free", "", False, True, ""),
        ("POS5", "TipGEBAF250A", "Inoculation tip 1", "", False, True, ""),
        ("POS6", "TipGEBAF250A", "Inoculation tip 2", "", False, True, ""),
        ("POS7", "TipGEBAF250A", "Inoculation tip 3", "", False, True, ""),
        ("POS8", "TipGEBAF250A", "Inoculation tip 4", "", False, True, ""),
        ("POS9", "96_wellplate_flat_bottom", "New plate 1", "", False, True, ""),
        ("POS10", "96_wellplate_flat_bottom", "New plate 2", "", False, True, ""),
        ("POS11", "96_wellplate_flat_bottom", "New plate 3", "", False, True, ""),
        ("POS12", "96_wellplate_flat_bottom", "New plate 4", "", False, True, ""),
        ("POS13", "96_wellplate_flat_bottom", "Old plate 1", "", False, True, ""),
        ("POS14", "96_wellplate_flat_bottom", "Old plate 2", "", False, True, ""),
        ("POS15", "96_wellplate_flat_bottom", "Old plate 3", "", False, True, ""),
        ("POS16", "96_wellplate_flat_bottom", "Old plate 4", "", False, True, ""),
        (
            "POS17",
            "TipGEBAF250A",
            "New media tips",
            "",
            False,
            True,
            "",
        ),
        (
            "POS18",
            "SuzhouChenxuCAR-190NS",
            "PBS tip wash reservoir",
            "",
            False,
            True,
            "Magnet",
        ),
        ("POS19", "SuzhouChenxuCAR-190NS", "WASTE", "", False, True, ""),
        ("POS20", "", "Teleshake", "", False, True, "Shaker"),
        (
            "POS21",
            "SuzhouChenxuCAR-190NS",
            "PBS plate wash reservoir",
            "",
            False,
            True,
            "Temp",
        ),
        ("POS22", "TipGEBAF250A", "Old media tips", "", False, True, ""),
        ("POS23", "SuzhouChenxuCAR-190NS", "TrypLE reservoir", "", False, True, ""),
        (
            "POS24",
            "SuzhouChenxuCAR-190NS",
            "Fresh media reservoir",
            "",
            False,
            True,
            "",
        ),
    ]


binding_map(
    {
        "POS1": ["TipGEBAF250A", None, None],
        "POS2": ["TipGEBAF250A", None, None],
        "POS3": [None, None, None],
        "POS4": [None, None, None],
        "POS5": ["TipGEBAF250A", None, None],
        "POS6": ["TipGEBAF250A", None, None],
        "POS7": ["TipGEBAF250A", None, None],
        "POS8": ["TipGEBAF250A", None, None],
        "POS9": ["96_wellplate_flat_bottom", None, None],
        "POS10": ["96_wellplate_flat_bottom", None, None],
        "POS11": ["96_wellplate_flat_bottom", None, None],
        "POS12": ["96_wellplate_flat_bottom", None, None],
        "POS13": ["96_wellplate_flat_bottom", None, None],
        "POS14": ["96_wellplate_flat_bottom", None, None],
        "POS15": ["96_wellplate_flat_bottom", None, None],
        "POS16": ["96_wellplate_flat_bottom", None, None],
        "POS17": ["TipGEBAF250A", None, None],
        "POS18": ["SuzhouChenxuCAR-190NS", None, None],
        "POS19": ["SuzhouChenxuCAR-190NS", None, None],
        "POS20": [None, None, "shake"],
        "POS21": ["SuzhouChenxuCAR-190NS", None, None],
        "POS22": ["TipGEBAF250A", None, None],
        "POS23": ["SuzhouChenxuCAR-190NS", None, None],
        "POS24": ["SuzhouChenxuCAR-190NS", None, None],
    }
)
# deck block end
# constants
waste = "POS19"
waste_height_offset = 30
waste_touch_offset = 6
shake = "POS20"
pbs_plate_wash = "POS18"
pbs_tip_wash = "POS21"
old_media_tips = "POS22"
tryple_tips = "POS1"
tryple_res = "POS23"
pbs_plate_wash_tips = "POS2"
pbs_wash_cycle = 2
new_media_res = "POS24"
# defining the default user input variables
plate_type = "96_wellplate_flat_bottom"
number_plates = 1
out_media_vol = 180
new_media_vol = 180
inoc_vol = 180
aspirate_z_offset = 0.4
aspirate_speed = 60
# asks the user for the inputs
s_require3_result = require3(
    [{"Select plate type": ["96_wellplate_flat_bottom", "96_wellplate_u_bottom"]}],
    [
        {"Number of plates": ["1", "Integer between 1-4"]},
        {"Volume of media to remove": ["200", "Integer between 0-300"]},
        {"Volume of fresh media": ["180", "Integer between 0-300"]},
        {"Volume to inoculate": ["20", "Integer between 0-175"]},
        {"Aspiration height offset": ["0.4", "mm of height offset, between 0-10"]},
        {"Aspiration speed": ["60", "Rate of aspiration, 0-100"]},
    ],
)
# indexes the provided user inputs and converts data type as appropriate
plate_type = s_require3_result.Item1[0]
number_plates = min(int(s_require3_result.Item2[0]), 4)
out_media_vol = min(int(s_require3_result.Item2[1]), 300)
new_media_vol = min(int(s_require3_result.Item2[2]), 300)
inoc_vol = min(int(s_require3_result.Item2[3]), 175)
aspirate_z_offset = min(float(s_require3_result.Item2[4]), 10)
aspirate_speed = min(int(s_require3_result.Item2[5]), 100)
old_plates_list = ["POS13", "POS14", "POS15", "POS16"][0:number_plates]

report("PBS plate wash", "Start")
load_tips({"Module": pbs_plate_wash_tips, "Tips": 96, "Col": 1, "Row": 1})
if number_plates >= 4:
    repeat = 2
    old_plates_list_wash = [old_plates_list[0:2], old_plates_list[2:4]]
else:
    repeat = 1
    old_plates_list_wash = [old_plates_list]
pbs_aspirate_vol = 50 * number_plates / repeat
for cycle in range(pbs_wash_cycle):
    report("PBS plate wash Cycle " + str(cycle + 1), "Start")
    for plate_group in range(repeat):
        report("PBS plate wash Cycle " + str(cycle + 1), "Aspirate PBS")
        aspirate(
            {
                "Module": pbs_plate_wash,
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "AspirateVolume": pbs_aspirate_vol,
                "BottomOffsetOfZ": 5,
                "AspirateRateOfP": 100,
                "PreAirVolume": 0,
                "PostAirVolume": 0,
                "DelySeconds": 0,
                "IfTipTouch": False,
                "SecondRouteRate": 35,
            }
        )
        for plate in old_plates_list_wash[plate_group]:
            report(
                "PBS plate wash Cycle " + str(cycle + 1),
                "Dispense PBS into plate "
                + str(plate)
                + ", Plate group "
                + str(plate_group + 1),
            )
            dispense(
                {
                    "Module": plate,
                    "Tips": 96,
                    "Col": 1,
                    "Row": 1,
                    "DispenseVolume": 50,
                    "BottomOffsetOfZ": 10,
                    "DispenseRateOfP": 60,
                    "DelySeconds": 0,
                    "IfTipTouch": True,
                    "TipTouchHeight": 10,
                    "TipTouchOffsetOfX": 3,
                    "SecondRouteRate": 35,
                }
            )
    unload_tips({"Module": pbs_plate_wash_tips, "Tips": 96, "Col": 1, "Row": 1})
    for plate in old_plates_list:
        report("PBS plate wash Cycle " + str(cycle + 1), "Shake plate " + str(plate))
        mvkit(plate, shake)
        shake_on(200, 2)
        dely(10)
        shake_off()
        mvkit(shake, plate)
    load_tips({"Module": pbs_plate_wash_tips, "Tips": 96, "Col": 1, "Row": 1})
    for plate in old_plates_list:
        report("PBS plate wash Cycle " + str(cycle + 1), "Aspirate PBS plate " + plate)
        aspirate(
            {
                "Module": plate,
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "AspirateVolume": 60,
                "BottomOffsetOfZ": aspirate_z_offset,
                "AspirateRateOfP": aspirate_speed,
                "PreAirVolume": 0,
                "PostAirVolume": 0,
                "DelySeconds": 0,
                "IfTipTouch": False,
                "TipTouchHeight": 10,
                "TipTouchOffsetOfX": 3,
                "SecondRouteRate": 35,
            }
        )
        empty(
            {
                "Module": waste,
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "BottomOffsetOfZ": waste_height_offset,
                "DispenseRateOfP": 100,
                "DelySeconds": 0,
                "IfTipTouch": True,
                "TipTouchHeight": waste_height_offset,
                "TipTouchOffsetOfX": waste_touch_offset,
                "SecondRouteRate": 35,
            }
        )
unload_tips({"Module": pbs_plate_wash_tips, "Tips": 96, "Col": 1, "Row": 1})
report("PBS plate wash", "End")
