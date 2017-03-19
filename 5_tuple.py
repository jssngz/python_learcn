'''
这个类展示的是tuple的定义和操作
tuple 和list的区别是什么，为何有了list还要有tuple
答：list和tuple的区别是tuple是不可变的，而list是可以变的。其他的功能，两者相同。因为tuple不可变，
所以tuple没有list的一些方法如appen。
创建tuple是用‘()’创建list是用‘[]’

'''
a = (1, 2, 3, 'zhangsan')
print(a, type(a), len(a))
print(a[0], a[1:5])


