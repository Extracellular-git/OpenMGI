# looping test
plate_list = ["1", "2", "3", "4", "5"]
number_plates = len(plate_list)
chunked_list = list()
if number_plates <= 3:
    reuse_count = 1
elif number_plates <= 6:
    reuse_count = 2
else:
    reuse_count = 3
for i in range(0, len(plate_list), reuse_count):
    chunked_list.append(plate_list[i : i + reuse_count])

print(chunked_list)
tip_list = ["tip 1", "tip 2", "tip 3"]

tip_counter = 0
plate_done_count = 0

for tip in tip_list:
    print("loading " + tip)
    # for reuse_cycle in range(reuse_count):
    try:
        plate_sublist = plate_list[plate_done_count : plate_done_count + reuse_count]
    except IndexError:
        plate_sublist = plate_list[plate_done_count::]

    for plate in plate_sublist:
        plate_done_count += 1
        print(f"--plate {plate}")
        # for asp in range(2):
        # print(f"----aspiration {asp+1}")
        # print("--tip wash x1")
        # print("--tip wash x2")
    print(f"unloading {tip}")
