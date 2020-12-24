#urllib.parse.request中的urlencode()接受的参数是一个字典
import urllib.parse as up
import urllib.request as ur

nl={"nl":"倪路"}
encoding=up.urlencode(nl)
print(encoding)

#将转码后的再转回去`
m=up.unquote(encoding)
print(m)