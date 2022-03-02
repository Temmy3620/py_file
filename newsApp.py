from cProfile import label
from datetime import datetime

from kivy.config import Config
#ウインドウの幅と高さの設定
Config.set('graphics', 'width', 833)
Config.set('graphics', 'height', 310)
#1でサイズ変更可、0はサイズ変更不可
Config.set('graphics', 'resizable', 0)

from kivy.lang import Builder
Builder.load_file("news_app.kv")

from argparse import Action
import os
import sys

import time
import threading
from turtle import color
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar, ActionItem, ActionButton, ActionView, ActionPrevious, ActionGroup
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from pygments import highlight


import news_list
from concurrent.futures import ThreadPoolExecutor
from kivy.core.text import LabelBase, DEFAULT_FONT  # 追加分
from kivy.resources import resource_add_path  # 追加分

resource_add_path('c:/Windows/Fonts')  # 追加分
LabelBase.register(DEFAULT_FONT, 'meiryo.ttc')  # 追加分

class Re:
    def renew(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
class Pop:
    def pop(self):
        print("popup open!!")
        popup = Popup(title='News Article',content=Label(text="sssssssssssssssssssss"),
        size_hint=(None, None), size=(500, 300))
        popup.open()
        pass


class NewsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        
        self.newslist = news_list.NewsList()
        self.todaynews = self.newslist.news_today()
        self.itnews = self.newslist.news_it()
        self.worldnews = self.newslist.news_world()
        #self.article = self.newslist.get_article()
        
        
    
    
    
    def build(self):
        
       
            
        
        root = BoxLayout(orientation='vertical')
        item = Accordion()
        
        item3 = AccordionItem(title='World')
        layout = GridLayout(cols=1,size_hint=(None, None))
        layout.bind(minimum_height=layout.setter('height'))
        for i in self.worldnews:#i[0]：文字i[1]:リンク
            b1 = Button(text=i[0],size=(700, 40),size_hint=(None, None),on_release=Pop.pop)
            layout.add_widget(b1)
        #item.add_widget(b2)
        scrolv = ScrollView(size_hint=(None, None),size=(980, 260),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        scrolv.add_widget(layout)
        item3.add_widget(scrolv)
            
        item2 = AccordionItem(title='IT')#IT系の記事
        layout = GridLayout(cols=1, size_hint=(None, None))
        layout.bind(minimum_height=layout.setter('height'))
        for i in self.itnews:#i[0]：文字i[1]:リンク
            b1 = Button(text=i[0],size=(700, 40),size_hint=(None, None),on_release=Pop.pop)
            layout.add_widget(b1)
        scrolv = ScrollView(size_hint=(None, None),size=(980, 260),
            pos_hint={'center_x': .5, 'center_y': .5},do_scroll_x=False)
        scrolv.add_widget(layout)
        item2.add_widget(scrolv)
        
        item1 = AccordionItem(title='ALL')
        layout = GridLayout(cols=1, size_hint=(None, None))
        layout.bind(minimum_height=layout.setter('height'))
        for i in self.todaynews:#i[0]：ニュース　i[1]:リンク
            
            b1 = Button(text=i[0],size=(700, 40),size_hint=(None, None),
                        on_release=Pop.pop)
            layout.add_widget(b1)
        scrolv = ScrollView(size_hint=(None, None),size=(980, 260),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        scrolv.add_widget(layout)
        item1.add_widget(scrolv)
    
        
        
        item.add_widget(item3)
        item.add_widget(item2)
        item.add_widget(item1)
        
        root.add_widget(item)
        
        a_bt3 = ActionButton(text="setting",on_press=NewsApp.stop)
        a_bt2 = ActionButton(text="renew",on_press=Re.renew)
        a_bt = ActionButton(text="shutdwon",on_press=exit)
        actionp = ActionPrevious(title="news app",with_previous=False)
        actionview = ActionView()
        actionview.add_widget(actionp)
        actionview.add_widget(a_bt3)
        actionview.add_widget(a_bt2)
        actionview.add_widget(a_bt)
        
        action = ActionBar()
        
        action.add_widget(actionview)
        
        root.add_widget(action)
        
        return root


if __name__ == '__main__':
    
    NewsApp().run()
