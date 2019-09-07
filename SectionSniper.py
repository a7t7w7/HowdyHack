from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.config import Config


class Display(Widget):

    def init(self):
        print("initialize")


    def update(self, dt):
        pass

    def button_pressed(self):
        print("lmao")
        print("Department: ", self.ids.department.text)
        print("Course #: ", self.ids.course_num.text)
        print("Section #: ", self.ids.sec_num.text)



class SectionSniperApp(App):
    def build(self):
        display = Display()
        display.init()
        Clock.schedule_interval(display.update, 1.0)
        return display


if __name__ == '__main__':
    Config.set('graphics', 'width', '320')
    Config.set('graphics', 'height', '480')
    SectionSniperApp().run()
