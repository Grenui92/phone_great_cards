
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

from screens.main_window import MainBox
from screens.cards.cards_services import get_user_collections
from screens.auth.login_makets import LogButton


class CollectionsList(MainBox):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.collections = get_user_collections(self)

        for col in self.collections:

            one_collection = Collection(col)
            
            
            self.add_widget(one_collection)


class Collection(MainBox):
    
    def __init__(self, colleciton, **kwargs):
        super().__init__(**kwargs)
        
        
        with self.canvas.before:
            Color(1, 0, 0, 0.5)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            
        self.bind(pos=self.update_rect, size=self.update_rect)


        self.orientation = 'horizontal'
        
        open_collection = CollectionsButton(text=colleciton['name'], background_color=(0, 0, 0, 0))
        edit_colleciton = CollectionsButton(text=f'Edit')
        
        self.add_widget(open_collection)
        self.add_widget(edit_colleciton)
        
        
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

        
class CollectionsButton(Button):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.size_hint_y = 0.4

        self.pos_hint = {'top': 1}