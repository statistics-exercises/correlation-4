import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = np.zeros(100), np.zeros(100)
# Your code goes here




# The commands to plot the data 
plt.plot( xdata, ydata, 'bo' )
plt.plot( [0,0], [0.4,0], 'k-' )
plt.plot( [0,5.7], [0.4,0.4], 'k-' )
plt.plot( [0,5.7], [0,0], 'k-' )
plt.plot( [5.7,5.7], [0,0.4], 'k-' )
plt.savefig('joint_uniform.png')
