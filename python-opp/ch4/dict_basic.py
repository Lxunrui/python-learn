# 字典的创建
a = {
    1: 'a',
    2: 'b',
    '3': 'c'
}
# 不可改变的数据类型
list1 = [1,2,3]
t1 = (1,2,3)
c={
    t1: list1
}
print(c)

d = dict()
print(d)
e = dict(a=1,b=2,c='a')
print(e)

# 字典的访问
print(e['a'])

# 字典是可以改变的
e['d']=123
print(e)
e['c']=3
print(e)

# 一个字典不能作为另一个字典的key