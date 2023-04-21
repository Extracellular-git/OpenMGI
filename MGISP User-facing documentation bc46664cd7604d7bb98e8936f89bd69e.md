# MGISP User-facing documentation

# Table of contents

# Good practice for writing scripts

Every script must begin with a few specific lines to initialise the machine. 

```python
from spredo import *

spx96 = globals().get("Spx96")

init(spx96)
shake.binding(spx96)

pos_type_map = {...}
binding_map(pos_type_map)

lighton()
home()
```

Every script should also end with `home()`

- Pos Type map template
    
    ```python
    pos_type_map = {
        "POS1": None,
        "POS2": None,
        "POS3": None,
        "POS4": None,
        "POS5": None,
        "POS6": None,
        "POS7": None,
        "POS8": None,
        "POS9": None,
        "POS10": None,
        "POS11": None,
        "POS12": None,
        "POS13": None,
        "POS14": None,
        "POS15": None,
        "POS16": None,
        "POS17": None,
        "POS18": None,
        "POS19": None,
        "POS20": [None, "shake"],
        "POS21": None,
        "POS22": None,
        "POS23": None,
        "POS24": None,
    }
    ```
    

# Functions

---

## Function name

### Usage

### Examples

---

<aside>
❗ Note that several functions take arguments in a non-standard way: one argument as a dictionary that contains all of the arguments.

</aside>

## aspirate

Draws up a specified amount of liquid. Many parameters can be changed.

Note: the tips are 250ul, but the manufacturer recommend a range of 2-170ul max. 

### Usage

```python
argument_dict = {
										"Module": "POS1",
										"Well": "1A",
										"BottomOffsetOfZ": 0.5,
										"AspirateVolume": (100),
										"PreAirVolume": (5),
										"PostAirVolume": (2),
										"AspirateRateOfP": 10,
										"DelySeconds": 0.5
										"IfTipTouch": False,
										"TipTouchOffsetOfX": 3.3,
										"TipTouchHeight": 3
								}

aspirate(argument_dict)
```

TipTouch is used in the `"2020-08-12T14_12_25.1761894+01_002 Plate Nucleic Acid Extraction with PCR [Setup.py](http://setup.py/)"` file in history. Both Empty/dispense and aspirate appear to use it. 

### **TipTouch:**

TipTouch will after an aspiration or a empty touch the edge of the deep well plate.

```python
										"IfTipTouch": False,
										"TipTouchOffsetOfX": 3.3,
										"TipTouchHeight": 3
								}

```

### Usage

By default "IfTipTouch": False. 

To declare true, you don’t need to include it, just add the offset and height settings. 

### Examples

These settings work well with a “DeepwellPlateVWR_7353325”.

**TipTouchOffsetOfX:** how far it goes to touch from the centre. Higher than 3 it’s quite violent.

**TipTouchHeight:** how high the tips go before move to the edge. 

```python
argument_dict = {
										"Module": "POS1",
										"Well": "1A",
										"BottomOffsetOfZ": 0.5,
										"AspirateVolume": (100),
										"PreAirVolume": (5),
										"PostAirVolume": (2),
										"AspirateRateOfP": 10,
										"DelySeconds": 0.5
										"TipTouchOffsetOfX": 3,
										"TipTouchHeight": 38
								}

aspirate(argument_dict)
```

## empty

### Usage

### Examples

## mix

### Usage

### Examples

## load_tips

Loads tips from a specified position. The head can only load all at the same time, so in order to grab 1 row of tips, you need to specify the last row or column and leave space around the tip box for the head to go down.

### Usage

```python
argument_dict = {
										"Module": "POS1",
										"Well": "1A",
										"BottomOffsetOfZ": 0.5,
										"Row": 1,
										"Col" : 1,
										"Tips" : 96
								}

load_tips(argument_dict)
```

`Module` - specifies the position of the tip box to load from.

`Well` - Specifies where the 1A position of the head should move to on the tip box. see examples.

`BottomOffsetOfZ` - Function unknown. varying the number doesn’t seem to have any effect. this can be omitted.

`Row` - Specifies which row the head should move to when loading tips

`Col` - Specifies which column the head should move to when loading tips

`Tips` - Specifies how many tips should be picked up. This is not really functional, only 96 works.

### Examples

The argument dict provides several ways to specify where the head should be when it descends to pick up the tips. `Well`, `Row` & `Col` and `Tips` all do roughly the same thing, but with different usages. 

If you want to simply pick up all of the tips, your argument dict could be any of the following:

Well method:

```python
# Well method
argument_dict = {
										"Module": "POS1",
										"Well": "1A"
								}

# Row and Col method
argument_dict = {
										"Module": "POS1",
										"Row": 1,
										"Col" : 1
								}

# Tips method
argument_dict = {
										"Module": "POS1",
										"Tips": 96
								}
```

If you want to pick up only 1 row or column of tips, you can use either the Well argument, or the Row and Col arguments (they effectively describe the same thing):

```python
# Well method, pikcup up last column of 8 tips
argument_dict = {
										"Module": "POS1",
										"Well": "12A"
								}

# Row and Col method
argument_dict = {
										"Module": "POS1",
										"Row": 1,
										"Col" : 12
								}
```

## unload_tips

Unloads the tips to the specified location. This is highly controlled, suitable for depositing the tips back into the box they were loaded from. Usage is exactly the same as `load_tips()` and it takes the same arguments, just that it places the tips down instead of loading them. Quick example:

```python
argument_dict = {
										"Module": "POS1",
										"Well": "1A",
								}

unload_tips(argument_dict)
```

This will unload all 96 tips with the top left position being 1A on the receiving box.

## dely / delay

### Usage

### Examples

## home

Resets the machine head to position 1. This is important to call at the start and end of each script, so that the next script works correctly and the head is not left in the middle of the space.

### Usage

```python
home()
```

This function does not take any arguments

### Examples

```python

# Finish doing stuff
home()
```

## shake_on

Turns the shaker in position 20 on, to the specified rate (intensity) and direction. Shaking continues until `shake_off` is called.

### Usage

```python
shake_on(rate, direction)
```

- `rate` is an integer, specifies the intensity of the shaking. This value can range from 100-2000. For mixing a 96 well plate, 700 is a good amount.
- `direction` is an integer, specifies the direction of shaking. key:
    - `1` - counter-clockwise
    - `2` - clockwise
    - `3` - leading diagonal - ↗️ bottom left to top right
    - `4` - counter diagonal - ↖️ bottom right to top left
    - `5` - up and down
    - `6` - left to right

### Examples

Because shaking is generally wanted for a specific period of time, the best way to use this function is to run it in a `parallel_block`. This allows you to start the shaking and continue it whilst the machine carries out other instructions.

```python
def shake_block():
    shake_on(1000,1)
    dely(65)
    shake_off()

shaking_operation = parallel_block(shake_block)
```

The above code section does the following:

defines a function that:

starts the shaker at 1000 rate and counter clockwise direction.

waits for 65 seconds

turns off the shaker

runs the `shake_block` function in the background so that other instructions can be performed. 

This means that the shaker will run for 65 seconds at the desired rate and direction. 

If you need the shaking to be done before you perform any more instructions, you can use the `.Wait()` function from `parallel_block`:

```python
# Shaking has been started earlier

shaking_operation.Wait()

# Run other functions that need the shaking to be finished.
```

The `.Wait()` function pauses execution of any further instructions until the shaking in the block `shaking_operation` has completed.

## mvkit

Moves a selected “kit” from the source position to the destination position. The “kit” can be any plate or reservoir that the device recognises, as well as a lid.

If a position has a plate with a lid on it, and `moveall` is False, it will move the lid only. If it is true, it will move both items.

<aside>
❗ Moving lids does not seem to work.

</aside>

### Usage

```python
mvkit(source, dest, moveall=False, isJc=False)
```

- `source` Is the position which the robot will pick up from. this should be provided as a text string, eg: `"POS1"`. In the position map, this must have a specified kit name, eg. `"DeepwellPlateDT7350504"`. it must not be `None` or `"useless"`.
- `dest` is the destination position where the item will be placed. this should also be provided as a text string, eg: `"POS2"`. This must be `None` in the map.
- `moveall` is a boolean variable to indicate whether you want all of the items to be picked up (set to `True`), or just the top item (if there is one there). If there is no lid, it will just act as normal and pick up the item. This defaults to `False`, meaning you do not need to specify it.
- `isJc` I’m not sure what this is, don’t bother using it. Even the developers weren’t sure what it was.

### Examples

In most cases, the only arguments you need to give are the source and destination positions. example:

```python
# Move from position 1 to position 20
mvkit("POS1","POS20")
```

You can specifiy the `moveall` flag if you need it, like so:

```python
# Move all items from position 1 to position 20
mvkit("POS1", "POS20", moveall= True)
```

### Exceptions

- Moving a PCR plate (the ones without a proper base) to the MagRacks in position 18 and 19 does not work well, they will not seat properly and cannot be picked up again.
- The positions 1-4 cannot be used. The reason is physical. The robot arm cannot go that far into the frame with the gripper. Any other position 5-24 are free to be used.

GraspOffsetOfZ: 

GraspOffsetOfG:

## Moving lids custom function

What do we need:

tip no lid

lid

tip with lid

look into how it does it for PCR

## Display a message

---

---

---

---

---

---

---

---

---

## Labware measurement storage: kit.json

Measurements

You need to measure from the bottom (reservoirs, 96 well plates) if it’s a tip lid or pcr plate, from the top. The difference between top/bottom is usually around 2mm

GraspOffsetOfZ: 

GraspOffsetOfG:

ConsmeBottomOfZ:

**Note**: changing manually the Z, you can accurate modify how “movekit” function works. However, if you set up the Z too high, the function will execute the first part of the move (getting the item) but it will crash because the Z is out of the limit for the machine. This also happens if you want to use differenrent height for moving. i.e a pcr plate from a 96 deepwell plate to the floor etc. It seems works fine if you move from one position to the other if the deepwell is the same (maybe it detecs 

Board:

> 
> 
> 
> ```python
> lighton = lambda : board().OpenFloodLight()
> lightoff = lambda : board().CloseFloodLight()
> uvon = lambda : board().OpenSterilamp()
> uvoff = lambda : board().CloseSterilamp()
> unlock = lambda : board().OpenSafetyLock()
> lock = lambda : board().Lock()
> ```
> 

Laminar hood

`def hoodspeed(speed):`

```python
begin = time.time()
    exe_event("Set laminarhood",EnumStates.Running,'Hood',{'argus': {"Speed": speed},'PPX':speed})
    board().HoodSpeed(speed)
    exe_event("Set laminarhood",EnumStates.Completion,'Hood',{'argus': {"Speed": speed},'PPX':speed},True,False,time.time() - begin)
```

```python
def mvkit(source, dest,moveall = False,isJc = False):
    """
    source抓取pos号
    dest松开pos号
    moveall是否搬空整个pos号的东西
    isJc是否是丢垃圾指令，丢垃圾指令所有POS号都能抓取
    如果抓取位置上既有试剂盒又有盖子，抓取所有的话，就不需要盖子属性
    如果松开的位置上有试剂盒，那么kitname就应该是松开位置试剂盒的名称

Source capture pos number 
dest loose pos number 
moveall whether to empty the whole pos number 
isJc whether it is a garbage disposal command, 
all POS numbers can be captured if there are both kits 
and covers on the grabbing position, grab If you take all, 
there is no need for the lid attribute. 
If there is a kit in the loose position, then 
kitname should be the name of the kit in the loose position
    """
    global __MAP   
    info("move kit: parameters = %s"%str({"source":source,"dest":dest,"moveall":moveall}))
    kitname = __MAP[source][0]
    lidname = __MAP[source][1]   #时序使用
    kitname1 = __MAP[source][0]
    lidname2 = __MAP[source][1]   #check使用
    grasptop = False

    grasp_check(source)
    if(kitname is not None and lidname is not None and not moveall):#如果一个位置既有盖子，又有试剂盒，并且不移动所有的，那么就是抓取顶部
        grasptop = True

    grasp({'Module':source,'KitName':kitname,'LidName':lidname,'IsTop':grasptop,'IsJc':isJc})  #IsTop属性来识别到底用那个的属性
    change_map_grasp(source,moveall)
    report_pos(source,"grasp",grasptop)

    loosentop = False
    loose_check(dest,kitname1,lidname2,moveall)
    if(grasptop):                                                    #如果抓取顶部盖子，清空试剂盒名称
        kitname = None
    if(__MAP[dest][0] is not None):                                  #判断放置的位置，是不是放置在顶部            
        loosentop = True
        kitname = __MAP[dest][0]                                     #获取松开位置的试剂盒名称
    loosen({'Module':dest,'KitName':kitname,'LidName':lidname,'IsTop':loosentop})     #IsTop属性来识别到底用那个的属性
    change_map_loose(dest,kitname1,lidname2,moveall)
    report_pos(dest,"loosen",loosentop)
```