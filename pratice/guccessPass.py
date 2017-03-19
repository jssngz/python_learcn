from random import randint
'''
再来一个相对简单点的。
以前电子词典上有个游戏：要你猜一个4位密码，密码由0-9组成，不重复。
猜对正确位置上的数字为A，猜到数字但位置不正确为B。每次显示答案中A和B的个数。
比如：密码是1234
猜2345，显示0A3B
猜4231，显示2A2B
直到显示4A0B的时候，游戏胜利。
以此为基础，做个游戏。
'''
passwdInt = randint(1000,9999)
passwd = str(passwdInt)
print(passwd)
while True:
    # print("请输入猜测的密码：")
    inputpassWd = input()
    if len(inputpassWd) == 0:
        continue
    rightPosCount = 0
    rightNumberCount = 0
    char = ''
    for i in range(len(inputpassWd)):
        char = inputpassWd[i]
        if char == passwd[i]:
            rightPosCount += 1
        else:
            if char in passwd:
                rightNumberCount += 1

    if rightPosCount == 4 and rightNumberCount == 0: # && 使用and ||使用 or代替
        print('结果正确：' + str(rightPosCount) + 'A' + str(rightNumberCount) + 'B')
        break
    else:
        print('结果错误：' + str(rightPosCount) + 'A' + str(rightNumberCount) + 'B')
