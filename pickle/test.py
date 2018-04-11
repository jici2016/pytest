# __author liuming
# 2018-04-11

'''使用pickle 获取文件中的方法，然后加载和调用'''

def hello1():
    print('test')


import  pickle
r=open('pickle.txt','rb')
data=r.read()
print(type(data),data)
method=pickle.loads(data)
print(type(method),method)
method() #调用  这里有坑，使用他的话，要求本地内存中需要有这个对应的方法才行