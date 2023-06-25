import os
from multiprocessing import Pool, Manager, Lock
from functools import partial
import os
import time
import random

"""
只遍历对角线一边的元素，则第一层循环 i: 0 ~ n, 第二层循环 j: i + 1 ~ n
利用一个一维数组存储所有元素的相似度，则总共需要的数组大小为: (n^2 - n) / 2
根据 i 和 j 计算一维相似度数组中的位置的公式为： index = i * (2 * n - i - 1) + j - i - 1
知道 index 之后求 i
"""
def fun0(value, register, rand_num, lock, x):
    try:
        lock.acquire()
        print("successful")
        for i in range(x * 10, x * 10 + 10):
            print(f"pid: {os.getpid()}")
            print(f"i {i}")
            register[i] = os.getpid()
            rand_num[i] = random.randint(1, 100)
            raise "100"
    except Exception as e:
            pass
    finally:
        lock.release()


if __name__ == '__main__':
    manager = Manager()
    num = manager.Value('i', 0)
    register = manager.Array('i', range(100))
    rand_num = manager.Array('i', range(100))
    lock = manager.Lock()

    with Pool(3) as pool:
        # 使用partial函数将num对象作为参数传递给子进程
        pool.map(partial(fun0, num, register, rand_num, lock), range(10))

    print(register)
    print(rand_num)