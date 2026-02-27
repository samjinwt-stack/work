from kivy.app import App
from kivy.uix.label import Label

class WorkLogApp(App):
    def build(self):
        return Label(text="WorkLog Android Build Success")

if __name__ == "__main__":
    WorkLogApp().run()
