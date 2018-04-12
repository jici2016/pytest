# __author liuming
# 2018-04-12
'''
shelve包 就像是一个可以直接使用的字典，但是他可以存储为文件

'''
import shelve

dic = {'name':'刘铭','age':"28","sex":'男'}

d=shelve.open('shelvefile')

d['dic']=dic

# print(d['dic']['name1'])
print(d.get('dic').get('sex'))
print(d['dic']['sex'])
print(d.get('dic').get('sex1','girl'))
d['dic']['age']='18'
# print(d['dic']['sex1'])