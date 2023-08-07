import numpy
import numpy as np
import timeit

string = "The password must contain at Least 1 Uppercase letter and 2 numbers" * 100000


def test_one_by_one():
    i = 0
    for c in string:
        if c.isupper():
            i += 1
    print(f"test_one_by_one: {i}")


def test_numpy():
    np_arr = np.array([ord(char) for char in string], np.int16)
    print(f"test_numpy: {len(np.where((np_arr >= 65) & (np_arr <= 90))[0])}")

# ascii_array = [ord(char) for char in string]

# print(ascii_array)

# test_one_by_one()
# test_numpy()