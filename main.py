import os

from kivymd.app import MDApp

from screens.screenmanager import sm, screens


class MainApp(MDApp):
    screen_manager = None

    def __init__(self, **kwargs):
        self.title = "My Material Application"
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "DeepPurple"
        super().__init__(**kwargs)

    def init_app(self):
        self.screen_manager = sm
        self.switch_screen('main')

    def switch_screen(self, name_screen):
        if name_screen in screens.keys():
            screen = screens[name_screen](name=name_screen)
            self.screen_manager.switch_to(screen)

    def build(self):
        # self.theme_cls.theme_style = 'Light'
        self.init_app()
        return self.screen_manager

    @staticmethod
    def file_kv(val):
        val = val.split('.')
        path = '{}/kv/{}.kv'.format(val[0], val[1])
        return path


if __name__ == '__main__':
    MainApp().run()
