'''
有一个字符串
text = "aAsmr3idd4bgs7Dlsf9eAF"

请将text字符串中的数字取出，并输出成一个新的字符串。

'''
text = "aAsmr3idd4bgs7Dlsf9eAF"
number = ''
for i in range(len(text)):
    char =text[i]
    if char.isdigit():
        # python的内建函数，判断是否是数字
        number += char
print(number)
# 第二种解决方法
text = "aAsmr3idd4bgs7Dlsf9eAF"
number = ''
for i in range(len(text)):
    char =text[i]
    try:
        int(char)
        number += char
    except ValueError:
        pass
print(number)


