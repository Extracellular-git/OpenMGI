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
        ("POS9", "96_wellplate_u_bottom", "Cell plate 1", "", False, True, ""),
        ("POS10", "96_wellplate_u_bottom", "Cell plate 2", "", False, True, ""),
        ("POS11", "96_wellplate_u_bottom", "Cell plate 3", "", False, True, ""),
        ("POS12", "96_wellplate_u_bottom", "Cell plate 4", "", False, True, ""),
        ("POS13", "96_wellplate_u_bottom", "Cell plate 5", "", False, True, ""),
        ("POS14", "96_wellplate_u_bottom", "Cell plate 6", "", False, True, ""),
        ("POS15", "96_wellplate_u_bottom", "Cell plate 7", "", False, True, ""),
        ("POS16", "96_wellplate_u_bottom", "Cell plate 8", "", False, True, ""),
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

# defining the default user inputed variables
number_plates = 1
in_media_vol = 180
aspirate_z_offset = 0.5
# asks the user for the inputs
s_require3_result = require3(
    [],
    [
        {"Number of plates": ["1", "Integer between 1-8"]},
        {"Volume of fresh media": ["180", "Integer between 0-200"]},
    ],
)
# indexes the provided user inputs and converts data type as appropriate
number_plates = int(s_require3_result.Item2[0])
in_media_vol = int(s_require3_result.Item2[1])

# defining the different iterable parameters required for the assay
# Where the tips for the transfers are stored
tips_list = ["POS1", "POS2", "POS3", "POS4", "POS5", "POS6", "POS7", "POS8"]
use_tips_list = tips_list[0 : number_plates - 1]
# List of positions in which the plates are placed (8 total)
plates_list = ["POS9", "POS10", "POS11", "POS12", "POS13", "POS14", "POS15", "POS16"]
use_plates_list = plates_list[0 : number_plates - 1]
# workflow block begins
home()

# Remove media from each plate in use with new tips each time.
for idx, plate_pos in enumerate(use_plates_list):
    load_tips({"Module": use_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})
    aspirate(
        {
            "Module": plate_pos,
            "Tips": 96,
            "Col": 1,
            "Row": 1,
            "AspirateVolume": 200,
            "BottomOffsetOfZ": aspirate_z_offset,
            "AspirateRateOfP": 100,
            "PreAirVolume": 5,
            "PostAirVolume": 0,
            "DelySeconds": 0.5,
            "IfTipTouch": False,
            "TipTouchHeight": 10,
            "TipTouchOffsetOfX": 3,
            "SecondRouteRate": 10,
        }
    )
    empty(
        {
            "Module": "POS17",
            "Tips": 96,
            "Col": 1,
            "Row": 1,
            "BottomOffsetOfZ": 35,
            "DispenseRateOfP": 1000,
            "DelySeconds": 0.5,
            "IfTipTouch": False,
            "TipTouchHeight": 1,
            "TipTouchOffsetOfX": 5,
            "SecondRouteRate": 10,
        }
    )
    unload_tips({"Module": use_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})

# TODO Add fresh media from reservoir to each plate in use. use only 1 set of tips, do not touch bottom.

load_tips({"Module": "POS22", "Tips": 96, "Col": 1, "Row": 1})
for idx, plate_pos in enumerate(use_plates_list):
    # Load fresh media
    aspirate(
        {
            "Module": "POS23",
            "Tips": 96,
            "Col": 1,
            "Row": 1,
            "AspirateVolume": in_media_vol,
            "BottomOffsetOfZ": 35,
            "AspirateRateOfP": 150,
            "PreAirVolume": 5,
            "PostAirVolume": 0,
            "DelySeconds": 0,
            "IfTipTouch": False,
            "TipTouchHeight": 10,
            "TipTouchOffsetOfX": 3,
            "SecondRouteRate": 35,
        }
    )
    # Dispense fresh media into plate. do not touch the bottom, and do it slowly.
    empty(
        {
            "Module": plate_pos,
            "Tips": 96,
            "Col": 1,
            "Row": 1,
            "BottomOffsetOfZ": 10,
            "DispenseRateOfP": 100,
            "DelySeconds": 0,
            "IfTipTouch": False,
            "TipTouchHeight": 1,
            "TipTouchOffsetOfX": 5,
            "SecondRouteRate": 10,
        }
    )
unload_tips({"Module": "POS22", "Tips": 96, "Col": 1, "Row": 1})

home()
# workflow block end
