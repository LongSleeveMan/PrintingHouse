# Project made by: Patryk Foryszewski

# import Statements
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.utils import get_color_from_hex

# Config
Config.set('graphics', 'multisamples', '0')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('kivy', 'exit_on_escape', '0')
Config.write()

# Builder used to load all the kivy files to be loaded in the main.py file
# Builder.load_file('front.kv')

#colors
light_red = '#f11f5f'
green = '#80d859'
light_blue = '#56c2f7'
lighter_blue = '#7fcdf3'
light_gray ='#f2f2f2'
white = '#ffffff'
orange = '#ff9933'


class Main(BoxLayout):
    def __init__(self,**kwargs):
        super(Main, self).__init__(**kwargs)


# mainApp class
class mainApp(App):

    def build(self):
        self.title = "PrintingHouse"
        self.load_kv('front.kv')
        return Main()


# BoilerPlate
if __name__ == '__main__':
    app = mainApp()
    app.run()