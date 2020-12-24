import urllib.request as ur
import random
url="https://www.whatismyip.com"

iplist=['36.249.119.21:9999']

proxy_support=ur.ProxyHandler({'http':random.choice(iplist)})

opener=ur.build_opener(proxy_support)

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68')]
ur.install_opener(opener)

response=ur.urlopen(url)

html=response.read().decode('utf-8')

print(html)