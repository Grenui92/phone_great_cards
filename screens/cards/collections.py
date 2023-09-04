from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from screens.cards.cards_services import get_user_collections, get_cards_from_collection
from screens.cards.collections_makets import CollectionsButton, CreationButton
from screens.main_makets import MainBox, RoundedButton

from tools.mixin import RunAppMixin


class CollectionsScreen(MainBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
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
                                                  background_color=(1, 0, 1, 1),
                                                  color=(0, 0, 0, 1),
                                                  font_size=20)

        self.add_widget(create_card_button)
        self.add_widget(create_collection_button)

        for col in self.collections:
            open_collection = CollectionsButton(text=col['name'],
                                                background_color=(0.1, 0.1, 0.1, 0.1),
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