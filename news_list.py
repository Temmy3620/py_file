from multiprocessing import get_context
import re
import requests
from bs4 import BeautifulSoup
import datetime


    

class NewsList:
    def __init__(self):
        
        dt_now = datetime.datetime.now()#現在時刻取得
        now_month =  str(dt_now.month)#月
        now_day = str(dt_now.day)#日

        now = str(dt_now.year) + now_month.zfill(2) + now_day.zfill(2)#現在時刻を8桁で取得

        url = "https://news.yahoo.co.jp/topics/top-picks?date=" + now#主要ニュースurl
        url_it = "https://news.yahoo.co.jp/topics/it?date=" + now#ITニュースurl
        url_world ="https://news.yahoo.co.jp/topics/world?date=" + now


        response = requests.get(url)
        response_it = requests.get(url_it)
        response_world = requests.get(url_world)

        self.soup = BeautifulSoup(response.content, "html.parser")
        self.soup_it = BeautifulSoup(response_it.content, "html.parser")
        self.soup_world = BeautifulSoup(response_world.content, "html.parser")
    
    def get_article(self, news_url):
        
        response_c = requests.get(news_url)
        soup_c = BeautifulSoup(response_c.content, "html.parser")
        context = soup_c.find("p",class_ = "sc-fElddq cGSivN highLightSearchTarget")
        return context.text
 
    def news_today(self):
        today = self.soup.find("ul",class_ = "newsFeed_list")
        today_list = []#今日のニュースの見出し一覧
        for s in today:
            news_list = []#ニュースの見出しとそのURLのリスト
            news_list.append(s.text)#ニュースの見出し取得
            for s2 in s.find_all('a'):#URL取得
                news_list.append(s2.get('href'))
            today_list.append(news_list)
        today_list = [s for s in today_list if s != ['']]#なぜか['']が入るので削除
        return today_list#
    
    def news_it(self):
        today_it = self.soup_it.find("ul",class_ = "newsFeed_list")
        today_list_it = []
        for s in today_it:
            news_list = []#ニュースの見出しとそのURLのリスト
            news_list.append(s.text)
            for s2 in s.find_all('a'):#URL取得
                news_list.append(s2.get('href'))
            today_list_it.append(news_list)
        today_list_it = [s for s in today_list_it if s != ['']]#なぜか['']が入るので削除
        return today_list_it

    def news_world(self):
        today_world = self.soup_world.find("ul",class_ = "newsFeed_list")
        today_list_world = []
        for s in today_world:
            news_list = []#ニュースの見出しとそのURLのリスト
            news_list.append(s.text)
            for s2 in s.find_all('a'):#URL取得
                news_list.append(s2.get('href'))
            today_list_world.append(news_list)
        today_list_world = [s for s in today_list_world if s != ['']]#なぜか['']が入るので削除
        return today_list_world
    
    

if __name__ == '__main__':
    news = NewsList().news_world()
    news2 = NewsList().news_it()
    news3 = NewsList().news_today()
    
    print(news2[0])
    print(NewsList().get_article(news2[0][1]))
    
    
    