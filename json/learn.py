# __author liuming
# 2018-04-11
dic={"name":"jack","age":28,"sex":'男'}
#方法一
'''
#不使用其他包，可以这样写入字典
f=open('json.txt','w',encoding='utf-8')
data=str(dic)
f.write(data)# 需要使用str()将字典转为str，麻烦
f.close()
'''

'''
r=open('json.txt','r',encoding='utf-8')
data=r.read()
print(eval(data)['age']) # 可以使用eval()解析json，但是这样读出来并不好
'''

#方法二 ，采用 json方式
import  json
'''
#使用json dumps将字典转换为str
data2 = json.dumps(dic)
print(type(data2))
f=open('json2.txt','w',encoding='utf-8')
f.write(data2)# 需要使用str()将字典转为str，麻烦
f.close()
'''
'''
#使用 json的loads方法将str转换为字典
r=open('json2.txt','r')
data2 = r.read()
print("data2",type(data2))
data2=json.loads(data2)
print("data2",type(data2))
print(data2['name'])
'''