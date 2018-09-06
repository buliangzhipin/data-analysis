import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data.csv')
data['DATE'] = pd.to_datetime(data['DATE'])
plt.plot(data['DATE'],data['VALUE'])

# rotation of the xticks
plt.xticks(rotation=45)

# xlabel , ylabel
plt.xlabel("years") 
plt.show()
print(data)
