
from kivy.uix.label import Label

from screens.main_window import MainBox


class CollectionsList(MainBox):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username_label = Label(
            text=self.running_app.CURRENT_USER.username, color=(0, 0, 0, 1))
        self.add_widget(self.username_label)
