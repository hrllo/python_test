#!/usr/bin/python
#coding=UTF-8
import psycopg2


def Create_Link(a):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE {0}
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           LINK        CHAR(50),
           NUMBER        INT     NOT NULL);'''.format(a))
    print "Table created successfully"
    conn.commit()
    #conn.close()


def Create_Login(a):
    cur=conn.cursor()
    cur.execute('''CREATE TABLE {0}
           (
           NAME           TEXT    NOT NULL,
           PASSWORD        CHAR(50),
           IP        CHAR(50)     );'''.format(a))
    print "Table created successfully"
    conn.commit()


def  InsertTable(a,b,c,d):
    cur=conn.cursor()
    cur.execute('''INSERT INTO {0}
    (ID,NAME,LINK,NUMBER)
    VALUES('{1}','{2}','{3}','0');'''.format(a,b,c,d))
    print "Table inserted successfully"
    conn.commit()


def UpateTable(a,b,c):
    cur = conn.cursor()
    cur.execute('''UPDATE {0}
    SET LINK ={1} WHERE LINK ={2};'''.format(a,b,c))
    print "Table updated successfully"
    conn.commit()


def DeleteTable(a,b):
    cur = conn.cursor()
    cur.execute('''DELETE FROM {0}
    WHERE NAME ={1};'''.format(a,b))
    print "Table deleted successfully"
    conn.commit()


conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
print("Opened database successfully")
Create_Link('tv')
Create_Link('shop')
Create_Link('music')
Create_Link('mail')
Create_Link('news')
Create_Link('bank')
Create_Login('login')

InsertTable('tv','1','爱奇艺','https://www.iqiyi.com/')
InsertTable('tv','2','腾讯视频','https://v.qq.com/')
InsertTable('tv','3','优酷','https://www.youku.com/')
InsertTable('tv','4','哔哩哔哩动画','https://www.bilibili.com/')
InsertTable('tv','5','芒果TV','https://www.mgtv.com/')

InsertTable('mail','1','163邮箱','https://mail.163.com/')
InsertTable('mail','2','阿里云','https://mail.aliyun.com/')
InsertTable('mail','3','126邮箱','https://www.126.com/')
InsertTable('mail','4','新浪邮箱','https://mail.sina.com.cn/')
InsertTable('mail','5','QQ邮箱','https://mail.qq.com/')
InsertTable('mail','6','139邮箱','https://mail.10086.cn/')

InsertTable('shop','1','1号店','https://www.yhd.com/')
InsertTable('shop','2','苏宁易购','https://www.suning.com/')
InsertTable('shop','3','阿里1688','https://page.1688.com/')
InsertTable('shop','4','唯品会','https://www.vip.com/')
InsertTable('shop','5','淘宝特卖','https://ai.taobao.com')
InsertTable('shop','6','京东','https://www.jd.com')

InsertTable('bank','1','工商银行','http://www.icbc.com.cn/')
InsertTable('bank','2','农业银行','http://www.abchina.com/')
InsertTable('bank','3','中国银行','http://www.boc.cn/')
InsertTable('bank','4','招商银行','http://www.cmbchina.com/')
InsertTable('bank','5','建设银行','http://www.ccb.com/')
InsertTable('bank','6','中信银行','http://www.citicbank.com/')
InsertTable('bank','7','邮政储蓄','http://www.psbc.com/')

InsertTable('music','1','酷狗音乐','http://www.kugou.com/')
InsertTable('music','2','一听音乐','https://www.1ting.com/')
InsertTable('music','3','虾米音乐','https://www.xiami.com/')
InsertTable('music','4','百度音乐','http://music.taihe.com/')
InsertTable('music','5','QQ音乐','https://y.qq.com/')
InsertTable('music','6','酷我音乐','http://www.kuwo.cn/')
InsertTable('music','7','网易云音乐','https://music.163.com/')

InsertTable('news','1','新浪新闻','https://news.sina.com.cn/')
InsertTable('news','2','腾讯新闻','https://news.qq.com/')
InsertTable('news','3','热点新闻','https://kan.china.com/?qudao=sgkz')
InsertTable('news','4','今日热点','https://top.voc.com.cn/sg_xwkz/list/4.html')















