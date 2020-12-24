#HTTPPasswordMgrWithDefaultRealm  这个类会创建一个密码管理对象，用来保存和HTTP请求相关的授权信息
#ProxyBasicAuthHandler 授权代理处理器
#HTTPBasicAuthHandler 验证web客户端的授权处理器
import urllib.request as ur

test="18582699881"
password="20021112nl"
webserver="120.55.144.107"

#构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordmgr=ur.HTTPPasswordMgrWithDefaultRealm()

#第一个参数代表域realm，若没有指定就填None  后三个参数分别是站点ip，账户和密码
passwordmgr.add_password(None,webserver,test,password)

#HTTPBasicAuthHandler()  HTTP基础验证处理器类
http_handler=ur.HTTPBasicAuthHandler(passwordmgr)

#用于处理代理基础验证相关的处理器类
proxyauth_handler=ur.ProxyBasicAuthHandler(passwordmgr)

#构建自定义opener 可以添加多个处理器类
opener=ur.build_opener(http_handler)

#添加全局opener 执行此操作后 可直接用urllib.request.urlopen来打开网页
#ur.install_opener(opener)

request=ur.Request("http://"+webserver)

#有授权验证信息方式打开请求
reponse=opener.open(request)

#没有授权验证信息打开请求
#reponse=ur.urlopen(request)

print(reponse.read().decode("utf-8"))
