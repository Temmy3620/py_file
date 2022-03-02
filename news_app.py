from tkinter import Scrollbar
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from pygments import highlight
import news_list
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分

resource_add_path('c:/Windows/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'msgothic.ttc')  # 追加分

#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 300)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 1)

class NewsButton(Button):
    orientation='vertical'
    def on_press(self):
        pass


class NewsApp(App):
    
     
    def build(self):
        newslist = news_list.NewsList()
        self.todaynews = newslist.news_today()
        self.itnews = newslist.news_it()
        self.worldnews = newslist.news_world()
        
        root = Accordion()
        item3 = AccordionItem(title='World News')
        button = BoxLayout(orientation='vertical')
        for i in self.worldnews:#i[0]：文字i[1]:リンク
            b1 = Button(text=str(i[0]))
            button.add_widget(b1)
        item3.add_widget(button)
        
        item2 = AccordionItem(title='IT News')
        button = BoxLayout(orientation='vertical')
        button.bind(minimum_height=button.setter('height'))
        for i in self.itnews:#i[0]：文字i[1]:リンク
            b1 = Button(text=str(i[0]),)
            button.add_widget(b1)
        item2.add_widget(button)
            
        
        
        item = AccordionItem(title='News')
        button = BoxLayout(orientation='vertical')
        for i in self.todaynews:#i[0]：文字i[1]:リンク
            b1 = Button(text=str(i[0]))
            button.add_widget(b1)
        #item.add_widget(b2)
        
        
        item.add_widget(button)
    
        
        
        root.add_widget(item3)
        root.add_widget(item2)
        root.add_widget(item)
        
        return root


if __name__ == '__main__':
    NewsApp().run()
