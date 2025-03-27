import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import  FuncAnimation
import pandas as pd

# Data
data = pd.read_csv("C:\\Users\\przem\\Desktop\\test_1_data.csv", usecols=['time', 'el_power'])
data_time = data['time'].values
data_el_power = data['el_power'].values
print(len(data_time))

fig,ax= plt.subplots()
line,=ax.plot(data_time,data_el_power)

def myupdating(i):
    line.set_data(data_time[:i],data_el_power[:i])

myanimatin=FuncAnimation(fig,myupdating,frames=len(data_time),interval=0.001)
plt.show()