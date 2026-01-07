from kivy.app import App
from kivy.uix.label import Label

class CinemanaApp(App):
    def build(self):
        return Label(text="Welcome to Cinemana iOS!")

if __name__ == "__main__":
    CinemanaApp().run()
