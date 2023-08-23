from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class MainWindow(BoxLayout):
    pass

class GreatCardsApp(App):
    
    def build(self):
        main_window = MainWindow()
        return main_window

    
if __name__ == "__main__":
    GreatCardsApp().run()