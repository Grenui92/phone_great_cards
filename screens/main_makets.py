from kivy.graphics import RoundedRectangle, Color
from kivy.uix.button import Button
from kivy.app import App

class RoundedButton(Button):

    def __init__(self, background_color, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.create_rounded_corners(background_color)
        
    def create_rounded_corners(self, background_color):
        
        with self.canvas.before:
            Color(*background_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        

class MainBox():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running_app = App.get_running_app()  