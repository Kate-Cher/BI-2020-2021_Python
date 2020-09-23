data_vol = {1: "bit",
            2: "byte",
            3: "kilobyte",
            4: "megabyte",
            5: "gigabyte",
            6: "terabyte",
            7: "petabyte"}

bit_rate = {1: "bit/s"}
byte_conv = ''
print("Hello! This is simple units converter.")
# print("Choose units to convert:\n 1:convert data volume\n 2:convert volume")
# convert_type = input("Enter 1 or 2: ")
convert_type = 1
if convert_type == 1:
    print("Choose units you'd like to convert:")
    for key in data_vol:
        print(key, ":", data_vol[key])
    conv = [int(x) for x in input("Enter 2 numbers-1st-from, 2nd-to:").split()]
    vol = int(input("How many " + str(data_vol[conv[0]]) + "s to convert: "))
    if conv[0] >= 2 and conv[1] >= 2:
        byte_conv = vol * 2 ** (10 * (conv[0] - conv[1]))
    elif conv[0] == 1 and conv[1] != 1:
        byte_conv = vol * 2 ** (10 * (conv[0] - conv[1]+1)) / 8
    elif conv[1] == 1 and conv[0] != 1:
        byte_conv = vol * 2 ** (10 * (conv[0] - conv[1] - 1)) * 8
    else:
        byte_conv = vol
        out_str = str(vol) + " " + str(data_vol[conv[0]])
    print(str(byte_conv) + " " + str(data_vol[conv[1]]) + "s in " + out_str)
elif convert_type == 2:
    print("Choose units you'd like to convert:")
