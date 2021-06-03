# *-* coding: utf-8 *-*
"""
作者：XGM
日期：2021.05.29 11:52:23
"""
import time
# 这是一个计算函数执行时间的装饰器
def decorator(fu):
    def inner(*args,**kwargs):
        start = time.perf_counter()
        ret = fu(*args,**kwargs)
        end = time.perf_counter()
        print("该函数的运行时间是：",end - start,"s")
        return ret
    return inner


# 例子：输出“计算1+1”所使用的时间
@decorator
def one_add_one():
    a = 1+1
    print(a)


one_add_one()

