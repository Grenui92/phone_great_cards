from kivy.uix.screenmanager import Screen, ScreenManagerException
def switch_to_other_screen(BaseClass: str, InnerClass, screen_name, self,  *args, **kwargs):
    try:
        print(1)
        cur_screen = self.running_app.screen_manager.get_screen(screen_name)
        self.running_app.screen_manager.remove_widget(cur_screen)
    except ScreenManagerException:
        pass
    collections_screen = Screen(name=screen_name)
    collections_screen.add_widget(BaseClass(widget_class=InnerClass, *args, **kwargs))
    self.running_app.screen_manager.add_widget(collections_screen)
    self.running_app.root.current = screen_name
    