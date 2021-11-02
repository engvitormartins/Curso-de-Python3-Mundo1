
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])


plt.subplot(1, 2, 1)
# plt.grid()
plt.bar(x,y)
plt.title('SALES')

#plot 2:
x = np.array([5, 10, 50, 80])
# y = np.array([10, 20, 30, 40])
mylabels = ['ruim', 'medio', 'bom', 'excelente']
myexplode = [0.05, 0.1, 0.15, 0.2]
mycolors = ['#C3C3C3', '#979797', '#787878', '#2C2B2B']



plt.subplot(1, 2, 2)
# plt.grid()
plt.pie(x, labels = mylabels, explode=myexplode, shadow=True, colors=mycolors,
        autopct=lambda p:f'{p:.2f}%, {p*sum(x)/100 :.0f} items')

# plt.legend(mylabels, loc = 'best', title = "Numbers of X:")
plt.title('INCOME')

plt.suptitle('MY DATA PLOTS')
plt.show()
