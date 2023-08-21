from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from login import LoginWindow

class MainWindow(BoxLayout):
    pass

class GreatCardsApp(App):
    
    def build(self):
        main_window = MainWindow(orientation="vertical")
        login_window = LoginWindow(orientation="vertical", size_hint=(1, 0.1))
        main_window.add_widget(login_window)
        return main_window

    
if __name__ == "__main__":
    GreatCardsApp().run()