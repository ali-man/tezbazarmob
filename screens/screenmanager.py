from kivy.uix.screenmanager import ScreenManager

from screens.categoryscreen import CategoryScreen
from screens.mainscreen import MainScreen
from screens.productscreen import ProductScreen

sm = ScreenManager()
screens = {
    'main': MainScreen,
    'category': CategoryScreen,
    'product': ProductScreen,
}
