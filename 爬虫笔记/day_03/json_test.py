#json.loads()  把Json格式的字符串解码转换称Python对象
    #object->dict   array->list string->unicode number(int)->int,long   number(real)->float true->True  flase->False    null->None
#json.dumps()  把python类型转化为json字符串，返回一个str对象
    #dict->object   list,tuple->array   str,unicode->string int,long,float->number  True->true  False->flase    None->null
#JsonPath 信息抽取类库  与Xpath类似

#xpath jsonpath语法对比
'''
XPath	JSONPath	Description
/	        $	    the root object/element
.	        @	    the current object/element
/	        . or []	child operator
..	        n/a	    parent operator
//	        ..	    recursive descent. JSONPath borrows this syntax from E4X.
*	        *	    wildcard. All objects/elements regardless their names.
@	        n/a	    attribute access. JSON structures don't have attributes.
[]	        []	    subscript operator. XPath uses it to iterate over element collections and for predicates. In Javascript and JSON it is the native array operator.
|	        [,]	    Union operator in XPath results in a combination of node sets. JSONPath allows alternate names or array indices as a set.
n/a	        [start:end:step]	array slice operator borrowed from ES4.
[]	        ?()	    applies a filter (script) expression.
n/a	        ()	    script expression, using the underlying script engine.
()	        n/a	    grouping in Xpath
'''

#xpath模糊查询 [contains(@属性, "str")]

#导入json解析库
import json

#导入json解析语法
import jsonpath
import urllib.request as ur
url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'}

request=ur.Request(url, headers=headers)

response=ur.urlopen(request)

#取出json文件内容，返回的格式是字符串
html=response.read().decode('utf-8')

#把json文件里的字符串内容转化为python形式的unicode字符串格式
unicodestr=json.loads(html)

#python形式的列表
city_list=jsonpath.jsonpath(unicodestr, "$..name")

#要将ensure_ascii设置为False 否则在转换时会将json字符串默认转换中文为ascii格式，需要将字符串转化为unicode格式，方便使用
arrayList=json.dumps(city_list,ensure_ascii=False)

with open("City.json", 'w') as f:
    f.write(arrayList)

