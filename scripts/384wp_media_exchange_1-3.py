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
        ("POS1", "TipMGIAFT70", "Removal tip 1", "", False, True, ""),
        ("POS2", "TipMGIAFT70", "Removal tip 2", "", False, True, ""),
        ("POS3", "TipMGIAFT70", "Removal tip 3", "", False, True, ""),
        ("POS4", "TipMGIAFT70", "Addition tip 1", "", False, True, ""),
        ("POS5", "phenoplate_384_ula", "", "", False, True, ""),
        ("POS6", "phenoplate_384_ula", "", "", False, True, ""),
        ("POS7", "phenoplate_384_ula", "", "", False, True, ""),
        ("POS8", "", "", "", False, True, ""),
        ("POS9", "", "", "", False, True, ""),
        ("POS10", "", "", "", False, True, ""),
        ("POS11", "", "", "", False, True, ""),
        ("POS12", "", "", "", False, True, ""),
        ("POS13", "reservoir", "Fresh media", "", False, True, ""),
        ("POS14", "", "", "", False, True, ""),
        ("POS15", "", "", "", False, True, ""),
        ("POS16", "reservoir", "Waste media", "", False, True, ""),
        ("POS17", "", "", "", False, True, ""),
        ("POS18", "", "", "", False, True, "Magnet"),
        ("POS19", "", "", "", False, True, "Magnet"),
        ("POS20", "", "", "", False, True, "Shaker"),
        ("POS21", "", "", "", False, True, "Temp"),
        ("POS22", "", "", "", False, True, ""),
        ("POS23", "", "", "", False, True, ""),
        ("POS24", "", "", "", False, True, ""),
    ]


binding_map(
    {
        "POS1": ["TipMGIAFT70", None, None],
        "POS2": ["TipMGIAFT70", None, None],
        "POS3": ["TipMGIAFT70", None, None],
        "POS4": ["TipMGIAFT70", None, None],
        "POS5": ["phenoplate_384_ula", None, None],
        "POS6": ["phenoplate_384_ula", None, None],
        "POS7": ["phenoplate_384_ula", None, None],
        "POS8": [None, None, None],
        "POS9": [None, None, None],
        "POS10": [None, None, None],
        "POS11": [None, None, None],
        "POS12": [None, None, None],
        "POS13": ["reservoir", None, None],
        "POS14": [None, None, None],
        "POS15": [None, None, None],
        "POS16": ["reservoir", None, None],
        "POS17": [None, None, None],
        "POS18": [None, None, None],
        "POS19": [None, None, None],
        "POS20": [None, None, "shake"],
        "POS21": [None, None, None],
        "POS22": [None, None, None],
        "POS23": [None, None, None],
        "POS24": [None, None, None],
    }
)


# deck block end

# workflow block begin
num_plates = 1  # Number of plates, max 3
aspiration_volume = 20  # Vol to remove from plates
new_media_volume = 20  # Vol to add
new_media_pos = "POS13"
new_media_tips = "POS4"
waste_pos = "POS16"  # position of waste reservoir
waste_empty_height = 15
waste_tips_list = ["POS1", "POS2", "POS3"]
aspirate_height = 5.5  # height in mm to aspirate old media ouf plate
aspirate_rate = 5  # aspiration rate for old media
second_route_rate = 70
plates_list = ["POS5", "POS6", "POS7"]
media_add_height = 10
initialize()

s_require3_result = require3(
    [],
    [
        {"Number of plates": ["1", "Integer between 1-3"]},
        {"Volume of media to remove": ["20", "Integer between 0-80 (uL)"]},
        {"Volume of media to add": ["20", "Integer between 0-80 (uL)"]},
    ],
)
num_plates = min(int(s_require3_result.Item2[0]), 3)
aspiration_volume = min(float(s_require3_result.Item2[1]), 80)
new_media_volume = min(float(s_require3_result.Item2[2]), 80)

use_plates_list = plates_list[0:num_plates]

report("Removal of old media", "Start")
for idx, plate in enumerate(use_plates_list):
    report("Removal of old media", "Load tips for plate" + str(idx+1))
    load_tips({"Module": waste_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})
    s_avoidBodyEmpty = 1
    for row in [1, 2]:
        for col in [1, 2]:
            report("Removal of old media", "Plate " + str(idx+1) + ", Row: " + str(row) + ", Col: " + str(col))
            aspirate(
                {
                    "Module": plate,
                    "Tips": 96,
                    "Col": col,
                    "Row": row,
                    "AspirateVolume": aspiration_volume,
                    "BottomOffsetOfZ": aspirate_height,
                    "AspirateRateOfP": aspirate_rate,
                    "PreAirVolume": 0,
                    "PostAirVolume": 0,
                    "DelySeconds": 0,
                    "IfTipTouch": False,
                    "TipTouchHeight": 20,
                    "TipTouchOffsetOfX": 0,
                    "SecondRouteRate": second_route_rate,
                }
            )
            # intentionally not dispensing all waste, it would cause droplets.
            # remaining waste will be discarded inside the tip.
            dispense(
                {
                    "Module": waste_pos,
                    "Tips": 96,
                    "Col": 1,
                    "Row": 1,
                    "DispenseVolume": 18,
                    "BottomOffsetOfZ": waste_empty_height,
                    "DispenseRateOfP": 100,
                    "DelySeconds": 0,
                    "IfTipTouch": False,
                    "TipTouchHeight": 20,
                    "TipTouchOffsetOfX": 0,
                    "SecondRouteRate": second_route_rate,
                }
            )
    report("Removal of old media", "Unload tips for plate" + str(idx+1))
    unload_tips({"Module": waste_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})

report("Removal of old media", "End")

report("Addition of fresh media", "Start")
report("Addition of fresh media", "Load tips")
load_tips({"Module": new_media_tips, "Tips": 96, "Col": 1, "Row": 1})
for idx, plate in enumerate(use_plates_list):
    s_avoidBodyEmpty = 1
    report("Addition of fresh media", "Plate " + str(idx+1))
    for row in [1, 2]:
        for col in [1, 2]:
            aspirate(
                {
                    "Module": new_media_pos,
                    "Tips": 96,
                    "Col": 1,
                    "Row": 1,
                    "AspirateVolume": new_media_volume,
                    "BottomOffsetOfZ": 1,
                    "AspirateRateOfP": 20,
                    "PreAirVolume": 0,
                    "PostAirVolume": 0,
                    "DelySeconds": 0,
                    "IfTipTouch": False,
                    "TipTouchHeight": 20,
                    "TipTouchOffsetOfX": 0,
                    "SecondRouteRate": second_route_rate,
                }
            )
            report("Addition of fresh media", "Plate " + str(idx+1) + ", Row: " + str(row) + ", Col: " + str(col))
            empty(
                {
                    "Module": plate,
                    "Tips": 96,
                    "Col": col,
                    "Row": row,
                    "BottomOffsetOfZ": media_add_height,
                    "DispenseRateOfP": 60,
                    "DelySeconds": 0,
                    "IfTipTouch": True,
                    "TipTouchHeight": 10,
                    "TipTouchOffsetOfX": 2,
                    "SecondRouteRate": second_route_rate,
                }
            )
report("Addition of fresh media", "Unload tips")
unload_tips({"Module": new_media_tips, "Tips": 96, "Col": 1, "Row": 1})
home()
# workflow block end
