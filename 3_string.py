'''
怎么声明一个变量为字符串 ok
怎么得知一个变量是字符串变量 ok
怎么得知字符串的长度 ok
字符串中的特殊类型怎么得到? 换行 制表 no
为了防止特殊字符发生转义，怎么操作能够让字符串不转义 ok

怎么得知某个字符串在第二个字符串中的第一个位置，最后一个位置 no
怎么得到对应的子串 no
怎么确定字符串是空还是null no
字符串的正则表达式是怎么做到的 no
怎么由数字类型转化为字符串类型的 no
怎么由日期类型转化为字符串类型 no
'''
s = 'Yes ,he doesn\'t'
print(s, type(s), len(s), 'len函数可以计算字符串的长度')
print('C:\some\name', '使用\可以转义后面的字符')
print(r'C:\some\name', '使用r加一个字符串的方式，可以使字符串中的字符\不发生转义')
print('str'+'int', 'my'*3, '字符串可以使用+连接，使用*重复')
word = 'python'
print(word[0], word[5])
print(word[-1], word[-6])
new_word = "ilovepython"
print(new_word[1:5])


