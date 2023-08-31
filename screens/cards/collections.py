from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from screens.cards.cards_services import get_user_collections
from screens.cards.collections_makets import CollectionsButton
from screens.main_makets import MainBox

class Collections(GridLayout, MainBox):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 2
        self.spacing = 10
        self.collections = get_user_collections(self=self)
        self.rows = len(self.collections)
        
        for col in self.collections:
            open_collection = Button(text=col['name'], background_color = (0, 0, 0, 0))
            edit_colleciton = CollectionsButton(text=f'Edit')
            
            self.add_widget(open_collection)
            self.add_widget(edit_colleciton)
        
        self.size_hint = 1, None
        self.height = 50 * self.rows
