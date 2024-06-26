'''
函数递归是调用函数自身的变成技巧
递归有两个非常重要的概念：
    1. 递归点：找到解决当前问题的等价函数(先解决规模比当前问题小的一些函数，一次类推，最终实现对问题的解决) => 有递有归
    2. 递归出口： 当问题解决的时候，已经到达(必须存在)最优问题，不能再次调用函数了
    如果没有递归出口就变成一个死循环了
'''

def func(num):
    if num ==1 or num ==2:
        return 1
    
    return func(num-1)+func(num-2)

print(func(4))