text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# better替换为worse
text1 = text.replace('better', 'worse')
print(text1)

# 剔除包含 ea 的单词
x = text1.split()
text2 = []
for i in x:
    if i.find('ea') < 0:
        text2.append(i)
print(text2)

# 字母大小写翻转
a = ''
b = a.join(text2)
text3 = b.swapcase()
print(text3)

# 单词按a~z升序排列
c = text3.split()
text4 = sorted(c)
print(text4)
