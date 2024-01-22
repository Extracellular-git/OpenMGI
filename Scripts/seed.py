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
        ("POS1", "TipGEBAF250A", "Tips for seeding", "", False, True, ""),
        ("POS2", "SuzhouChenxuCAR-190NS", "Cell reservoir", "", False, True, ""),
        ("POS3", "", "", "", False, True, ""),
        ("POS4", "", "", "", False, True, ""),
        ("POS5", "", "", "", False, True, ""),
        ("POS6", "96_wellplate_flat_bottom", "Plate to seed", "", False, True, ""),
        ("POS7", "", "", "", False, True, ""),
        ("POS8", "", "", "", False, True, ""),
        ("POS9", "", "", "", False, True, ""),
        ("POS10", "", "", "", False, True, ""),
        ("POS11", "", "", "", False, True, ""),
        ("POS12", "", "", "", False, True, ""),
        ("POS13", "", "", "", False, True, ""),
        ("POS14", "", "", "", False, True, ""),
        ("POS15", "", "", "", False, True, ""),
        ("POS16", "", "", "", False, True, ""),
        ("POS17", "", "", "", False, True, ""),
        (
            "POS18",
            "",
            "",
            "",
            False,
            True,
            "Magnet",
        ),
        (
            "POS19",
            "",
            "",
            "",
            False,
            True,
            "Magnet",
        ),
        (
            "POS20",
            "",
            "",
            "",
            False,
            True,
            "Shaker",
        ),
        ("POS21", "", "", "", False, True, "Temp"),
        ("POS22", "", "", "", False, True, ""),
        ("POS23", "", "", "", False, True, ""),
        ("POS24", "", "", "", False, True, ""),
    ]


binding_map(
    {
        "POS1": ["TipGEBAF250A", None, None],
        "POS2": ["SuzhouChenxuCAR-190NS", None, None],
        "POS3": ["", None, None],
        "POS4": ["", None, None],
        "POS5": ["", None, None],
        "POS6": ["96_wellplate_flat_bottom", None, None],
        "POS7": ["", None, None],
        "POS8": ["", None, None],
        "POS9": ["", None, None],
        "POS10": ["", None, None],
        "POS11": ["", None, None],
        "POS12": ["", None, None],
        "POS13": ["", None, None],
        "POS14": ["", None, None],
        "POS15": ["", None, None],
        "POS16": ["", None, None],
        "POS17": ["", None, None],
        "POS18": ["", None, None],
        "POS19": ["", None, None],
        "POS20": ["", None, "shake"],
        "POS21": ["", None, None],
        "POS22": ["", None, None],
        "POS23": ["", None, None],
        "POS24": ["", None, None],
    }
)

tips = "POS1"
cell_res = "POS2"
cell_tips = "POS6"
seed_vol = 100

load_tips({"Module": tips, "Tips": 96, "Col": 1, "Row": 1})

mix(
    {
        "Module": cell_res,
        "Tips": 96,
        "Col": 1,
        "Row": 1,
        "SubMixLoopCounts": 3,
        "MixLoopVolume": 100,
        "BottomOffsetOfZ": 5,
        "MixLoopAspirateRate": 70,
        "MixOffsetOfZInLoop": 5,
        "MixLoopDispenseRate": 70,
        "MixOffsetOfZAfterLoop": 5,
        "DispenseRateAfterSubmixLoop": 70,
        "PreAirVolume": 0,
        "SubMixLoopCompletedDely": 0,
        "SecondRouteRate": 35,
        "IfTipTouch": False,
        "MixLoopAspirateDely": 0,
        "MixLoopDispenseDely": 0,
        "DelyAfterSubmixLoopCompleted": 0,
    }
)

aspirate(
    {
        "Module": cell_res,
        "Tips": 96,
        "Col": 1,
        "Row": 1,
        "AspirateVolume": seed_vol + 10,
        "BottomOffsetOfZ": 2,
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


dispense(
    {
        "Module": cell_plate,
        "Tips": 96,
        "Col": 1,
        "Row": 1,
        "DispenseVolume": seed_vol,
        "BottomOffsetOfZ": 35,
        "DispenseRateOfP": 60,
        "DelySeconds": 0,
        "IfTipTouch": False,
        "TipTouchHeight": 1,
        "TipTouchOffsetOfX": 5,
        "SecondRouteRate": 35,
    }
)
