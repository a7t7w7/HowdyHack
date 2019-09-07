# HowdyHack 2019
import json
import requests


# Get all terms: https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500
from requests import Response

class CourseData:
    def __init__(self, crn, name, title):
        self.crn = crn
        self.name = name
        self.title = title

    def print_data(self):
        print("CRN:", self.crn)
        print("Name:", self.name)
        print("Title:", self.title)

def find_avai_class(data, wanted_class = "MATH 151"):
    """
    Takes in a given data set and a class.
    Returns an array of the classes that are open of a specific type.
    """
    arr = []
    for CRN in data.values():
        for key in CRN.keys():
            if key == "name":
                if wanted_class in CRN["name"] and CRN["open"] == True:
                    arr.append(CRN[key])
    return arr

def check_class(fullname, arr):
    """
    Takes in the full name of a specific class and an array of the available open classes. Ex: MATH 251 509
    Returns Boolean variable to see if the specific class is open
    """
    if fullname in arr:
        return True
    else:
        return False

def request_terms():
    url = "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500"
    response: Response = requests.get(url)
    content = json.loads(response.content)
    print(content)



request_terms()

#This is just for tests
database = "201931.json"
data = json.loads(open(database).read())

open_class = find_avai_class(data, "MATH 251")
print(open_class)
print(check_class("MATH 251 505", open_class))