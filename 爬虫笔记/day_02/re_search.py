#re.search(str,begin,end)
#返回一个匹配对象，与match类似
import re

pattern=re.compile(r"\d+")

m=pattern.search("aaa123bbb456",2,5)

print(m.group(0))

print(m.span())

