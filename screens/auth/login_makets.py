from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from screens.main_makets import RoundedButton


class LogSubBox(BoxLayout):

    def __init__(self, orientation, **kwargs):
        super().__init__(**kwargs)

        self.orientation = orientation
        self.padding = (self.width * 0.2, self.height * 0.1)
        self.spacing = (self.height * 0.1)


class LogButton(RoundedButton):

    def __init__(self, background_color, text, on_press=None, **kwargs):
        super().__init__(background_color, **kwargs)

        self.on_press = on_press
        self.text = text
        self.size_hint = (0.4, 0.2)
        self.pos_hint = {'center_y': 0.5}
        
        
class LogTextInput(TextInput):

    def __init__(self, hint_text, **kwargs):
        super().__init__(**kwargs)

        self.hint_text = hint_text
        self.multiline = False
        self.size_hint_y = None
        self.size = (0, 30)
        self.pos_hint = {'center_y': 0.5}
