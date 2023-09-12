from kivy.uix.gridlayout import GridLayout

from tools.mixin import RunAppMixin
from screens.english.cards.collections_makets import CreationButton, CollectionsButton
from screens.english.cards.cards_services import get_cards_from_collection

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