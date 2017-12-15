#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
path="/home/eloise/catkin-ws/src/ddpg/scripts/"
results=np.load(path+"results2.npy")
l=20
font = {'family' : 'normal',
        'size'   : l}

plt.rc('font', **font)

l=5
plt.figure(1)
plt.subplot(211)
plt.plot(np.arange(len(results)),results[:,[0]], 'r+',ms=l)

plt.subplot(212)
plt.plot(np.arange(len(results)),results[:,[1]], 'b+',ms=l)
plt.show()


plt.figure(2)
plt.subplot(211)
plt.plot(np.arange(500),results[:,[0]][0:500], 'r+',ms=l)

plt.subplot(212)
plt.plot(np.arange(500),results[:,[1]][0:500], 'b+',ms=l)
plt.show()

