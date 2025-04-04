import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

auto = pd.read_csv(r"C:\Users\przem\Desktop\auto-mpg.csv")

# konkretne kolumny
X = auto[["cylinders","displacement","weight","acceleration","model year","origin"]]
y = auto["mpg"]

# Tworze model
lr = LinearRegression()
lr.fit(X.to_numpy(),y)
lr.score(X.to_numpy(),y)

score_data = lr.score(X.to_numpy(),y)


my_car1 = [6, 200, 3150, 15.5, 76, 1]
my_car2 = [4, 200, 260, 15, 83, 1]
my_car = [8,307,3504,12,70,1]
cars = [my_car1,  my_car]

prediction = lr.predict(cars)
print(score_data)
print(prediction)



