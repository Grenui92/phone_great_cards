from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from screens.cards.cards_services import get_user_collections
from screens.cards.collections_makets import CollectionsButton, CreationButton
from screens.main_makets import MainBox, RoundedButton


class CollectionsScreen(MainBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        collections = get_user_collections(self=self)
        self.add_widget(Collections(collections=collections))

class Collections(GridLayout):
    
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
                                                background_color=(0.1, 0.1, 0.1, 0.1))
            edit_colleciton = CollectionsButton(text=f'Edit',
                                                background_color=(0.1, 0.1, 0.1, 0.1))

            self.add_widget(open_collection)
            self.add_widget(edit_colleciton)

