from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from screens.auth.login_makets import LogSubBox, LogButton, LogTextInput
from screens.cards.collections import Collections
from screens.auth.login_services import log_user, user_registration
from screens.main_makets import MainBox


class LoginScreen(BoxLayout, MainBox):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_upper_buttons()
        self.add_text_input()
        self.add_lower_buttons()

    def add_upper_buttons(self):
        self.sub_box = LogSubBox(orientation='horizontal')
        self.upper_button = LogButton(text='Registration',
                                      on_press=self.switch_registration_login,
                                      background_color=(1, 0, 0, 1))

        self.sub_box.add_widget(self.upper_button)
        self.add_widget(self.sub_box)

    def add_text_input(self):
        self.inp_box = LogSubBox(orientation='vertical')

        self.username_inp = LogTextInput(hint_text='Username')
        self.password_inp = LogTextInput(hint_text='Password')
        self.label = Label(text='Login now:', font_size='24sp',
                           color=(20/255, 20/255, 20/255, 1))

        self.inp_box.add_widget(self.label)
        self.inp_box.add_widget(self.username_inp)
        self.inp_box.add_widget(self.password_inp)
        self.add_widget(self.inp_box)

    def add_lower_buttons(self):
        self.sub_box = LogSubBox(orientation='horizontal')
        self.submit_button = LogButton(text='Submit',
                                       on_press=self.on_submit,
                                       background_color=(1, 0, 0, 1))
        self.reset_button = LogButton(text='Reset',
                                      background_color=(1, 0, 0, 1))

        self.sub_box.add_widget(self.submit_button)
        self.sub_box.add_widget(self.reset_button)
        self.add_widget(self.sub_box)

    def switch_registration_login(self):

        if self.running_app.root.current == 'Login':
            self.running_app.root.current = 'Registration'

        elif self.running_app.root.current == 'Registration':
            self.running_app.root.current = 'Login'

    def on_submit(self):
        username = self.username_inp.text
        password = self.password_inp.text
        if username and password:
            succes = log_user(self=self, username=username, password=password)
            if succes:
                collections_list = Screen(name='Colletions')
                collections_list.add_widget(Collections())

                self.running_app.screen_manager.add_widget(collections_list)
                self.running_app.root.current = 'Colletions'


class RegistrationScreen(LoginScreen):

    def add_upper_buttons(self):
        self.sub_box = LogSubBox(orientation='horizontal')
        self.upper_button = LogButton(text='Login', 
                                      on_press=self.switch_registration_login,
                                      background_color=(1, 0, 0, 1))

        self.sub_box.add_widget(self.upper_button)
        self.add_widget(self.sub_box)

    def add_text_input(self):
        self.inp_box = LogSubBox(orientation='vertical')
        self.username_inp = LogTextInput(hint_text='Username')
        self.password_inp = LogTextInput(hint_text='Password')
        self.confirm_password_inp = LogTextInput(hint_text='Confirm Password')
        self.email = LogTextInput(hint_text='Email')
        self.label = Label(text='Registration now:',
                           font_size='24sp', color=(20/255, 20/255, 20/255, 1))

        self.inp_box.add_widget(self.label)
        self.inp_box.add_widget(self.username_inp)
        self.inp_box.add_widget(self.password_inp)
        self.inp_box.add_widget(self.confirm_password_inp)
        self.inp_box.add_widget(self.email)
        self.add_widget(self.inp_box)

    def on_submit(self):
        username = self.username_inp.text
        password1 = self.password_inp.text
        password2 = self.confirm_password_inp.text
        email = self.email.text

        if all([username, password1, password2, email]):
            success = user_registration(
                self, username, password1, password2, email)
            if success:
                self.running_app.root.current = 'Login'
