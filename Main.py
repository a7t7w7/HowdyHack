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


def request_terms():
    url = "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500"
    response: Response = requests.get(url)
    content = json.loads(response.content)
    print(content)



request_terms()
