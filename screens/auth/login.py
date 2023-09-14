from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from screens.main_makets import SubBox, LoginButton, LoginTextInput
from screens.main_makets import NavButton

from screens.english.logged_screens import LoggedScreens, Collections
from screens.auth.login_services import log_user, user_registration

from tools.mixin import RunAppMixin
from tools.const import LOGIN_SCREEN_NAME, REGISTRATION_SCREEN_NAME, COLLECTIONS_SCREEN_NAME


class LoginScreen(BoxLayout, RunAppMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_nav_buttons()
        self.add_text_input()
        self.add_lower_buttons()

    def add_text_input(self):
        self.inp_box = SubBox(orientation='vertical')

        self.username_inp = LoginTextInput(hint_text='Username')
        self.password_inp = LoginTextInput(hint_text='Password')
        self.label = Label(text='Login now:', font_size='24sp',
                           color=(20/255, 20/255, 20/255, 1))

        self.inp_box.add_widget(self.label)
        self.inp_box.add_widget(self.username_inp)
        self.inp_box.add_widget(self.password_inp)
        self.add_widget(self.inp_box)

    def add_lower_buttons(self):
        self.submit_box = SubBox(orientation='horizontal')
        
        self.submit_button = LoginButton(text='Submit',
                                         on_press=self.on_submit,
                                         background_color=(1, 0, 0, 1))
        self.reset_button = LoginButton(text='Reset',
                                        on_press=self.on_reset,
                                        background_color=(1, 0, 0, 1))

        self.submit_box.add_widget(self.submit_button)
        self.submit_box.add_widget(self.reset_button)
        self.add_widget(self.submit_box)

    def add_nav_buttons(self):
        self.orientation = 'vertical'
        
        self.sub_box = SubBox(orientation='horizontal', size_hint=(1, 0.1))


        login_button = NavButton(text=LOGIN_SCREEN_NAME,
                                    on_press=self.switch_to_login,
                                    background_color=(1, 0, 0, 1))
        registration_button = NavButton(text=REGISTRATION_SCREEN_NAME,
                                        on_press=self.switch_to_registration,
                                        background_color=(1, 0, 0, 1))

        self.sub_box.add_widget(login_button)
        self.sub_box.add_widget(registration_button)
        
        self.add_widget(self.sub_box)
        

    def on_submit(self, button):
        username = self.username_inp.text
        password = self.password_inp.text
        if username and password:
            user = log_user(self=self, username=username, password=password)
            if user:
                self.running_app.CURRENT_USER = user
                collections_list = Screen(name=COLLECTIONS_SCREEN_NAME)
                collections_list.add_widget(LoggedScreens(widget_class=Collections))

                self.running_app.screen_manager.add_widget(collections_list)
                self.running_app.root.current = COLLECTIONS_SCREEN_NAME

    def on_reset(self, button):
        self.username_inp.text = ''
        self.password_inp.text = ''


    def switch_to_login(self, b):
        self.running_app.root.current = LOGIN_SCREEN_NAME

    def switch_to_registration(self, b):
        self.running_app.root.current = REGISTRATION_SCREEN_NAME


class RegistrationScreen(LoginScreen):

    def add_text_input(self):
        self.inp_box = SubBox(orientation='vertical')
        self.username_inp = LoginTextInput(hint_text='Username')
        self.password_inp = LoginTextInput(hint_text='Password')
        self.confirm_password_inp = LoginTextInput(
            hint_text='Confirm Password')
        self.email = LoginTextInput(hint_text='Email')
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
                self.running_app.root.current = LOGIN_SCREEN_NAME

    def on_reset(self, button):
        self.username_inp.text = ''
        self.password_inp.text = ''
        self.confirm_password_inp.text = ''
        self.email.text = ''