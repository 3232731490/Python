#split(str,count)
#count是最大分割次数

import re
pattern=re.compile(r"[\s\d\\\;]+")

m=pattern.split(r"a bb\aa;m1m;      a")

print(m)