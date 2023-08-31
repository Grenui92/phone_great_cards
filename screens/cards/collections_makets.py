from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

from screens.main_makets import RoundedButton
             
class CollectionsButton(RoundedButton):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.size_hint_y = 0.1

        self.pos_hint = {'top': 1}