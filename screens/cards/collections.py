from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from screens.cards.cards_services import get_user_collections, get_cards_from_collection
from screens.cards.collections_makets import CollectionsButton, CreationButton
from screens.main_makets import NavButton, SubBox

from tools.mixin import RunAppMixin
from screens.auth.login_services import logout

class LoggedNavigation():        

    def add_nav_buttons(self):
        self.sub_box = SubBox(orientation='horizontal', size_hint=(1, 0.1))
        logout_button = NavButton(text='Logout',
                                  on_press=self.logout_switch,
                                  background_color=(1, 0, 0, 1))
        english_cards_button = NavButton(text='Cards',
                                         on_press=self.logout_switch,
                                         background_color=(0, 0, 1, 1))
        chat_button = NavButton(text='Chat',
                                on_press=self.logout_switch,
                                background_color=(0, 0, 1, 1))
        day_words = NavButton(text='Words',
                              on_press=self.logout_switch,
                              background_color=(0, 0, 1, 1))

        self.sub_box.add_widget(english_cards_button)
        self.sub_box.add_widget(chat_button)
        self.sub_box.add_widget(day_words)
        self.sub_box.add_widget(logout_button)

        self.add_widget(self.sub_box)


    def logout_switch(self, b):
        
        logout(self=self)
        self.running_app.root.current = 'Login'
        
        
class CollectionsScreen(BoxLayout, LoggedNavigation, RunAppMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_nav_buttons()
        collections = get_user_collections(self=self)
        self.add_widget(Collections(collections=collections))



class Collections(GridLayout, RunAppMixin):

    def __init__(self, collections, **kwargs):
        super().__init__(**kwargs)
        
        self.collections = collections

        self.cols = 2
        self.padding = 10
        self.spacing = 10
        self.rows = len(self.collections) + 1

        create_card_button = CreationButton(text='Create Card',
                                            background_color=(1, 0, 1, 1),
                                            color=(0, 0, 0, 1),
                                            font_size=20)
        create_collection_button = CreationButton(text='Create Collection',
                                                  background_color=(
                                                      1, 0, 1, 1),
                                                  color=(0, 0, 0, 1),
                                                  font_size=20)

        self.add_widget(create_card_button)
        self.add_widget(create_collection_button)

        for col in self.collections:
            open_collection = CollectionsButton(text=col['name'],
                                                background_color=(
                                                    0.1, 0.1, 0.1, 0.1),
                                                on_press=self.open_collection_button)
            open_collection.data = col
            edit_colleciton = CollectionsButton(text=f'Edit',
                                                background_color=(0.1, 0.1, 0.1, 0.1))
            edit_colleciton.data = col

            self.add_widget(open_collection)
            self.add_widget(edit_colleciton)



    def open_collection_button(self, instance):
        result = get_cards_from_collection(self, instance.data)
        for k in result:
            print(k)
