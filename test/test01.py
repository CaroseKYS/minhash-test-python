import numpy as np
import scipy.stats as st

data = np.random.randint(1, 1000, 1000)

print(st.skew(data))
print(st.kurtosis(data))
