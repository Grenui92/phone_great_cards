
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from screens.auth.login_services import logout
from screens.english.cards.cards_services import get_user_collections
from screens.english.cards.collections import Collections
from screens.main_makets import NavButton, SubBox

from tools.mixin import RunAppMixin
from tools.const import LOGIN_SCREEN_NAME, COLLECTIONS_SCREEN_NAME


class LoggedNavigation(RunAppMixin):        

    def add_nav_buttons(self):
        self.sub_box = SubBox(orientation='horizontal', size_hint=(1, 0.1))
        logout_button = NavButton(text='Logout',
                                  on_press=self.logout_switch,
                                  background_color=(1, 0, 0, 1))
        english_cards_button = NavButton(text='Cards',
                                         on_press=self.cards_on_press,
                                         background_color=(0, 0, 1, 1))
        chat_button = NavButton(text='Chat',
                                on_press=self.chat_on_press,
                                background_color=(0, 0, 1, 1))
        day_words = NavButton(text='Words',
                              on_press=self.words_on_press,
                              background_color=(0, 0, 1, 1))

        self.sub_box.add_widget(english_cards_button)
        self.sub_box.add_widget(chat_button)
        self.sub_box.add_widget(day_words)
        self.sub_box.add_widget(logout_button)
        self.add_widget(self.sub_box)


    def logout_switch(self, b):
        logout(self=self)
        self.running_app.root.current = LOGIN_SCREEN_NAME

    def create_screens(self):
        collections_screen = Screen(name=COLLECTIONS_SCREEN_NAME)
        collections_screen.add_widget(CollectionsScreen())
        self.running_app.screen_manager.add_widget(collections_screen)
        
    def cards_on_press(self, b):
        self.running_app.root.current = COLLECTIONS_SCREEN_NAME
    
    def chat_on_press(self, b):
        pass
    
    def words_on_press(self, b):
        pass

        
class CollectionsScreen(BoxLayout, LoggedNavigation, RunAppMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_nav_buttons()
        collections = get_user_collections(self=self)
        self.add_widget(Collections(collections=collections))
        

