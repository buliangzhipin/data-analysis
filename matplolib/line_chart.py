import matplotlib.pyplot as plt
import pandas as pd

import os
path = os.getcwd()
print(path)

data = pd.read_csv(path+'\\matplotlib\\data.csv')
print(data)
