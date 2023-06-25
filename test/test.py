import numpy as np
from lib.util import jaccard_on_lean_minhash
from datetime import datetime
import cProfile

def test():
    original_lines = list()

    with open("../data/01.data.txt", "r") as file:
        for line in file:
            original_lines.append(line)

    num_of_lines = len(original_lines)

    result = np.zeros((num_of_lines, num_of_lines), dtype=np.float32)

    start = datetime.now()

    for i in range(0, num_of_lines):
        print(f"i: {i}， time consuming [{(datetime.now() - start).seconds}] seconds")
        for j in range(0, num_of_lines):
            result[i][j] = jaccard_on_lean_minhash(original_lines[i], original_lines[j])
            # result1[i][j] = jaccard(original_lines[i], original_lines[j])

    end = datetime.now()
    print(f'time consuming [{(end - start).seconds}] seconds')
    print(result)


cProfile.run('test()')