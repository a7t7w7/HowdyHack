# HowdyHack 2019
import json

class CourseData:
    def __init__(self, crn, name, title):
        self.crn = crn
        self.name = name
        self.title = title

    def print_data(self):
        print("CRN:", self.crn)
        print("Name:", self.name)
        print("Title:",self.title)

database = "201931.json"
data = json.loads(open(database).read())

wanted_class = "MATH 251"

for CRN in data.values():
    for key in CRN.keys():
        if key == "name":
            if wanted_class in CRN["name"] and CRN["open"] == True:
                print(CRN[key])


