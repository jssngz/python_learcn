'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)

'''
def foo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return foo(n-1) +foo(n-2)
def printFoo(n):
    l = list()
    if i == 0:
        l.append(0)
        return l
    elif i == 1:
        l.append(0)
        l.append(1)
        return l
    else:
        l.append(0)
        l.append(1)
        for k in range(2,n+1):
            l.append(foo(k))
        return l
while True:
    i = int(input("请输入正整数"))
    print('费波那契', printFoo(i))
