from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle


class LogSubBox(ButtonBehavior, BoxLayout):

    def __init__(self, orientation, **kwargs):
        super().__init__(**kwargs)

        self.orientation = orientation
        self.padding = (self.width * 0.2, self.height * 0.1)
        self.spacing = (self.height * 0.1)


class LogButton(Button):

    def __init__(self, text, on_press=None, **kwargs):
        super().__init__(**kwargs)

        self.on_press = on_press
        self.text = text
        self.size_hint = (0.4, 0.2)
        self.pos_hint = {'center_y': 0.5}
        self.background_color = [0, 0, 0, 0]
        self.create_rounded_corners()
        
    def create_rounded_corners(self):
        
        with self.canvas.before:
            Color(120/255, 120/255, 175/255, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
class LogTextInput(TextInput):

    def __init__(self, hint_text, **kwargs):
        super().__init__(**kwargs)

        self.hint_text = hint_text
        self.multiline = False
        self.size_hint_y = None
        self.size = (0, 30)
        self.pos_hint = {'center_y': 0.5}
