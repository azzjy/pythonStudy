'''
不定长字典参数：代表传递过程中，其参数数量不固定，但是其返回的结果是一个字典
'''
#不定长字典参数
def user_info(**kwargs):
    print(kwargs)
    print(type(kwargs))

user_info(name='Lily',age=23,address='gd')
