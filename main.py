# Project made by: Patryk Foryszewski

# import Statements
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import os
from PIL import Image
from kivy.utils import get_color_from_hex

# Config
Config.set('graphics', 'multisamples', '0')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '720')
Config.set('kivy', 'exit_on_escape', '0')
Config.write()

# Builder used to load all the kivy files to be loaded in the main.py file

# colors
light_red = '#f11f5f'
green = '#80d859'
light_blue = '#56c2f7'
lighter_blue = '#7fcdf3'
light_gray = '#f2f2f2'
white = '#ffffff'
orange = '#ff9933'


class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)

    def proces1(self):
        print('Proces1')

    def resize(self):
        print('RESIZE')
        image = Image.open(self.path)
        path = str(self.path)
        size_x = self.ids.project_view.size[0]
        print('     Image size', image.size)
        coef = size_x/image.size[0]
        base, file = os.path.split(path)
        file = str(file)
        print('     File1', file, type(file))
        file = file.split('.')
        print('     File2', file)
        thumb_size = [image.size[0]*coef, image.size[1]*coef]
        image.thumbnail(thumb_size)
        self.ids.project_view.size = thumb_size

        dir = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], '/Desktop/PrintingHouse/Thumbs')
        print('     Dir', dir)
        if not os.path.exists(dir):
            print('     Path not exists')
            os.makedirs(dir)
        else:
            print('     Path exists')
        print('     str', str(file[0]))
        path = os.path.join(dir, '{}.png'.format(str(file[0])))
        print('     Path', path)     
        image.save(path)
        self.ids.project_view.source = path


    def _on_file_drop(self, window, path):
        print('FILE PATH', path)
        self.path = path
        self.resize()

# mainApp class
class MainApp(App):

    def build(self):
        self.title = "PrintingHouse"
        self.load_kv('front.kv')
        return Main()


# BoilerPlate
if __name__ == '__main__':
    app = MainApp()
    app.run()