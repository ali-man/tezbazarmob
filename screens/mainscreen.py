from core.utils import open_file_kv
from screens.basescreen import BaseScreen

from kivy.lang import Builder
Builder.load_string(open_file_kv(__name__))


class MainScreen(BaseScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
