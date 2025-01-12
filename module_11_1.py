import numpy as np
import matplotlib.pyplot as plt


y = np.array([1, 2, -6, 8, 4]) #создание массива с помощью numpy
x = np.arange(0, 5, 1) #создание массива с помощью numpy

plt.plot(x, y) #построение линейного графика с помощью библиотеки matplotlib
plt.grid() #показать сетку
plt.show() #показать график

