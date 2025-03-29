import pandas as pd
from scipy.cluster import hierarchy
import numpy as np
import matplotlib.pyplot as plt

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram

# Data - moze tylko byc 2 wymiarowa albo jednowymiarowa
data  = np.array([
    [5,4,3,2], # Obiekt 0
    [2,2,0,0], # Obiekt 1
    [6,7,8,9], # Obiket 2
    [4,5,6,5], # Obiekt 3
    [7,7,7,7], # Obiekt 4
    [3,4,5,6], # Obiekt 5
    [1,1,1,1]  # Obiekt 6
])

# Dendogram
# Każdy wiersz to pojedyńczy obiekt a kazdy obiekt to oddzielne kryterium( czyli np.  Obiekt 0 -> macierz -> oceny z polskiego)
# Każda kolumna to cecha
# Grupowanie w dendogramie pokazuje ktrore obiekty sa podobne do siebie
#Jak go czytać mam 6 obiektów dlatego też mam 6
K = hierarchy.linkage(data,method='average') # y - data, method - metoda z której skorzystamy
plt.figure()
plt.title("Dendrogram")
dendrogram = hierarchy.dendrogram(K)
plt.show()

# Omównienie wyniku
# Obiekt 6 i 1 są podobne ponieważ oba mają małe wartości, czyli [1,1,1,1] i [2,2,0,0]
# Obiekt 5 i 3 są podobne ponieważ powtarzają się u nich liczby w podobnej kolejnosci 4,5 i 6 bo: 5: [3,4,5,6] i 3: [4,5,6,5]
# itd

#Wniosek
# Im niżej dwa obiekty są połączone, tym są bardziej podobne.
# Im wyżej, tym bardziej różnią się od siebie.
# Dendrogram pomaga znaleźć podobieństwa w zestawie danych i pokazuje, jak bardzo różne obiekty są do siebie zbliżone na podstawie określonych cech.