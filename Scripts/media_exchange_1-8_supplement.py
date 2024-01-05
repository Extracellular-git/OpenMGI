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
        ("POS1", "TipGEBAF250A", "Tips for spent media 1,2,3", "", False, True, ""),
        ("POS2", "TipGEBAF250A", "Tips for spent media 4,5,6", "", False, True, ""),
        ("POS3", "TipGEBAF250A", "Tips for spent media 7,8", "", False, True, ""),
        (
            "POS4",
            "SuzhouChenxuCAR-190NS",
            "PBS tip wash x1 reservoir",
            "",
            False,
            True,
            "",
        ),
        (
            "POS5",
            "VDeepwellPlateDN07350501",
            "Waste disposal deepwell",
            "",
            False,
            True,
            "",
        ),
        ("POS6", "SuzhouChenxuCAR-190NS", "Fresh media reservoir", "", False, True, ""),
        ("POS7", "TipGEBAF250A", "Fresh media tips", "", False, True, ""),
        (
            "POS8",
            "SuzhouChenxuCAR-190NS",
            "PBS tip wash x2 reservoir",
            "",
            False,
            True,
            "",
        ),
        ("POS9", "96_wellplate_flat_bottom", "Cell plate 1", "", False, True, ""),
        ("POS10", "96_wellplate_flat_bottom", "Cell plate 2", "", False, True, ""),
        ("POS11", "96_wellplate_flat_bottom", "Cell plate 3", "", False, True, ""),
        ("POS12", "96_wellplate_flat_bottom", "Cell plate 4", "", False, True, ""),
        ("POS13", "96_wellplate_flat_bottom", "Cell plate 5", "", False, True, ""),
        ("POS14", "96_wellplate_flat_bottom", "Cell plate 6", "", False, True, ""),
        ("POS15", "96_wellplate_flat_bottom", "Cell plate 7", "", False, True, ""),
        ("POS16", "96_wellplate_flat_bottom", "Cell plate 8", "", False, True, ""),
        ("POS17", "VDeepwellPlateDN07350501", "Supplement 1", "", False, True, ""),
        (
            "POS18",
            "VDeepwellPlateDN07350501",
            "Supplement 2",
            "",
            False,
            True,
            "Magnet",
        ),
        (
            "POS19",
            "VDeepwellPlateDN07350501",
            "Supplement 3",
            "",
            False,
            True,
            "Magnet",
        ),
        (
            "POS20",
            "VDeepwellPlateDN07350501",
            "Supplement 4",
            "",
            False,
            True,
            "Shaker",
        ),
        ("POS21", "TipGEBAF250A", "Supplement 1 tips", "", False, True, "Temp"),
        ("POS22", "TipGEBAF250A", "Supplement 2 tips", "", False, True, ""),
        ("POS23", "TipGEBAF250A", "Supplement 3 tips", "", False, True, ""),
        ("POS24", "TipGEBAF250A", "Supplement 4 tips", "", False, True, ""),
    ]


binding_map(
    {
        "POS1": ["TipGEBAF250A", None, None],
        "POS2": ["TipGEBAF250A", None, None],
        "POS3": ["TipGEBAF250A", None, None],
        "POS4": ["SuzhouChenxuCAR-190NS", None, None],
        "POS5": ["VDeepwellPlateDN07350501", None, None],
        "POS6": ["SuzhouChenxuCAR-190NS", None, None],
        "POS7": ["TipGEBAF250A", None, None],
        "POS8": ["SuzhouChenxuCAR-190NS", None, None],
        "POS9": ["96_wellplate_flat_bottom", None, None],
        "POS10": ["96_wellplate_flat_bottom", None, None],
        "POS11": ["96_wellplate_flat_bottom", None, None],
        "POS12": ["96_wellplate_flat_bottom", None, None],
        "POS13": ["96_wellplate_flat_bottom", None, None],
        "POS14": ["96_wellplate_flat_bottom", None, None],
        "POS15": ["96_wellplate_flat_bottom", None, None],
        "POS16": ["96_wellplate_flat_bottom", None, None],
        "POS17": ["VDeepwellPlateDN07350501", None, None],
        "POS18": ["VDeepwellPlateDN07350501", None, None],
        "POS19": ["VDeepwellPlateDN07350501", None, None],
        "POS20": ["VDeepwellPlateDN07350501", None, "shake"],
        "POS21": ["TipGEBAF250A", None, None],
        "POS22": ["TipGEBAF250A", None, None],
        "POS23": ["TipGEBAF250A", None, None],
        "POS24": ["TipGEBAF250A", None, None],
    }
)
# deck block end
# define constants
new_media_tips = "POS7"
new_media_res = "POS6"
old_media_res = "POS5"
pbs_tip_wash_list = ["POS4", "POS8"]
supplement_tips_list = ["POS21", "POS22", "POS23", "POS24"]
supplement_res_list = ["POS17", "POS18", "POS19", "POS20"]
# defining the default user inputed variables
number_plates = 1
in_media_vol = 180
aspirate_z_offset = 0.4
supp_vol = 20
plate_type = "96_wellplate_flat_bottom"
# asks the user for the inputs
s_require3_result = require3(
    [{"Select plate type": ["96_wellplate_flat_bottom", "96_wellplate_u_bottom"]}],
    [
        {"Number of plates": ["1", "Integer between 1-8"]},
        {"Volume of media to remove": ["200", "Integer between 0-300"]},
        {"Volume of fresh media": ["180", "Integer between 0-300"]},
        {"Number of supplement plates": ["1", "Integer between 0-4"]},
        {
            "Supplement 1 goes into which plates?": [
                "",
                "Comma-seperated list of integers eg. 1,2,3",
            ]
        },
        {
            "Supplement 2 goes into which plates?": [
                "",
                "Comma-seperated list of integers eg. 1,2,3",
            ]
        },
        {
            "Supplement 3 goes into which plates?": [
                "",
                "Comma-seperated list of integers eg. 1,2,3",
            ]
        },
        {
            "Supplement 4 goes into which plates?": [
                "",
                "Comma-seperated list of integers eg. 1,2,3",
            ]
        },
    ],
)
# indexes the provided user inputs and converts data type as appropriate
plate_type = s_require3_result.Item1[0]
number_plates = min(int(s_require3_result.Item2[0]), 8)
out_media_vol = min(int(s_require3_result.Item2[1]), 300)
in_media_vol = min(int(s_require3_result.Item2[2]), 300)
number_supplement_plates = min(int(s_require3_result.Item2[3]), 4)
supplement_additions = [
    [int(num) for num in s_require3_result.Item2[4].split(",")],
    [int(num) for num in s_require3_result.Item2[5].split(",")],
    [int(num) for num in s_require3_result.Item2[6].split(",")],
    [int(num) for num in s_require3_result.Item2[7].split(",")],
]
# parse supplement additions to plate positions
plate_pos_dict = {
    1: "POS9",
    2: "POS10",
    3: "POS11",
    4: "POS12",
    5: "POS13",
    6: "POS14",
    7: "POS15",
    8: "POS16",
}
for idx, supp_sublist in enumerate(supplement_additions):
    supplement_additions[idx] = [plate_pos_dict[x] for x in supp_sublist]


update_feature(
    [
        ("POS1", "TipGEBAF250A", "Tips for spent media 1,2,3", "", False, True, ""),
        ("POS2", "TipGEBAF250A", "Tips for spent media 4,5,6", "", False, True, ""),
        ("POS3", "TipGEBAF250A", "Tips for spent media 7,8", "", False, True, ""),
        (
            "POS4",
            "SuzhouChenxuCAR-190NS",
            "PBS tip wash x1 reservoir",
            "",
            False,
            True,
            "",
        ),
        (
            "POS5",
            "VDeepwellPlateDN07350501",
            "Waste disposal deepwell",
            "",
            False,
            True,
            "",
        ),
        ("POS6", "SuzhouChenxuCAR-190NS", "Fresh media reservoir", "", False, True, ""),
        ("POS7", "TipGEBAF250A", "Fresh media tips", "", False, True, ""),
        (
            "POS8",
            "SuzhouChenxuCAR-190NS",
            "PBS tip wash x2 reservoir",
            "",
            False,
            True,
            "",
        ),
        ("POS9", plate_type, "Cell plate 1", "", False, True, ""),
        ("POS10", plate_type, "Cell plate 2", "", False, True, ""),
        ("POS11", plate_type, "Cell plate 3", "", False, True, ""),
        ("POS12", plate_type, "Cell plate 4", "", False, True, ""),
        ("POS13", plate_type, "Cell plate 5", "", False, True, ""),
        ("POS14", plate_type, "Cell plate 6", "", False, True, ""),
        ("POS15", plate_type, "Cell plate 7", "", False, True, ""),
        ("POS16", plate_type, "Cell plate 8", "", False, True, ""),
        ("POS17", "VDeepwellPlateDN07350501", "Supplement 1", "", False, True, ""),
        (
            "POS18",
            "VDeepwellPlateDN07350501",
            "Supplement 2",
            "",
            False,
            True,
            "Magnet",
        ),
        (
            "POS19",
            "VDeepwellPlateDN07350501",
            "Supplement 3",
            "",
            False,
            True,
            "Magnet",
        ),
        (
            "POS20",
            "VDeepwellPlateDN07350501",
            "Supplement 4",
            "",
            False,
            True,
            "Shaker",
        ),
        ("POS21", "TipGEBAF250A", "Supplement 1 tips", "", False, True, "Temp"),
        ("POS22", "TipGEBAF250A", "Supplement 2 tips", "", False, True, ""),
        ("POS23", "TipGEBAF250A", "Supplement 3 tips", "", False, True, ""),
        ("POS24", "TipGEBAF250A", "Supplement 4 tips", "", False, True, ""),
    ]
)

binding_map(
    {
        "POS1": ["TipGEBAF250A", None, None],
        "POS2": ["TipGEBAF250A", None, None],
        "POS3": ["TipGEBAF250A", None, None],
        "POS4": ["SuzhouChenxuCAR-190NS", None, None],
        "POS5": ["VDeepwellPlateDN07350501", None, None],
        "POS6": ["SuzhouChenxuCAR-190NS", None, None],
        "POS7": ["TipGEBAF250A", None, None],
        "POS8": ["SuzhouChenxuCAR-190NS", None, None],
        "POS9": [plate_type, None, None],
        "POS10": [plate_type, None, None],
        "POS11": [plate_type, None, None],
        "POS12": [plate_type, None, None],
        "POS13": [plate_type, None, None],
        "POS14": [plate_type, None, None],
        "POS15": [plate_type, None, None],
        "POS16": [plate_type, None, None],
        "POS17": ["VDeepwellPlateDN07350501", None, None],
        "POS18": ["VDeepwellPlateDN07350501", None, None],
        "POS19": ["VDeepwellPlateDN07350501", None, None],
        "POS20": ["VDeepwellPlateDN07350501", None, "shake"],
        "POS21": ["TipGEBAF250A", None, None],
        "POS22": ["TipGEBAF250A", None, None],
        "POS23": ["TipGEBAF250A", None, None],
        "POS24": ["TipGEBAF250A", None, None],
    }
)
# defining the different iterable parameters required for the assay
# Where the tips for the transfers are stored
tips_list = ["POS1", "POS2", "POS3"]
# List of positions in which the plates are placed (8 total)
plates_list = ["POS9", "POS10", "POS11", "POS12", "POS13", "POS14", "POS15", "POS16"]
use_plates_list = plates_list[0:number_plates]
use_supplement_list = ["POS17", "POS18", "POS19", "POS20"][0:number_supplement_plates]
use_supplement_additions_list = supplement_additions[0:number_supplement_plates]
# create block list
block_list = []
if number_plates <= 3:
    reuse_count = 1
elif number_plates <= 6:
    reuse_count = 2
else:
    reuse_count = 3
for idx in range(0, len(use_plates_list), reuse_count):
    block_list.append(use_plates_list[idx : idx + reuse_count])

# workflow block begins
lock()
hoodspeed(1000)
home()
# Remove media from each plate in use with new tips each time.
report("Removal of old media", "Start")
tip_counter = 0
if number_plates <= 3:
    reuse_count = 1
elif number_plates <= 6:
    reuse_count = 2
else:
    reuse_count = 3

for block_idx, block in enumerate(block_list):
    report("Plate block " + str(block_idx + 1), "Start")
    load_tips({"Module": tips_list[block_idx], "Tips": 96, "Col": 1, "Row": 1})
    # Media removal and tip wash loop
    for idx, plate_pos in enumerate(block):
        if out_media_vol > 175:
            # have to do more than one pipetting motion
            repeat = 2
        else:
            repeat = 1
        for cycle in range(repeat):
            plate_num = (idx + 1) + (block_idx * len(block_list[0]))
            report(
                "Removal of old media",
                "Aspirating plate " + str(plate_num) + ", cycle: " + str(cycle + 1),
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
            if cycle != 1:
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
                # Can tip touch liquid to get rid of drops since it is last operation
                report("Removal of old media", "Emptying excess")
                empty(
                    {
                        "Module": old_media_res,
                        "Tips": 96,
                        "Col": 1,
                        "Row": 1,
                        "BottomOffsetOfZ": 35,
                        "DispenseRateOfP": 100,
                        "DelySeconds": 0,
                        "IfTipTouch": True,
                        "TipTouchHeight": 40,
                        "TipTouchOffsetOfX": 2.8,
                        "SecondRouteRate": 35,
                    }
                )
        report("Removal of old media", "Tip wash")
        if number_plates != 1:
            # Don't mix if there is only one plate - no need
            for wash_res in pbs_tip_wash_list:
                mix(
                    {
                        "Module": wash_res,
                        "Tips": 96,
                        "Col": 1,
                        "Row": 1,
                        "SubMixLoopCounts": 5,
                        "MixLoopVolume": 150,
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
    unload_tips({"Module": tips_list[block_idx], "Tips": 96, "Col": 1, "Row": 1})
    # Fresh media addition inside each block-loop, so the cells don't dry out.
    report("Addition of new media", "Start")
    load_tips({"Module": new_media_tips, "Tips": 96, "Col": 1, "Row": 1})
    if in_media_vol > 175:
        repeat = 2
    else:
        repeat = 1
    for idx, plate in enumerate(block):
        plate_num = (idx + 1) + (block_idx * len(block_list[0]))
        for cycle in range(repeat):
            report(
                "Addition of new media",
                "Aspirating new media for plate "
                + str(plate_num)
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
                + str(plate_num)
                + ", cycle: "
                + str(cycle + 1),
            )
            dispense(
                {
                    "Module": plate,
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
    report("Addition of new media", "Complete")
    unload_tips({"Module": new_media_tips, "Tips": 96, "Col": 1, "Row": 1})
report("Media exchange", "Complete")

# perform supplement addition
report("Supplement addition", "Start")
for idx, supp_sublist in enumerate(use_supplement_additions_list):
    if len(supp_sublist) != 0:
        report("Supplement addition", "Load tips for S" + str(idx + 1))
        load_tips({"Module": supplement_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1})
        # Aspirate liquid for all additions from this supplement. add extra 5ul for reverse pipette. with 20ul supp, maximum would be 160ul so we are under the limit. If supp vol is higher, would have to do more transfers.
        report("Supplement addition", "Load S" + str(idx + 1))
        aspirate(
            {
                "Module": supplement_res_list[idx],
                "Tips": 96,
                "Col": 1,
                "Row": 1,
                "AspirateVolume": (supp_vol * len(supp_sublist)) + 5,
                "BottomOffsetOfZ": aspirate_z_offset,
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
        for plate in supp_sublist:
            report(
                "Supplement addition", "Dispense S" + str(idx + 1) + " into " + plate
            )
            # aspirate from supplement res list
            dispense(
                {
                    "Module": plate,
                    "Tips": 96,
                    "Col": 1,
                    "Row": 1,
                    "DispenseVolume": supp_vol,
                    "BottomOffsetOfZ": 10,
                    "DispenseRateOfP": 60,
                    "DelySeconds": 0,
                    "IfTipTouch": True,
                    "TipTouchHeight": 11,
                    "TipTouchOffsetOfX": 2,
                    "SecondRouteRate": 35,
                }
            )
        report("Supplement addition", "Complete")
        unload_tips(
            {"Module": supplement_tips_list[idx], "Tips": 96, "Col": 1, "Row": 1}
        )

home()
unlock()
dialog("Media exchange completed.")
# workflow block end
