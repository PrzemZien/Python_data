import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_test_1_time = pd.read_csv("C:\\Users\\przem\\Desktop\\test_1_data.csv",usecols=['time'], header=0).values
data_test_1_el_power = pd.read_csv("C:\\Users\\przem\\Desktop\\test_1_data.csv",usecols=['el_power'], header=0).values

fig, ax = plt.subplots(figsize=(5,2.7), layout='constrained')
ax.plot(data_test_1_time,data_test_1_el_power,label='linear')
ax.plot(data_test_1_time,data_test_1_el_power,label='quadratic')
ax.plot(data_test_1_time,data_test_1_el_power,label='cubic')
ax.set_xlabel("time [s]")
ax.set_ylabel("Electrical Power [W]")
ax.set_title("Plot")
ax.legend()
plt.show()




