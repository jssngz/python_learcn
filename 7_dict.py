'''
dictionaries 是类似于java中的map的一种数据类型
他是一种键值关系。
创建一个空的字典，使用'{}'来声明一个空的map
关键字必须使用不可变类型，像数值型和字符串都可以，关键字不能相同
java当中的map的key是存在set当中的，所以java当中的map的key也不可以重复
使用 变量名[key]能取出key对应的value，
使用 变量名[key] = 新的value，修改dict中指定的key对应的value，如果key不存在于dict中，则增加
得到所有的key 列表，使用dict.keys()方法
测试指定的key是否存在于dict中，使用 key in（not in ） dict表达式，
返回值为boolean类型，表示对应的关键字存在（不存在）dict中。

删除dict中指定的键值对，如果key不存在，无操作
'''
empty = {}
print(empty, type(empty), len(empty))
tel = {'zhushuai' :'15068153755','shiwanlin': '158005299947'}
print(tel, type(tel), len(tel))
print('zhushuai tel:', tel['zhushuai'])
tel['zhushuai'] = '0122993920'
print('修改后的tel', tel, type(tel), len(tel))
tel['lisi'] = '122121'
print('修改后的tel', tel, type(tel), len(tel))
print('zhushuai' in tel,'wangwu' in tel)
print(list(tel.keys()))
del tel['zhushuai']
print('修改后的tel', tel, type(tel), len(tel))