# 获取列表的一些基本信息
list1 = [9,1,-4,3,7,11,3]
print('list1的长度 =',len(list1))
print('list1里的最大值 =',max(list1))
print('list1里的最小值 =',min(list1))
print('list1里3这个元素出现了{}次'.format(list1.count(3)))

# 列表的改变
list2 = ['a','c','d']
# 给list2结尾添加一个新元素e
list2.append('e')
print('list2 =',list2)
# 给list2的a and c 之间插入b
list2.insert(1,'b')
print('list2 =',list2)
# 删除list2里的b
list2.remove('b')
print('list2 =',list2)
# 可以改变列表里的值，但是不可以改变字符串里的某个值只能全部改
list2[0] = '1'
print('list2 =',list2)

# 列表翻转
list3 = [1,2,3]
list3.reverse()
print('list3 = ',list3)
# 列表排序
list4 = [9,1,-4,3,7,11,3]
list4.sort()
print('list4 =',list4)