import urllib.request as ur
import urllib.parse as up
import json
content=input("请输入您要翻译的内容：")
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data={}
data['i']=content
data['from']='AUTO'
data['to']= 'AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']= '16052370333174'
data['sign']= '515ab450c36c14f12388754474cea7a1'
data['lts']= '1605237033317'
data['bv']= '30910bdfd133e33a1cc370e4ad51d60f'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']= 'FY_BY_CLICKBUTTION'

data=up.urlencode(data).encode('utf-8')
response=ur.urlopen(url,data)

html=response.read().decode('utf-8')

print(html)
