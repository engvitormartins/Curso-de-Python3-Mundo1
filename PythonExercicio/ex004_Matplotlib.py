import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoLocator)
from matplotlib.ticker import AutoMinorLocator


x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

# plot01
# plt.subplot(1, 2, 1)
plt.plot(x, label='linear')
plt.plot(y, label='quadratic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')
plt.legend()
plt.minorticks_on()
plt.grid(which='major', linestyle=':')
plt.tick_params(which='major', grid_color='black', width=2)
plt.tick_params(which='minor', length=4)

plt.show()



