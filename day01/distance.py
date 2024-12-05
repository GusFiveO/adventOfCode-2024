import pandas as pd
import numpy as np

lists = pd.read_csv("./lists.csv", header=None, sep="\s+")
lists = lists.to_numpy().T
sorted_list = np.sort(lists)
distance = sorted_list[1] - sorted_list[0]
distance_sum = sum(abs(distance))
print("The total distance is:", distance_sum)
