#cookielib  用于存储cookie的对象
#HTTPCookieProcessor 处理器  用于处理cookie对象，并构建handler对象

import urllib.request as ur
from http import cookiejar
import urllib.parse as up

#通过CookieJar()类构建一个cookiejar对象用于保存cookie值
cookie=cookiejar.CookieJar()

#通过HTTPCookieProcessor 处理器类构建一个处理器对象，用于处理cookie
#参数就是构建的cookiejar对象 返回一个handler对象
cookie_handler=ur.HTTPCookieProcessor(cookie)

#构建一个自定义opener
opener =ur.build_opener(cookie_handler)

#自定义opener的addHeaders的参数，可以赋值HTTP报头参数
opener.addheaders=[("User-Agent"," Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41")]

#U校园登录接口
url="http://www.nowcoder.com/login"

user="18582699881"

password="20021112nl"

#需要登录的账户密码
data={"jsEmailIpt":user,"jsPasswordIpt":password}

#转码处理
data=bytes(up.urlencode(data),encoding="UTF-8")

#第一次是post请求，发送登录需要的参数，获取cookie
request=ur.Request(url,data=data)

#发送第一次请求 如果登录成功，生成登陆成功后的cookie
response=opener.open(request)

#print(response.read().decode("utf-8"))

#第二次请求可以是get请求，这个请求将保存生成后的cookie发送到服务器，服务器验证cookie通过
response2=opener.open("http://www.nowcoder.com/97464973")
#正常打开需登录后才能访问的页面
print(response2.read().decode("UTF-8"))

#不使用opener类打开需登录后的页面 无法发送登录成功的cookie，即访问不到需登录后才可访问的页面
response3=ur.urlopen("http://www.nowcoder.com/97464973")
#打不开该页面
print(response3.read().decode("UTF-8"))