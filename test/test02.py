import json

import pandas
from pandas import DataFrame

from lib.util import jaccard_on_lean_minhash_original, jaccard_on_lean_minhash_optimized, jaccard_on_lean_minhash_cached
from lib.util import jaccard_optimized, jaccard_original, jaccard_cached
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.stats as st
import pandas as pd

original_lines = list()

with open("../data/01.data.txt", "r") as file:
    for line in file:
        original_lines.append(line)

num_of_lines = len(original_lines)
size_of_result = int((pow(num_of_lines, 2) - num_of_lines) / 2)


def test(jaccard_function, test_name, df: DataFrame, num_perm: int = 128, seed: int = 1):
    result_path = f"../result1/{test_name}_{num_perm}_{seed}"
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    start = datetime.now()
    result = np.zeros(size_of_result, dtype=np.float32)
    cursor = 0
    for i in range(0, num_of_lines):
        print(f"i: {i}， time consuming [{(datetime.now() - start).seconds}] seconds")
        for j in range(i + 1, num_of_lines):
            result[cursor] = jaccard_function(original_lines[i], original_lines[j], num_perm=num_perm, seed=seed)
            cursor += 1
    end = datetime.now()
    print(f'cursor is [{cursor}]')
    print(f'time consuming [{(end - start).seconds}] seconds')
    stats = {
        "name": test_name,
        "num_perm": num_perm,
        "seed": seed,
        "time_consuming": (end - start).seconds,
        "middle": float(np.quantile(result, 0.5)),
        "mean": float(np.mean(result)),
        "var": float(np.var(result)),
        "max": float(np.max(result)),
        "min": float(np.min(result)),
        "skew": st.skew(result),
        "kurtosis": st.kurtosis(result)
    }

    df.loc[df.index.size] = stats

    with open(f"{result_path}/stat.json", "w") as file:
        file.write(json.dumps(stats))
    plt.hist(result, bins=80, histtype="stepfilled", alpha=.8)
    plt.savefig(f"{result_path}/distributing.png")


dataframe = pandas.DataFrame(columns=[
    "name",
    "num_perm",
    "seed",
    "time_consuming",
    "middle",
    "mean",
    "var",
    "max",
    "min",
    "skew",
    "kurtosis",
])
# test(jaccard_optimized, "m2-py-jaccard_optimized_01-1025", dataframe, num_perm=128, seed=1)
test(jaccard_original, "m2-py-jaccard_original_01-1025", dataframe, num_perm=128, seed=1)
# test(jaccard_cached, "m2-py-jaccard_cached_01-1025", dataframe, num_perm=128, seed=1)
# test(jaccard_on_lean_minhash_optimized, "m2-py-lean_minhash_optimized_01-1025", dataframe, num_perm=128, seed=1)
# test(jaccard_on_lean_minhash_original, "m2-py-lean_minhash_original_01-1025", dataframe, num_perm=128, seed=1)
# test(jaccard_on_lean_minhash_cached, "m2-py-lean_minhash_cached_01-1025", dataframe, num_perm=128, seed=1)

# test(jaccard_optimized, "m2-py-jaccard_optimized_01-1025", dataframe, num_perm=128, seed=100)
# test(jaccard_original, "m2-py-jaccard_original_01-1025", dataframe, num_perm=128, seed=100)
# test(jaccard_cached, "m2-py-jaccard_cached_01-1025", dataframe, num_perm=128, seed=100)
# test(jaccard_on_lean_minhash_optimized, "m2-py-lean_minhash_optimized_01-1025", dataframe, num_perm=128, seed=100)
# test(jaccard_on_lean_minhash_original, "m2-py-lean_minhash_original_01-1025", dataframe, num_perm=128, seed=100)
# test(jaccard_on_lean_minhash_cached, "m2-py-lean_minhash_cached_01-1025", dataframe, num_perm=128, seed=100)

# test(jaccard_optimized, "m2-py-jaccard_optimized_01-1025", dataframe, num_perm=256, seed=1)
# test(jaccard_original, "m2-py-jaccard_original_01-1025", dataframe, num_perm=256, seed=1)
# test(jaccard_cached, "m2-py-jaccard_cached_01-1025", dataframe, num_perm=256, seed=1)
# test(jaccard_on_lean_minhash_optimized, "m2-py-lean_minhash_optimized_01-1025", dataframe, num_perm=256, seed=1)
# test(jaccard_on_lean_minhash_original, "m2-py-lean_minhash_original_01-1025", dataframe, num_perm=256, seed=1)
# test(jaccard_on_lean_minhash_cached, "m2-py-lean_minhash_cached_01-1025", dataframe, num_perm=256, seed=1)

dataframe.to_excel('../result1/winner.xlsx',index = False)
