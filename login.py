import kivy

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class LoginInputs(BoxLayout):
    
    def __init__(self, orientation, **kwargs):
        super(LoginInputs, self).__init__(**kwargs)
        
        self.orientation = orientation
        self.username_intput = TextInput(hint_text="Username", size_hint=(0.6, 0.1))
        self.password_input = TextInput(hint_text="Password", size_hint=(0.6, 0.1))

        self.add_widget(self.username_intput)
        self.add_widget(self.password_input)
        
class Buttons(BoxLayout):
    
    def __init__(self, orientation, **kwargs):
        super(Buttons, self).__init__(**kwargs)
        
        self.orientation = orientation
        self.submit_button = Button(text="Submit")
        self.reset_button = Button(text="Reset")
        
        self.add_widget(self.submit_button)
        self.add_widget(self.reset_button)
        
        
class LoginWindow(BoxLayout):
    def __init__(self, orientation, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        
        self.orientation = orientation
        self.username_input = LoginInputs(orientation="vertical")
        self.password_input = Buttons(orientation="horizontal")
        
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

    
