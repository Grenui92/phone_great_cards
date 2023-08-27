
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class MainBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running_app = App.get_running_app()  

        
