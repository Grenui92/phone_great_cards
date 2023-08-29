
from kivy.uix.label import Label
from kivy.uix.button import Button

from screens.main_window import MainBox

from screens.cards.cards_services import get_user_collections


class CollectionsList(MainBox):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.collections = get_user_collections(self)

        for col in self.collections:
            lab = Button(text=col['name'])
            self.add_widget(lab)

        
