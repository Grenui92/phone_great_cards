from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color

from screens.main_makets import RoundedButton
             
class CollectionsButton(RoundedButton):
    
    def __init__(self, background_color, **kwargs):
        super().__init__(background_color, **kwargs)
        
        self.size_hint_y = None
        self.size = 0, 30

        
class CreationButton(RoundedButton):
    
    def __init__(self, background_color, **kwargs):
        super().__init__(background_color, **kwargs)
        
        self.size_hint_y = None
        self.size = 0, 50
        