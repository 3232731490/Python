import requests
from bs4 import BeautifulSoup
class DoubanSpider:
    def __init__(self):
        self.url='https://movie.douban.com/top250?start='
        self.begin=0
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'}

    def get_top(self,i):
        fullurl=self.url+str(i*25)
        html=requests.get(fullurl, headers=self.headers)
        soup=BeautifulSoup(html.content, 'html.parser')
        name=soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span')

        for i in name:
            print(i.get_text())

    def get_top250(self, i):
        for index in range(i):
            self.get_top(index)


if __name__=="__main__":
    spider=DoubanSpider()
    spider.get_top250(10)