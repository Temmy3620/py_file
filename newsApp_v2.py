from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 300)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

Builder.load_file('newsApp_v2.kv')

class TestWidget(BoxLayout):
    
    pass

class TestGrid(GridLayout):
    pass

class NewButton(Button):
    pass

class SampleBoxApp(App):
    def build(self):
        self.root = TestWidget()
        
        
        return self.root

if __name__ == '__main__':
    SampleBoxApp().run()