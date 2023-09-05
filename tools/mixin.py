from kivy.app import App

from screens.auth.login_services import logout

class RunAppMixin:
    def __init__(self):
        self.running_app = App.get_running_app()

