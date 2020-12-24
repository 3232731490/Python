import urllib.request as ur
import urllib.parse as up
import re

class Spider:
    def __init__(self, location):
        self.page=1
        self.switch=True
        self.location=up.quote(location, encoding="utf-8")

    def loadPage(self):
        print("正在查询天气中......")
        url="https://www.msn.cn/zh-cn/weather/today/Shanghai,Shanghai,China/we-city?iso=CN&form=PRWLAS&q="+self.location+"&el=akzE4OlgQ5tXfuusp%2FUZxQ%3D%3D"
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68'}
        request=ur.Request(url, headers=headers)
        response=ur.urlopen(request)
        html=response.read().decode("utf-8")
        pattern1=re.compile('<div class="dt">(.*?)</div>', re.S)
        pattern2=re.compile('<li>\s*<p>(.*?)class="transparent">(.*?)</li>', re.S)
        date_list=pattern1.findall(html)
        tempreture_list=pattern2.findall(html)
        self.dealHtml(date_list,tempreture_list)

    def dealHtml(self, date_list, tempreture_list):
        pattern=re.compile("\d{1,2}&")
        pattern2 = re.compile("<span>(.*?)</span>")
        newtempreture_list=[]
        newdate_list=[]
        for item in tempreture_list:
            c1=pattern.findall(item[0])[0].replace("&", "")
            c2=pattern.findall(item[1])[0].replace("&", "")
            newtempreture_list.append((c1, c2))

        for item in date_list:
            c1=pattern2.findall(item)
            newdate_list.append(c1)
        finish=zip(newdate_list,newtempreture_list)
        self.write_tem(finish)

    def write_tem(self, date_tem_zip):
        #with open("D:\\tempreture.txt", 'a') as f:
           # for item in date_tem_zip:
               # f.write("日期： "+item[0][0]+"  "+item[0][1]+"\n"+"\t当日最高温度: "+item[1][0]+"℃"+"\n"+"\t当日最低温度: "+item[1][1]+"℃\n")
        for item in date_tem_zip:
            print("日期： "+item[0][0]+"  "+item[0][1]+"\n"+"\t当日最高温度: "+item[1][0]+"℃"+"\n"+"\t当日最低温度: "+item[1][1]+"℃\n")
        print("天气已查询完毕！欢迎下次使用")

if __name__=="__main__":
    location=input("请输入你要查询天气的城市：")
    spider=Spider(location)
    spider.loadPage()