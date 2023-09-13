
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


from screens.auth.login_services import logout
from screens.english.cards_services import get_user_collections, get_cards_from_collection
from screens.main_makets import NavButton, SubBox, CreationButton, CollectionsButton

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

    def cards_on_press(self, b):
        if COLLECTIONS_SCREEN_NAME not in self.running_app.root.screen_names:
            collections_screen = Screen(name=COLLECTIONS_SCREEN_NAME)
            collections_screen.add_widget(CollectionsScreen())
            self.running_app.screen_manager.add_widget(collections_screen)
        self.running_app.root.current = COLLECTIONS_SCREEN_NAME

    def chat_on_press(self, b):
        pass

    def words_on_press(self, b):
        pass


class CollectionsScreen(BoxLayout, LoggedNavigation):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_nav_buttons()
        collections = get_user_collections(self=self)
        self.add_widget(Collections(collections=collections))


class OpenCollecitonScreen(BoxLayout, LoggedNavigation):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_nav_buttons()


# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111

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
        collection, cards = get_cards_from_collection(self, instance.data)
        open_c = Screen(name='Open')
        open_c.add_widget(OpenCollection(collection=collection, cards=cards))
        self.running_app.screen_manager.add_widget(open_c)
        self.running_app.root.current = 'Open'


class OpenCollection(BoxLayout, RunAppMixin):

    def __init__(self, collection, cards, **kwargs):
        super().__init__(**kwargs)

        self.collection = collection
        self.collection_order_list = collection['order_list']
        self.cards = cards
        self.orientation = 'vertical'

        label = Label(text=collection['name'])

        self.add_widget(label)
        self.create_card_window()
        
    def create_card_window(self):
        self.translate_window = SubBox(orientation='vertical')
        cards_buttons = SubBox(orientation='horizontal')
        
        self.current_card = self.cards[self.collection_order_list[0]-1]
        self.english_card_text = self.current_card['english_word']
        self.russian_card_text = self.current_card['russian_word']
        
        self.language_flag = 'English'        
        self.word = Label(text=self.english_card_text)   
             
        translate_button = CreationButton(text='Translate',
                                          background_color=(0, 1, 0.5, 1),
                                          on_press=self.translate_words)
        i_know_button = CreationButton(text='I know',
                                       background_color=(0, 1, 0.5, 1),
                                       on_press=self.i_know_word)
        remind_button = CreationButton(text='Remind',
                                       background_color=(0, 1, 0.5, 1),
                                       on_press=self.remind_word)

        cards_buttons.add_widget(i_know_button)
        cards_buttons.add_widget(remind_button)

        self.translate_window.add_widget(self.word)
        self.translate_window.add_widget(translate_button)
        self.translate_window.add_widget(cards_buttons)

        self.add_widget(self.translate_window)

    def translate_words(self, instance):
        if self.language_flag == 'English':
            self.word.text = self.russian_card_text
            self.language_flag = 'Russian'

        elif self.language_flag == 'Russian':
            self.word.text = self.english_card_text
            self.language_flag = 'English'

    def i_know_word(self, instance):
        
        self.collection_order_list.append(self.collection_order_list[0])
        self.collection_order_list = self.collection_order_list[1:]
        self.remove_widget(self.translate_window)
        self.create_card_window()

    def remind_word(self, instance):
        
        self.collection_order_list.insert(2 ,self.collection_order_list[0])
        self.collection_order_list = self.collection_order_list[1:]
        self.remove_widget(self.translate_window)
        self.create_card_window()
