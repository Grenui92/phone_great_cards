from kivy.app import App

class RunAppMixin:
    def __init__(self):
        self.running_app = App.get_running_app()
        