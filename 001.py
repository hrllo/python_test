#-*- coding:utf-8 -*-
'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import uuid
import random
st= 'qwertyuiopasdfghjklzxcvbnm!@#$%^&*'
for i in range(0,200):
    x=str(uuid.uuid4().fields[-1])[:10]+st
    #uuid.uuid1([node[, clock_seq]])  : 基于时间戳
    #uuid.uuid3(namespace, name) : 基于名字的MD5散列值
    #uuid.uuid4() : 基于随机数
    y=''
    for j in range(0,10):
         y+=random.choice(x)
    print (y+"\n")