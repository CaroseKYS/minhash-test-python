from lib.util import jaccard_on_lean_minhash
from datetime import datetime
import cProfile

def test():
    original_lines = list()

    with open(
            "/Users/kangyongsheng/Downloads/trainingandtestdata/training.1600000.processed.noemoticon.csv",
            "r",
            encoding="latin1"
    ) as file:
        for line in file:
            original_lines.append(line)

    num_of_lines = len(original_lines)

    start = datetime.now()

    for i in range(0, num_of_lines):
        print(f"i: {i}， time consuming [{(datetime.now() - start).seconds}] seconds")
        for j in range(0, num_of_lines):
            result = jaccard_on_lean_minhash(original_lines[i], original_lines[j])
            if result > 0.8:
                print(result)

    end = datetime.now()
    print(f'time consuming [{(end - start).seconds}] seconds')
    print(result)


cProfile.run('test()')