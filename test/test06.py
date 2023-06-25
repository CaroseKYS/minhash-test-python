import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
# 合并  ignore_index设置为 True可以重新排列索引
# dfx = pd.concat([df, [5, 6]], axis=0)

df.loc[df.index.size] = [5, 6]
print(df)