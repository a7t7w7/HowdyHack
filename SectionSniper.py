from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.config import Config
import json
from pprint import pprint
from typing import Dict, List
from plyer import notification

import requests
from Data_Functions import find_avai_class
from Data_Functions import find_all_class

# Get all terms: https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500
from requests import Response

def request_terms() -> List[Dict[str, str]]:
    """Performs a GET request for all terms in TAMU history"""
    url = "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?dataType=json&offset=1&max=500"
    response: Response = requests.get(url)
    return json.loads(response.content)


def request_sections(dept: str, course_num: str, cookies):
    url = f"https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subjectcoursecombo={dept+course_num}&txt_term=201931&pageOffset=0&pageMaxSize=500&sortColumn=subjectDescription&sortDirection=asc"
    response = requests.get(url, cookies=cookies)
    return(json.loads(response.content))


def post_term(term_code: str):
    """Makes a POST request to set the desired term for consequent requests. Returns cookies"""
    url = "https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/term/search?mode=courseSearch"
    body = {
        "dataType": "json",
        "term": term_code
    }
    response: Response = requests.post(url, data=body)
    return response.cookies


def search(dept: str, course_num: str, sec: str, currently_watching):
    name = dept + " " + course_num + " " + sec
    terms = request_terms()
    term_code = terms[0]["code"]
    term_cookies = post_term(term_code)
    database = request_sections(dept,course_num,term_cookies)
    # pprint(database)
    if database["tamuActualTotal"] == 0:
        print('INVALID INPUT')
        return False
    # pprint(database)
    allsecs = find_all_class(database, dept, course_num)
    avasecs = find_avai_class(database, dept, course_num)
    if name in avasecs:
        notification.notify(title="Section Available!: ", message=name, app_name="Section Sniper")
        return False
    elif name in allsecs:
        notification.notify(title="Section Unavailable: ", message=name, app_name="Section Sniper")
        if name not in currently_watching:
            currently_watching.append(name)
            return True
        return False
    else:
        notification.notify(title="Section Does Not Exist: ", message=name, app_name="Section Sniper")
        return False

class Display(Widget):

    def init(self):
        print("initialize")
        self.currently_watching = []

    def update(self, dt):
        for each in self.currently_watching:
            name,course_num,sec_num = each.split(" ")
            print(each)
            search(name, course_num, sec_num, self.currently_watching)

    def button_pressed(self):
        self.ids.department.text = self.ids.department.text.upper()
        print("Department: ", self.ids.department.text)
        print("Course #: ", self.ids.course_num.text)
        print("Section #: ", self.ids.sec_num.text)
        if (search(self.ids.department.text, self.ids.course_num.text, self.ids.sec_num.text, self.currently_watching)):
            self.ids.course_queue.text = "Course queue: \n"
            for each in self.currently_watching:
                self.ids.course_queue.text += each + "\n"



class SectionSniperApp(App):
    def build(self):
        display = Display()
        display.init()
        Clock.schedule_interval(display.update, 300)
        return display


if __name__ == '__main__':
    Config.set('graphics', 'width', '320')
    Config.set('graphics', 'height', '480')
    SectionSniperApp().run()
