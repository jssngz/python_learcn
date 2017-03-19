'''
set 是和java中set是一种数据类型
set使用‘{}’代表，使用set()方法可以创建一个空的set
set 是可以修改的

1、声明的时候，重复的元素会自动被去除掉
2、set可以当做数学中的集合，对两个set可以做集合运算
a- b差集 在a的基础上，减去b集合中的元素
a|b 并集 在a中存在,并且在b中存在的元素
'''
names = {'zhangsan', '李四', '王五','zhangsan'}
print(names,type(names),len(names))
a = set('abcdefg')
b = set('efghig')
print(a, 'a set', b, 'b set', len(a), len(b))
print(a - b, type(a - b), len(a-b), 'a和b的差集')
print(a|b, type(a|b), len(a|b), 'a和b的并集')
print(a&b, type(a&b), len(a&b), 'a和b的交集')
print(a^b, type(a^b), len(a^b), 'a和b中不同时存在的元素')
