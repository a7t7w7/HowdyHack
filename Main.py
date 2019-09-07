# HowdyHack 2019


class CourseData:
    def __init__(self, crn, name, title):
        self.crn = crn
        self.name = name
        self.title = title

    def print_data(self):
        print("CRN:", self.crn)
        print("Name:", self.name)
        print("Title:",self.title)


data_file = "201931.json"
class_list = []

try:
    f = open(data_file, "r")
    f1 = f.readlines()
    for line in f1:
        if len(line) > 11 and line[11] == '{':
            crn = line[3:8]
        if len(line) > 8 and line[5:9] == "name":
            name = line[13:-3]
        if len(line) > 8 and line[5:10] == "title":
            title = line[14:-3]
            class_list.append(CourseData(crn, name, title))
    f.close()
except FileNotFoundError:
    print("Error: data file does not exist")

for each in class_list:
    each.print_data()


