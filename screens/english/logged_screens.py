
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from screens.auth.login_services import logout
from screens.english.cards_services import get_user_collections, get_cards_from_collection, change_card_position
from screens.english.cards_services import create_card, get_card_information
from screens.main_makets import NavButton, SubBox, CreationButton, CollectionsButton, LoginTextInput
from screens.main_makets import LoginButton, ConfirmLabel

from tools.mixin import RunAppMixin
from tools.const import LOGIN_SCREEN_NAME, COLLECTIONS_SCREEN_NAME
from tools.colors import Colors


class LoggedScreens(BoxLayout, RunAppMixin):

    def __init__(self, widget_class, *args, **kwargs):
        super().__init__()
        self.orientation = 'vertical'
        self.add_nav_buttons()
        self.create_main_widget(widget_class, **kwargs)

    def add_nav_buttons(self):
        self.sub_box = SubBox(orientation='horizontal', size_hint=(1, 0.1))
        logout_button = NavButton(text='Logout',
                                  on_press=self.logout_switch,
                                  background_color=(1, 0, 0, 1))
        english_cards_button = NavButton(text='Cards',
                                         on_press=self.cards_on_press,
                                         background_color=Colors.blue)
        chat_button = NavButton(text='Chat',
                                on_press=self.chat_on_press,
                                background_color=Colors.blue)
        day_words = NavButton(text='Words',
                              on_press=self.words_on_press,
                              background_color=Colors.blue)

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
            collections_screen.add_widget(
                LoggedScreens(widget_class=Collections))
            self.running_app.screen_manager.add_widget(collections_screen)
        self.running_app.root.current = COLLECTIONS_SCREEN_NAME

    def chat_on_press(self, b):
        pass

    def words_on_press(self, b):
        pass

    def create_main_widget(self, widget_class, **kwargs):
        main_widget = widget_class(**kwargs)
        self.add_widget(main_widget)

# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111
# 1111111111111111111111111111111111111111111111111111111111111111111


class Collections(GridLayout, RunAppMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        collections = get_user_collections(self=self)
        self.collections = collections

        self.cols = 2
        self.padding = 10
        self.spacing = 10
        self.rows = len(self.collections) + 1

        create_card_button = CreationButton(text='Create Card',
                                            background_color=Colors.pink,
                                            color=Colors.black,
                                            font_size=20,
                                            on_press=self.create_card_button)
        create_collection_button = CreationButton(text='Create Collection',
                                                  background_color=Colors.pink,
                                                  color=Colors.black,
                                                  font_size=20)

        self.add_widget(create_card_button)
        self.add_widget(create_collection_button)

        for col in self.collections:
            open_collection = CollectionsButton(text=col['name'],
                                                background_color=Colors.gray,
                                                on_press=self.open_collection_button)
            open_collection.data = col
            edit_colleciton = CollectionsButton(text=f'Edit',
                                                background_color=Colors.gray)
            edit_colleciton.data = col

            self.add_widget(open_collection)
            self.add_widget(edit_colleciton)

    def open_collection_button(self, instance):

        collection, cards = get_cards_from_collection(self, instance.data)

        open_c = Screen(name=f'Open{collection["id"]}')

        open_c.add_widget(LoggedScreens(
            widget_class=OpenCollection, collection=collection, cards=cards))

        self.running_app.screen_manager.add_widget(open_c)
        self.running_app.root.current = f'Open{collection["id"]}'

    def create_card_button(self, instance):
        create_card_screen = Screen(name='CreateCard')
        create_card_screen.add_widget(LoggedScreens(widget_class=CreateCard))
        self.running_app.screen_manager.add_widget(create_card_screen)
        self.running_app.root.current = 'CreateCard'


class OpenCollection(BoxLayout, RunAppMixin):

    def __init__(self, collection, cards, **kwargs):
        super().__init__(**kwargs)

        self.collection = collection

        self.cards = cards
        self.orientation = 'vertical'

        label = Label(text=collection['name'], size_hint=(1, 0.05))

        self.add_widget(label)
        self.create_card_window()

    def create_card_window(self):
        
        self.translate_window = SubBox(orientation='vertical')
        
        self.collection_order_list = self.collection['order_list']

        if self.collection_order_list:
            self.current_card = list(filter(lambda col: (col['id'] == self.collection_order_list[0]), self.cards))[0]

        else:
            self.current_card = {'english_word': 'Empty collection. Create card and add to the collection', 
                                 'russian_word': 'Empty collection Create card and add to the collection', 
                                 'id': 666}     
                   
        self.english_card_text = self.current_card['english_word']
        self.russian_card_text = self.current_card['russian_word']

        self.language_flag = 'English'
        self.word = Label(text=self.english_card_text)
        self.translate_window.add_widget(self.word)
        
        if self.collection_order_list:
            self.add_buttons()
            
        self.add_widget(self.translate_window)
         
    def add_buttons(self):
        cards_buttons = SubBox(orientation='horizontal')

        

        translate_button = CreationButton(text='Translate',
                                          background_color=Colors.for_buttons,
                                          on_press=self.translate_words)
        i_know_button = CreationButton(text='I know',
                                       background_color=Colors.for_buttons,
                                       on_press=self.i_know_word)
        remind_button = CreationButton(text='Remind',
                                       background_color=Colors.for_buttons,
                                       on_press=self.remind_word)

        cards_buttons.add_widget(i_know_button)
        cards_buttons.add_widget(remind_button)
  
        self.translate_window.add_widget(translate_button)
        self.translate_window.add_widget(cards_buttons)

        
                
    def translate_words(self, instance):
        if self.language_flag == 'English':
            self.word.text = self.russian_card_text
            self.language_flag = 'Russian'

        elif self.language_flag == 'Russian':
            self.word.text = self.english_card_text
            self.language_flag = 'English'

    def i_know_word(self, instance):
        self.collection = change_card_position(self,
                                               replace=1,
                                               word_id=self.current_card['id'],
                                               collection_id=self.collection['id'])

        self.remove_widget(self.translate_window)
        self.create_card_window()

    def remind_word(self, instance):
        self.collection = change_card_position(self,
                                               replace=0,
                                               word_id=self.current_card['id'],
                                               collection_id=self.collection['id'])

        self.remove_widget(self.translate_window)
        self.create_card_window()


class CreateCard(BoxLayout, RunAppMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_form_inputs()
        self.add_form_buttons()

    def add_form_inputs(self):
        self.collections = get_user_collections(self=self)

        self.creation_form = SubBox(orientation='vertical',
                                    pos_hint={'top': 1})
        self.english_word = LoginTextInput(hint_text='English word')
        self.russian_word = LoginTextInput(hint_text='Russian word')
        self.word_usage = LoginTextInput(hint_text='Word usage')
        self.selected_collection = Spinner(text='Select collection',
                                           values=(col['name']
                                                   for col in self.collections),
                                           size_hint_y=None,
                                           size=(0, 30))
        self.creation_form.add_widget(self.english_word)
        self.creation_form.add_widget(self.russian_word)
        self.creation_form.add_widget(self.word_usage)
        self.creation_form.add_widget(self.selected_collection)
        self.add_widget(self.creation_form)

    def add_form_buttons(self):
        buttons = SubBox(orientation='horizontal')

        submit_button = LoginButton(text='Submit',
                                    background_color=Colors.for_buttons,
                                    color=Colors.black,
                                    on_press=self.on_submit)
        reset_button = LoginButton(text='Reset',
                                   background_color=Colors.for_buttons,
                                   color=Colors.black,
                                   on_press=self.on_reset)

        buttons.add_widget(submit_button)
        buttons.add_widget(reset_button)

        self.add_widget(buttons)

    def on_submit(self, instance):
        col = list(filter(lambda x: (
            x['name'] == self.selected_collection.text), self.collections))
        if col:
            card = get_card_information(self=self, collection_id=col[0]['id'])
            confirm_screen = Screen(name='Confirm creation')
            confirm_screen.add_widget(LoggedScreens(widget_class=ConfirmCardCreation,
                                                    card=card,
                                                    collection=col[0]))
            self.running_app.screen_manager.add_widget(confirm_screen)
            self.running_app.root.current = 'Confirm creation'

        else:
            self.creation_form.add_widget(
                Label(text='You have to choice colelction'))

    def on_reset(self, instance):
        self.english_word.text = ''
        self.russian_word.text = ''
        self.word_usage.text = ''


class ConfirmCardCreation(BoxLayout, RunAppMixin):

    def __init__(self, card, collection, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.card = card
        self.collection = collection

        self.add_card_inform()
        self.add_buttons()

    def add_card_inform(self):

        self.info_box = SubBox(orientation='vertical', size=self.size)
        en_label = ConfirmLabel(text=f'English word:\n{self.card.get("english_word")}', 
                                background_color=Colors.red,
                                color=Colors.black)
        ru_label = ConfirmLabel(text=f'Russian word:\n{self.card.get("russian_word")}', 
                                background_color=Colors.red,
                                color=Colors.black)
        us_label = ConfirmLabel(text=f'Word usage:\n{self.card.get("word_usage")}', 
                                background_color=Colors.red,
                                color=Colors.black)
        col_label = ConfirmLabel(text=f'Collection:\n{self.collection["name"]}', 
                                 background_color=Colors.red,
                                 color=Colors.black)
        self.info_box.add_widget(en_label)
        self.info_box.add_widget(ru_label)
        self.info_box.add_widget(us_label)
        self.info_box.add_widget(col_label)
        self.add_widget(self.info_box)

    def add_buttons(self):
        buttons = SubBox(orientation='horizontal')

        submit_button = LoginButton(text='Submit',
                                    background_color=Colors.for_buttons,
                                    color=Colors.black,
                                    on_press=self.on_submit)
        reset_button = LoginButton(text='Reset',
                                   background_color=Colors.for_buttons,
                                   color=Colors.black,
                                   on_press=self.on_reset)

        buttons.add_widget(submit_button)
        buttons.add_widget(reset_button)

        self.add_widget(buttons)

    def on_submit(self, instance):
        result = create_card(self=self, card=self.card, collection_id=self.collection['id'])
        self.running_app.root.current = COLLECTIONS_SCREEN_NAME

    def on_reset(self, instance):
        pass
