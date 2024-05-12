'''
字符串，列表，元组都支持切片
'''
str1 = 'abcdefg'

print(str1[2])

print(str1[0:3])


# 序列名[开始位置的下标:结束位置的下标:步长]
str2 = '012345678'

print(str2[2:5:2])

print(str2[2:5])

print(str2[2:])

print(str2[::2])

#负数测试

print(str2[::-1]) #步长为负数表示倒叙选取
print(str2[-4:-1])

print(str2[-4:-1:-1]) #不能选取出数据 因为-4到-1结束，选取方向为从左到右，但是-1步长；从右向左选取

# ******* 如果

print(str2[-4:1:-1])