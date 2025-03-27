import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = pd.read_csv("C:\\Users\\przem\\Desktop\\test_1_data.csv", usecols=['time', 'el_power'])
data_time = data['time'].values
data_el_power = data['el_power'].values

# New points for interpolation
x_interp = np.linspace(min(data_time), max(data_time), 100)  # 100 punktów

# Interpolation
y_interp = np.interp(x_interp, data_time, data_el_power)

# Plots
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x_values, y_values, 'd', label="Dane oryginalne")  # Original Points
ax.plot(x_interp, y_interp, '-', label="Interpolacja")  # Interpolation
ax.legend()
plt.show()






