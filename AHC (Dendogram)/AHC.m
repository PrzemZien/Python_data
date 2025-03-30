clear all;
clc;

data_array = xlsread("Dane_studentów.xlsx","D1:F7");

% AHC

Y = pdist(data_array); % zwraca informacje o odległości pomiędzy parami obiektów(wierszy)
new_data = squareform(Y); % poprawia czytleność
%Grupowani eobiektów podobnych
linkage_data = linkage(new_data)
% Dane:
% Obietk Obiekt Odległość pomiędzy tymi obiektami 
% 1.0000 5.0000 2.0356

%Wyświetlenie danych
dendrogram(linkage_data)