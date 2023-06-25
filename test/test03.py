import time
from lib.util import jaccard_optimized, jaccard_original
from datetime import datetime
import numpy as np
import os
from multiprocessing import Manager, Pool
from functools import partial
from typing import Callable, Sequence
import math


def _read_data():
    original_lines = list()
    with open("../data/01.data.txt", "r") as file:
        print("读取了")
        for line in file:
            original_lines.append(line)

    return original_lines


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


def jaccard_of_two_text(jaccard_function: Callable, jaccard_scores, num_of_lines: int, info: tuple):
    i, j, i_text, j_text = info
    score = jaccard_function(i_text, j_text)
    score_index = _calculate_index(num_of_lines, i, j)
    jaccard_scores[score_index] = score


def test(jaccard_function, test_name, num_perm: int = 128, seed: int = 1):
    result_path = f"../result1/{test_name}_{num_perm}_{seed}"
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    original_lines = _read_data()
    num_of_lines = len(original_lines)
    size_of_result = int((pow(num_of_lines, 2) - num_of_lines) / 2)

    start = datetime.now()

    result = np.zeros(size_of_result, dtype=np.float32)
    manager = Manager()
    result_array = manager.Array('f', result)
    partial_fun = partial(jaccard_of_two_text, jaccard_function, result_array, num_of_lines)

    with Pool(5) as pool:
        pairs = list()
        for i in range(0, num_of_lines):
            print(f"i: {i}， time consuming [{(datetime.now() - start).seconds}] seconds")
            for j in range(i + 1, num_of_lines):
                pairs.append((i, j, original_lines[i], original_lines[j]))
                if len(pairs) < 5000:
                    continue
                # print("提交")
                pool.map(partial_fun, pairs)
                pairs.clear()
        pool.map(partial_fun, pairs)
        # 使用partial函数将num对象作为参数传递给子进程
    end = datetime.now()
    print(f'time consuming [{(end - start).seconds}] seconds')


if __name__ == '__main__':
    test(jaccard_optimized, "m2-py-jaccard_optimized_01-1025", num_perm=128, seed=1)
# test(jaccard_original, "m2-py-jaccard_original_01-1025", num_perm=128, seed=1)
# test(jaccard_on_lean_minhash_optimized, "m2-py-lean_minhash_optimized_01-1025", num_perm=128, seed=1)
# test(jaccard_on_lean_minhash_original, "m2-py-lean_minhash_original_01-1025", num_perm=128, seed=1)
#
# test(jaccard_optimized, "m2-py-jaccard_optimized_01-1025", num_perm=128, seed=100)
# test(jaccard_original, "m2-py-jaccard_original_01-1025", num_perm=128, seed=100)
# test(jaccard_on_lean_minhash_optimized, "m2-py-lean_minhash_optimized_01-1025", num_perm=128, seed=100)
# test(jaccard_on_lean_minhash_original, "m2-py-lean_minhash_original_01-1025", num_perm=128, seed=100)
#
# test(jaccard_optimized, "m2-py-jaccard_optimized_01-1025", num_perm=256, seed=1)
# test(jaccard_original, "m2-py-jaccard_original_01-1025", num_perm=256, seed=1)
# test(jaccard_on_lean_minhash_optimized, "m2-py-lean_minhash_optimized_01-1025", num_perm=256, seed=1)
# test(jaccard_on_lean_minhash_original, "m2-py-lean_minhash_original_01-1025", num_perm=256, seed=1)
