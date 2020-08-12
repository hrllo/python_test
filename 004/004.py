# -*- coding: utf-8 -*-
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

fin = open('004_text.txt', 'r')
str = fin.read()

reObj = re.compile('\b?(\w+)\b?')
words = reObj.findall(str)#a = re.findall("匹配规则", "要匹配的字符串")

wordDict = dict()#创建字典

for word in words:
    if word.lower() in wordDict:#lower()方法转换字符串中所有大写字符为小写
        wordDict[word.lower()] += 1
    else:
        wordDict[word] = 1

for key, value in wordDict.items():
    print('%s: %s' % (key, value))