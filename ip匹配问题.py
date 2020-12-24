import re

pattern=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1='127.0.0.1 192.168.1.66'

d=re.findall(pattern,str1)
for item in d:
    print(item[0])