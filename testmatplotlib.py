#Testing matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
from time import sleep
import numpy as np
'''
ax1 = plt.subplot(2,1,1)
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example One")
ax2 = plt.subplot(2,1,2)
plt.bar([3,4,5,7,6],[4,5,2,8,4], label="Example Two")
plt.show()
'''
i = 0
datalist = []
while i < 3:
    datalist.append(np.random.randint(1,200))
    i+=1


bar1 = plt.bar([1,2,3],[datalist[0],datalist[1],datalist[2]], width = .5)

plt.show()