import math
import cProfile
import random


def _calculate_index(token_count, row_num, column_num):
    return int(row_num * (2 * token_count - row_num - 1) / 2 + column_num - row_num - 1)


def deconstruct_row_and_column(token_count, index):
    b = 2 * token_count - 1
    c = - 2 * index

    discriminant = b ** 2 + 4 * c
    square_root = math.sqrt(discriminant)
    row_num = (-b + square_root) // -2
    column_num = index - (row_num * (b - row_num) // 2 - row_num - 1)
    return row_num, column_num


def test(n):
    all_i_correct = True
    all_j_correct = True
    for i in range(n):
        for j in range(i + 1, n):
            index = _calculate_index(n, i, j)
            print(index)
            i_cal, j_cal = deconstruct_row_and_column(n, index)
            all_i_correct = all_i_correct and i_cal == i
            all_j_correct = all_j_correct and j_cal == j
    return all_i_correct, all_j_correct


# print(test(25))
# cProfile.run("test(10000)")


class Test(object):
    def __init__(self):
        if hasattr(Test, "attr"):
            print(f"already: {getattr(Test, 'attr')}")
        else:
            setattr(Test, "attr", random.randint(1, 1000))
            print("init")

    def say(self):
        print(f"{getattr(Test, 'attr')}")


Test().say()
Test().say()
