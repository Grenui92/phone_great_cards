from dotenv import dotenv_values

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window

from screens.auth.login import LoginScreen, RegistrationScreen
from screens.english.logged_screens import CollectionsScreen
from screens.auth.login_services import get_logged_user
from tools.const import LOGIN_SCREEN_NAME, REGISTRATION_SCREEN_NAME, COLLECTIONS_SCREEN_NAME
Window.size = (450, 800)
Window.clearcolor = (0.913, 1, 0.674, 1)


class GreatCardsApp(App):

    main_api_url = dotenv_values().get('MAIN_API_URL')

    def build(self):

        self.screen_manager = ScreenManager()

        self.CURRENT_USER = get_logged_user()
        
        if self.CURRENT_USER:
            logged_screen_init = CollectionsScreen()
            logged_screen = Screen(name=COLLECTIONS_SCREEN_NAME)
            logged_screen.add_widget(logged_screen_init)

            self.screen_manager.add_widget(logged_screen)

        login_screen = Screen(name=LOGIN_SCREEN_NAME)
        registration_screen = Screen(name=REGISTRATION_SCREEN_NAME)
        
        login_screen.add_widget(LoginScreen())
        registration_screen.add_widget(RegistrationScreen())

        self.screen_manager.add_widget(login_screen)
        self.screen_manager.add_widget(registration_screen)

        return self.screen_manager


if __name__ == "__main__":
    GreatCardsApp().run()
