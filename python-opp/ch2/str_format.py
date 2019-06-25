name =  'python'
age = 22
# 打印 "我是python，今年27岁"
# 第一个不建议使用，因为格式转换比较麻烦
new_str = '我是' + name + ',' + '今年' + str(age) + '岁了';
print(new_str)

# python 2 里面这样转换，特别注意前面的%s和%d要和后面传入的数据类型一致
new_str1 = "我是%s，今年%d岁了" % (name , age)
print(new_str1)

# python 3格式转化 与2相比format不需要在意数据类型 还可以增加标识
new_str2 = "我是{name}，今年{age}岁了".format(name='python',age= 22)
print(new_str2)

# 这种方法可以直接引用变量
name1 = 'asd'
age1 = 22
new_str3 = f"我是{name1},今年{age1}岁了"
print(new_str3)

# bool就是 True or false条件语句会用到
# None空值就是没有值 a = '' （空字符串）or a = 0 （值是0）都不叫空。a = None叫空
