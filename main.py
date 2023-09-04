from dotenv import dotenv_values

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window

from screens.auth.login import LoginScreen, RegistrationScreen
from screens.cards.collections import CollectionsScreen
from screens.auth.login_services import get_logged_user

Window.size = (450, 800)
Window.clearcolor = (0.913, 1, 0.674, 1)


class GreatCardsApp(App):

    main_api_url = dotenv_values().get('MAIN_API_URL')

    def build(self):

        self.screen_manager = ScreenManager()

        login_screen = Screen(name='Login')
        registration_screen = Screen(name='Registration')

        self.CURRENT_USER = get_logged_user()
        if self.CURRENT_USER:
            collections_list = Screen(name='Collections')
            collections_list.add_widget(CollectionsScreen())
            self.screen_manager.add_widget(collections_list)
            
        login_screen.add_widget(LoginScreen())
        registration_screen.add_widget(RegistrationScreen())

        self.screen_manager.add_widget(login_screen)
        self.screen_manager.add_widget(registration_screen)

        return self.screen_manager


if __name__ == "__main__":
    GreatCardsApp().run()
