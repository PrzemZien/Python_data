import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Data
data = pd.read_csv("C:\\Users\\przem\\Desktop\\datadata.csv", usecols=['Humidity', 'Temperature'])
data_time = data['Humidity'].values
data_el_power = data['Temperature'].values

#Polyfit

function = np.polyfit(data_time,data_el_power,3)
p = np.poly1d(function)


# New points for interpolation
x_interp = np.linspace(min(data_time), max(data_time), 100)  # 100 punktów
plt.scatter(data_time,data_el_power,color="black",label="Humidity vs Temperature")
plt.plot(x_interp,p(x_interp),label="Polynomial fit",color="blue")


# Plots
plt.title("DHT11: Humidity vs Temperature")
plt.xlabel("Humidity [%]")
plt.ylabel("Temperature [°C]")
plt.legend()
plt.grid()
plt.show()
