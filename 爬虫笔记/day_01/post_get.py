#Get请求的URL会附带查询参数  查询参数在QueryString里保存
#Post请求的URL则不会附带参数  查询参数在Form表单里保存
#只要在获取请求对象时有data参数就是Post请求

#要发送Post需要通过抓包获取URL地址，不能直接通过浏览器上的URl

#有道翻译案例
import urllib.parse as up
import urllib.request as ur
import json
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
key=input("请输入您要翻译的文字：")
fromdata={'i':key,
'from':'AUTO&to=AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'16062794741335',
 'sign':'9a11f6408b644b34dd0a5dc8c03b24f7',
 'lts':'1606279474133',
 'bv':'ca0e150684e94d555f873bec59cdcbd3',
 'doctype':'json',
 'version':'2.1',
 'keyfrom':'fanyi.web',
 'action':'FY_BY_REALTlME'}

data=up.urlencode(fromdata).encode('utf-8')

request=ur.Request(url,data=data,headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41"})

response=ur.urlopen(request)

print("翻译结果为：")
html=response.read().decode('utf-8')

target=json.loads(html)

print(target)

print("翻译结果为： %s" % target['translateResult'][0][0]['tgt'])