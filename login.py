import kivy

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class LoginInputs(BoxLayout):
    
    def __init__(self, **kwargs):
        super(LoginInputs, self).__init__(**kwargs)
        
        self.orientation = "vertical"

        
        username_intput = TextInput(hint_text="Username",
                                         size_hint=(0.6, 1), 
                                         multiline=False,
                                         pos_hint={"center_x": .5})
        
        password_input = TextInput(hint_text="Password", 
                                        size_hint=(0.6, 1), 
                                        multiline=False,
                                        pos_hint={"center_x": .5})
        
        username_label = Label(text="Username")
        password_label = Label(text="Password")
        
        self.add_widget(username_label)
        self.add_widget(username_intput)
        self.add_widget(password_label)
        self.add_widget(password_input)

        
        
class Buttons(BoxLayout):
    
    def __init__(self, **kwargs):
        super(Buttons, self).__init__(**kwargs)
        
        self.orientation = "horizontal"
        self.submit_button = Button(text="Submit")
        self.reset_button = Button(text="Reset")
        
        self.add_widget(self.submit_button)
        self.add_widget(self.reset_button)
        
        
class LoginWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        
        self.orientation = "vertical"
        self.username_input = LoginInputs()
        self.password_input = Buttons()
        
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

    
