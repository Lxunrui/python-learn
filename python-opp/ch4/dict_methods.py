d = {
    'name': 'jack',
    'age': 9,
    'grade': 5,
}
# 获取某个key的值
print(d['name']) # 可能会报错
print(d.get("name"))

# 获取到有哪些key
print(d.keys())

# 获取有哪些值
print(d.values())

# 获取一对一对的key和值
print(d.items())

# 取出来所对应的key和值，之前的字典里的删除
c = d.pop('name')
print(c)
print(d)

# 清除字典
d.clear()
print(d)

# 字典的更新
c ={
    1: 1,
    1: 2,
}
c[3] = 3
c[4] = 4
print(c)

d = {
    1: 8,
    5:5,
    6:6,
}
# 重复的会被覆盖掉
c.update(d)
print(c)
# 下面这个效果相同但是原理不一样
#e = {**c,**d}
#print(e)