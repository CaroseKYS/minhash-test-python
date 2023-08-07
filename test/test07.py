import sys
from unicodedata import category
from datetime import datetime


dict_cache = dict.fromkeys(
            (i for i in range(sys.maxunicode) if category(chr(i)).startswith("P")),
            " ",
        )


def translate(s):
    return s.translate(
        dict.fromkeys(
            (i for i in range(sys.maxunicode) if category(chr(i)).startswith("P")),
            " ",
        )
    )


def translate_op(s):
    return s.translate(dict_cache)


def test_1(fun):
    start = datetime.now()
    i = 0
    max = 100
    with open("/Users/kangyongsheng/work/data/spark-cc/part-00052-0a7cb61e-56e8-492b-a9c0-cc1c6f0f3b6c-c000.json",
              "r") as file:
        for line in file:
            fun(line)
            i += 1
            if i >= max:
                break

    end = datetime.now()

    print(f"{max} rows, execution time {((end - start).microseconds) // 1000} milliseconds")


test_1(translate)
test_1(translate_op)
