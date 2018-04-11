# __author liuming
# 2018-04-11
import os
import sys

# print(sys.path.append('D:/python学习资料/fullstack')) # 不能写死路径
f=__file__
print('__file__',f)
abspath = os.path.abspath(f)
print('os.path.abspath(__file__)',abspath)
dirname= os.path.dirname(abspath)
print('os.path.dirname(abspath)',dirname)
BASE_DIR = os.path.dirname(dirname)
print('basedir',BASE_DIR)
print(sys.path)
sys.path.append(BASE_DIR)#添加项目路径到系统path中
print(sys.path)
from p1 import pp
pp.pm()