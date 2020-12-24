#pattern=re.compile("匹配规则")  返回一个匹配对象


#pattern.match("字符串")  从起始位置开始找，返回第一个符合规则的字符串的match对象，需要用group方法将字符串弄出来
#match(str,[begin,[end]])

#pattern.search("字符串")   从任意位置开始找，返回第一个符合规则的字符串
#pattern.findall("字符串")  对整个字符串进行匹配，返回一个列表
#pattern.finditem("字符串")  对整个字符串进行匹配，返回一个迭代器
#pattern.split("字符串")  分割字符串，返回列表
#pattern.sub()  替换符合规则的字符串

#re.I  忽略大小写
#re.S  全文匹配

import re
pattern=re.compile(r"(\d)(\d)" ,re.I)
str="abc123*&^"

#group( 0 ) 将所有字串读取出来
#group( n ) 将匹配的第 n 组字串读取出来
print(pattern.match(str,3,8).group(0))

#返回第一个符合规则的子串的起始位置到结束位置
print(pattern.match(str,3,8).span())
