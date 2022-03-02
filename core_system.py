import threading
import news_list
from datetime import datetime

class Newsrenew:
    """
    ニュースリストを更新する
    """
    def start(self):
        t = threading.Thread(target=self.news_get)
        t.start()
    
    def news_get(self):
        
            
        print("get_news_list!" + str(datetime.now()))
        newslist = news_list.NewsList()
        self.todaynews = newslist.news_today()
        self.itnews = newslist.news_it()
        self.worldnews = newslist.news_world()
        