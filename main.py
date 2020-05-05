# Project made by: Patryk Foryszewski

# import Statements
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.core.window import Window
import os
from PIL import Image
import math

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

class Img(BoxLayout):

    def __init__(self, angle, source, coef_x, coef_y, **kwargs):
        super(Img, self).__init__(**kwargs)
        self.angle = angle
        self.source = source
        self.coef_x = coef_x
        self.coef_y = coef_y

class Main(BoxLayout):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        Window.bind(on_dropfile=self._on_file_drop)

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
        dir = '{}/{}//Desktop/PrintingHouse/Thumbs/'.format(os.environ['HOMEDRIVE'],os.environ["HOMEPATH"])
        print('     Dir', dir)
        if not os.path.exists(dir):
            print('     Path not exists')
            os.makedirs(dir)
        else:
            print('     Path exists')
        print('     str', str(file[0]))
        self.path = os.path.join(dir, '{}.png'.format(str(file[0])))
        print('     Path', self.path)


        image.save(self.path)
        self.ids.project_view.source = self.path

    def int_valid(self, x):

        try:
            int(x)
        except:
            return 0
        else:
            return 1

    def calculate(self):
        print('CALCULATE')
        width = self.ids.width.text
        height = self.ids.height.text
        margins = self.ids.margins.text
        sheet_x = self.ids.sheet_x.text
        sheet_y = self.ids.sheet_y.text

        text = ""
        if not self.int_valid(width):
            text = 'Szerokość niepoprawna\n'
        if not self.int_valid(height):
            text += 'Wysokość niepoprawna\n'
        if not self.int_valid(margins):
            text += 'Margines niepoprawny\n'
        if not self.int_valid(sheet_x):
            text += 'Szerokość arkusza niepoprawna\n'
        if not self.int_valid(sheet_y):
            text += 'Wysokość arkusza niepoprawna\n'

        if text == "":
            width = int(width)
            height = int(height)
            margins = int(margins)
            sheet_x = int(sheet_x)
            sheet_y = int(sheet_y)

            print('     widht', width, 'height', height, 'margins', margins, 'sheet_x', sheet_x, 'sheet_y', sheet_y)

            xx = int(sheet_x / (width + margins)) * int(sheet_y / (height + margins))
            xy = int(sheet_y / (width + margins)) * int(sheet_x / (height + margins))

            print('     xx', xx, 'xy', xy)

            project_y = 0.7 * self.ids.layout.height
            project_x = project_y * (sheet_x / sheet_y)
            self.ids.project_space.size = (project_x, project_y)

            if xx > xy:
                cols = int(sheet_x / (width + margins))
                rows = int(sheet_y / (height+ margins))
                layout_x = cols * ((width + margins) / sheet_x) * project_x
                layout_y = rows * ((height + margins) / sheet_y) * project_y
                angle = 0

            else:
                print('     else', height + margins, '/', width + margins)
                cols = int(sheet_x / (height + margins))
                rows = int(sheet_y / (width + margins))
                layout_x = cols * ((height + margins) / sheet_x) * project_x
                layout_y = rows * ((width + margins) / sheet_y) * project_y
                angle = 90

            print('     cols', cols, 'rows', rows)

            layout = GridLayout(cols=cols, rows=rows, size_hint=(None, None), spacing=1)

            layout.size = (layout_x, layout_y)
            print('     project size',self.ids.project_space.size, 'layout size',  self.ids.layout.size)

            coef_x = width / (width + 2 * margins)
            coef_y = height / (height + 2* margins)
            print('     project size', self.ids.project_space.size, 'layout size', self.ids.layout.size, coef_x, coef_y)
            for i in range(cols*rows):
                img = Img(angle=angle, source=self.path, coef_x=coef_x, coef_y=coef_y  )
                layout.add_widget(img)

            self.ids.project_space.add_widget(layout)
            print("CALCULATIONS", cols, rows)
        else:
            print('Text:\n', text)

        #coef_x = int(sheet_x / height)
        #coef_y = int(sheet_y / width)


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