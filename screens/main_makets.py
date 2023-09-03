from kivy.graphics import RoundedRectangle, Color, Rectangle
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from time import sleep

from screens.auth.login_services import logout
class RoundedButton(Button):

    def __init__(self, background_color, **kwargs):
        super().__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]
        self.create_rounded_corners(background_color)

    def create_rounded_corners(self, background_color):

        with self.canvas.before:
            Color(*background_color)
            self.rect = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[10])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MainBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running_app = App.get_running_app()

        self.sub_box = SubBox(orientation='horizontal', size_hint=(1, 0.1))
        self.clear_widgets()
        if not self.running_app.CURRENT_USER:
            login_button = NavButton(text='Login',
                                       on_press=self.switch_to_login,
                                       background_color=(1, 0, 0, 1))
            registration_button = NavButton(text='Registration',
                                              on_press=self.switch_to_registration,
                                              background_color=(1, 0, 0, 1))

            self.sub_box.add_widget(login_button)
            self.sub_box.add_widget(registration_button)            

        else:
            logout_button = NavButton(text='Logout',
                                        on_press=self.logout_switch,
                                        background_color=(1, 0, 0, 1))
            self.sub_box.add_widget(logout_button)
            
        self.add_widget(self.sub_box)

    def switch_to_login(self, b):
        self.running_app.root.current = 'Login'
    
    def switch_to_registration(self, b):
        self.running_app.root.current = 'Registration'  
        
    def logout_switch(self, b):
        logout(self=self)
        self.running_app.CURRENT_USER = None
        self.running_app.build()
        self.running_app.root.current = 'Login'


class SubBox(BoxLayout):

    def __init__(self, orientation, **kwargs):
        super().__init__(**kwargs)

        self.orientation = orientation
        self.padding = (self.width * 0.2, self.height * 0.1)
        self.spacing = (self.height * 0.1)
        with self.canvas.before:
            Color(0, 0, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class LoginButton(RoundedButton):

    def __init__(self, background_color, text, **kwargs):
        super().__init__(background_color, **kwargs)

        self.text = text
        self.size_hint = (0.4, 0.2)
        self.pos_hint = {'top': 1}
        
class NavButton(RoundedButton):

    def __init__(self, background_color, text, **kwargs):
        super().__init__(background_color, **kwargs)

        self.text = text
        self.size_hint_y = None
        self.size = 0, 20
        self.pos_hint = {'top': 1}


class LoginTextInput(TextInput):

    def __init__(self, hint_text, **kwargs):
        super().__init__(**kwargs)

        self.hint_text = hint_text
        self.multiline = False
        self.size_hint_y = None
        self.size = (0, 30)
        self.pos_hint = {'center_y': 0.5}
