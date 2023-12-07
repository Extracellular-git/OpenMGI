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
        ("POS1", "TipGEBAF250A", "Tips for spent media 1", "", False, True, ""),
        ("POS2", "TipGEBAF250A", "Tips for spent media 2", "", False, True, ""),
        ("POS3", "TipGEBAF250A", "Tips for spent media 3", "", False, True, ""),
        ("POS4", "TipGEBAF250A", "Tips for spent media 4", "", False, True, ""),
        ("POS5", "TipGEBAF250A", "Tips for spent media 5", "", False, True, ""),
        ("POS6", "TipGEBAF250A", "Tips for spent media 6", "", False, True, ""),
        ("POS7", "TipGEBAF250A", "Tips for spent media 7", "", False, True, ""),
        ("POS8", "TipGEBAF250A", "Tips for spent media 8", "", False, True, ""),
        ("POS9", "96_wellplate_flat_bottom", "Cell plate 1", "", False, True, ""),
        ("POS10", "96_wellplate_flat_bottom", "Cell plate 2", "", False, True, ""),
        ("POS11", "96_wellplate_flat_bottom", "Cell plate 3", "", False, True, ""),
        ("POS12", "96_wellplate_flat_bottom", "Cell plate 4", "", False, True, ""),
        ("POS13", "96_wellplate_flat_bottom", "Cell plate 5", "", False, True, ""),
        ("POS14", "96_wellplate_flat_bottom", "Cell plate 6", "", False, True, ""),
        ("POS15", "96_wellplate_flat_bottom", "Cell plate 7", "", False, True, ""),
        ("POS16", "96_wellplate_flat_bottom", "Cell plate 8", "", False, True, ""),
        (
            "POS17",
            "SuzhouChenxuCAR-190NS",
            "Spent media reservoir",
            "",
            False,
            True,
            "",
        ),
        ("POS18", "", "", "", False, True, "Magnet"),
        ("POS19", "TipGEBAF250A", "Waste", "", False, True, ""),
        ("POS20", "", "Teleshake", "", False, True, "Shaker"),
        ("POS21", "", "Heat block", "", False, True, "Temp"),
        ("POS22", "TipGEBAF250A", "Tips for new media", "", False, True, ""),
        ("POS23", "SuzhouChenxuCAR-190NS", "New media reservoir", "", False, True, ""),
        ("POS24", "", "", "", False, True, ""),
    ]


binding_map(
    {
        "POS1": ["TipGEBAF250A", None, None],
        "POS2": ["TipGEBAF250A", None, None],
        "POS3": ["TipGEBAF250A", None, None],
        "POS4": ["TipGEBAF250A", None, None],
        "POS5": ["TipGEBAF250A", None, None],
        "POS6": ["TipGEBAF250A", None, None],
        "POS7": ["TipGEBAF250A", None, None],
        "POS8": ["TipGEBAF250A", None, None],
        "POS9": ["96_wellplate_u_bottom", None, None],
        "POS10": ["96_wellplate_u_bottom", None, None],
        "POS11": ["96_wellplate_u_bottom", None, None],
        "POS12": ["96_wellplate_u_bottom", None, None],
        "POS13": ["96_wellplate_u_bottom", None, None],
        "POS14": ["96_wellplate_u_bottom", None, None],
        "POS15": ["96_wellplate_u_bottom", None, None],
        "POS16": ["96_wellplate_u_bottom", None, None],
        "POS17": ["SuzhouChenxuCAR-190NS", None, None],
        "POS18": [None, None, None],
        "POS19": ["TipGEBAF250A", None, None],
        "POS20": [None, None, "shake"],
        "POS21": [None, None, None],
        "POS22": ["TipGEBAF250A", None, None],
        "POS23": ["SuzhouChenxuCAR-190NS", None, None],
        "POS24": [None, None, None],
    }
)
# deck block end
# define constants
new_media_tips = "POS22"
new_media_res = "POS23"
old_media_res = "POS17"
# defining the default user inputed variables
number_plates = 1
in_media_vol = 180
aspirate_z_offset = 0.4
plate_type = "96_wellplate_flat_bottom"
# asks the user for the inputs
s_require3_result = require3(
    [{"Select plate type": ["96_wellplate_flat_bottom", "96_wellplate_u_bottom"]}],
    [
        {"Number of plates": ["1", "Integer between 1-8"]},
        {"Volume of media to remove": ["200", "Integer between 0-300"]},
        {"Volume of fresh media": ["180", "Integer between 0-300"]},
    ],
)
# indexes the provided user inputs and converts data type as appropriate
plate_type = s_require3_result.Item1[0]
number_plates = min(int(s_require3_result.Item2[0]), 8)
out_media_vol = min(int(s_require3_result.Item2[1]), 300)
in_media_vol = min(int(s_require3_result.Item2[2]), 300)

update_feature(
    [
        ("POS1", "TipGEBAF250A", "Tips for spent media 1", "", False, True, ""),
        ("POS2", "TipGEBAF250A", "Tips for spent media 2", "", False, True, ""),
        ("POS3", "TipGEBAF250A", "Tips for spent media 3", "", False, True, ""),
        ("POS4", "TipGEBAF250A", "Tips for spent media 4", "", False, True, ""),
        ("POS5", "TipGEBAF250A", "Tips for spent media 5", "", False, True, ""),
        ("POS6", "TipGEBAF250A", "Tips for spent media 6", "", False, True, ""),
        ("POS7", "TipGEBAF250A", "Tips for spent media 7", "", False, True, ""),
        ("POS8", "TipGEBAF250A", "Tips for spent media 8", "", False, True, ""),
        ("POS9", "96_wellplate_flat_bottom", "Cell plate 1", "", False, True, ""),
        ("POS10", "96_wellplate_flat_bottom", "Cell plate 2", "", False, True, ""),
        ("POS11", "96_wellplate_flat_bottom", "Cell plate 3", "", False, True, ""),
        ("POS12", "96_wellplate_flat_bottom", "Cell plate 4", "", False, True, ""),
        ("POS13", "96_wellplate_flat_bottom", "Cell plate 5", "", False, True, ""),
        ("POS14", "96_wellplate_flat_bottom", "Cell plate 6", "", False, True, ""),
        ("POS15", "96_wellplate_flat_bottom", "Cell plate 7", "", False, True, ""),
        ("POS16", "96_wellplate_flat_bottom", "Cell plate 8", "", False, True, ""),
        (
            "POS17",
            "SuzhouChenxuCAR-190NS",
            "Spent media reservoir",
            "",
            False,
            True,
            "",
        ),
        Aspirate("POS18", "", "", "", False, True, "Magnet"),
        ("POS19", "TipGEBAF250A", "Waste", "", False, True, ""),
        ("POS20", "", "Teleshake", "", False, True, "Shaker"),
        ("POS21", "", "Heat block", "", False, True, "Temp"),
        ("POS22", "TipGEBAF250A", "Tips for new media", "", False, True, ""),
        ("POS23", "SuzhouChenxuCAR-190NS", "New media reservoir", "", False, True, ""),
        ("POS24", "", "", "", False, True, ""),
    ]
)

binding_map(
    {
        "POS1": ["TipGEBAF250A", None, None],
        "POS2": ["TipGEBAF250A", None, None],
        "POS3": ["TipGEBAF250A", None, None],
        "POS4": ["TipGEBAF250A", None, None],
        "POS5": ["TipGEBAF250A", None, None],
        "POS6": ["TipGEBAF250A", None, None],
        "POS7": ["TipGEBAF250A", None, None],
        "POS8": ["TipGEBAF250A", None, None],
        "POS9": [plate_type, None, None],
        "POS10": [plate_type, None, None],
        "POS11": [plate_type, None, None],
        "POS12": [plate_type, None, None],
        "POS13": [plate_type, None, None],
        "POS14": [plate_type, None, None],
        "POS15": [plate_type, None, None],
        "POS16": [plate_type, None, None],
        "POS17": ["SuzhouChenxuCAR-190NS", None, None],
        "POS18": [None, None, None],
        "POS19": ["TipGEBAF250A", None, None],
        "POS20": [None, None, "shake"],
        "POS21": [None, None, None],
        "POS22": ["TipGEBAF250A", None, None],
        "POS23": ["SuzhouChenxuCAR-190NS", None, None],
        "POS24": [None, None, None],
    }
)

# defining the different iterable parameters required for the assay
# Where the tips for the transfers are stored
tips_list = ["POS1", "POS2", "POS3", "POS4", "POS5", "POS6", "POS7", "POS8"]
use_tips_list = tips_list[0:number_plates]
# List of positions in which the plates are placed (8 total)
plates_list = ["POS9", "POS10", "POS11", "POS12", "POS13", "POS14", "POS15", "POS16"]
use_plates_list = plates_list[0:number_plates]
# workflow block begins
lock()
home()
# Remove media from each plate in use with new tips each time.
report("Removal of old media", "Start")
for idx, plate_pos in enumerate(use_plates_list):
    report("Removal of old media", "Load tips " + str(idx))
    load_tips({"Module": use_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})
    if out_media_vol > 175:
        # have to do more than one pipetting motion
        repeat = 2
    else:
        repeat = 1
    for cycle in range(repeat):
        report(
            "Removal of old media",
            "Aspirating plate " + str(idx + 1) + ", cycle: " + str(cycle + 1),
        )
        aspirate(
            {
                "Module": plate_pos,
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "AspirateVolume": out_media_vol / repeat,
                "BottomOffsetOfZ": aspirate_z_offset,
                "AspirateRateOfP": 100,
                "PreAirVolume": 0,
                "PostAirVolume": 0,
                "DelySeconds": 0,
                "IfTipTouch": False,
                "TipTouchHeight": 10,
                "TipTouchOffsetOfX": 3,
                "SecondRouteRate": 35,
            }
        )
        if cycle == 1:
            # do not empty all liquid if not last operation to stop droplets forming.
            report("Removal of old media", "Dispensing media")
            dispense(
                {
                    "Module": old_media_res,
                    "Tips": 96,
                    "Col": 1,
                    "Row": 1,
                    "DispenseVolume": (out_media_vol / repeat) - 10,
                    "BottomOffsetOfZ": 35,
                    "DispenseRateOfP": 100,
                    "DelySeconds": 0,
                    "IfTipTouch": False,
                    "TipTouchHeight": 1,
                    "TipTouchOffsetOfX": 5,
                    "SecondRouteRate": 35,
                }
            )
        else:
            # Can touch liquid to get rid of drops since it is last operation
            report("Removal of old media", "Emptying excess")
            empty(
                {
                    "Module": old_media_res,
                    "Tips": 96,
                    "Col": 1,
                    "Row": 1,
                    "BottomOffsetOfZ": 4,
                    "DispenseRateOfP": 100,
                    "DelySeconds": 0,
                    "IfTipTouch": False,
                    "TipTouchHeight": 30,
                    "TipTouchOffsetOfX": 4,
                    "SecondRouteRate": 35,
                }
            )
    unload_tips({"Module": use_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})
    report("Removal of old media", "End")
report("Addition of new media", "Start")
load_tips({"Module": new_media_tips, "Tips": 96, "Col": 1, "Row": 1})
if in_media_vol > 175:
    repeat = 2
else:
    repeat = 1
for idx, plate_pos in enumerate(use_plates_list):
    for cycle in range(repeat):
        report(
            "Addition of new media",
            "Aspirating new media for plate "
            + str(idx + 1)
            + ", cycle: "
            + str(cycle + 1),
        )
        # Load fresh media, use reverse pipetting
        aspirate(
            {
                "Module": new_media_res,
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "AspirateVolume": (in_media_vol / repeat) + 10,
                "BottomOffsetOfZ": 1,
                "AspirateRateOfP": 60,
                "PreAirVolume": 0,
                "PostAirVolume": 0,
                "DelySeconds": 0,
                "IfTipTouch": False,
                "TipTouchHeight": 10,
                "TipTouchOffsetOfX": 3,
                "SecondRouteRate": 35,
            }
        )
        # Dispense fresh media into plate. do not touch the bottom, and do it slowly.
        report(
            "Addition of new media",
            "Dispensing new media for plate "
            + str(idx + 1)
            + ", cycle: "
            + str(cycle + 1),
        )
        dispense(
            {
                "Module": plate_pos,
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "DispenseVolume": in_media_vol / repeat,
                "BottomOffsetOfZ": 10,
                "DispenseRateOfP": 50,
                "DelySeconds": 0,
                "IfTipTouch": False,
                "TipTouchHeight": 10,
                "TipTouchOffsetOfX": 3,
                "SecondRouteRate": 35,
            }
        )
    # empty excess for reverse pipette into new media
    report("Addition of new media", "Emptying excess")
    empty(
        {
            "Module": new_media_res,
            "Tips": 96,
            "Col": 1,
            "Row": 1,
            "BottomOffsetOfZ": 1,
            "DispenseRateOfP": 50,
            "DelySeconds": 0,
            "IfTipTouch": False,
            "TipTouchHeight": 10,
            "TipTouchOffsetOfX": 3,
            "SecondRouteRate": 35,
        }
    )
report("Addition of new media", "End")
unload_tips({"Module": new_media_tips, "Tips": 96, "Col": 1, "Row": 1})
report("Media exchange", "Complete")
home()
unlock()
dialog("Media exchange completed.")
# workflow block end
