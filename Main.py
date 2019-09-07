# HowdyHack 2019

data_file = "201931.json"

try:
    f = open(data_file, "r")
    f1 = f.readlines()
    for line in f1:
        if len(line) > 11 and line[11] == '{':
            print("CRN:",line[3:8])
        if len(line) > 8 and line[5:9] == "name":
            print("Name:",line[13:-3])
        if len(line) > 8 and line[5:10] == "title":
            print("Title:",line[14:-3])
    f.close()
except FileNotFoundError:
    print("Error: data file does not exist")




