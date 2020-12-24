import urllib.request as ur
import random

header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"}

 #返回一个请求对象，接受的参数可以有报头headers，方便与反爬虫对抗
request = ur.Request("http://www.baidu.com/" ,headers=header)

#返回一个类文件对象，可以使用python处理文件的一些方法
response=ur.urlopen(request)

#返回http响应码
print(response.getcode())

#返回 返回实际数据的URL，防止重定向问题
print(response.geturl())

#返回服务器响应的http报头
print(response.info())

#写一个User-Agent列表，访问网站时随机使用来反反爬虫
agent_list= [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0"
]

user_agent=random.choice(agent_list)

request2=ur.Request("http://www.baidu.com/")

#通过此方法将文件头加入请求对象
request2.add_header("User-Agent",user_agent)

#需要注意获取时第一个字母大写，后面的字母均小写
print(request2.get_header("User-agent"))

