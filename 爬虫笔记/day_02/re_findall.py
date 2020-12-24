#findall(str,begin,end)
#返回一个所有匹配成功子串的列表
#findier(str,begin,end)
#返回一个匹配对象的迭代器对象
import re

pattern= re.compile(r"\d+")

m=pattern.findall("aaa 12345  789")

print(m)

m=pattern.finditer("aaa 123456 789")

for i in m:
    print(i.group())