# __author liuming
# 2017-10-26
import re
str="hello,python3"
print(str)
ret = re.search('l+',str)
print(ret.group())

rg=re.compile('\d')

ret2 = rg.search(str)
print(ret2.group())