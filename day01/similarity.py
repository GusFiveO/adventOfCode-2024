import pandas as pd
import numpy as np

lists = pd.read_csv("./lists.csv", header=None, sep="\s+")
lists = lists.to_numpy().T
similarity = 0
list_1 = lists[1].tolist()
for id in lists[0]:
    similarity += id * list_1.count(id)
print("The similarity is:", similarity)
