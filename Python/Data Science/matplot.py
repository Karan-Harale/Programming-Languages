# from matplotlib import pylab
#
# import numpy as np
#
# n=np.random.rand(10)
# m=np.random.rand(10)
#
# pylab.plot(n,m,'r')
#
# print(n,m,)
#
# pylab.show()


from matplotlib import pyplot as plt

fig=plt.figure()
axis=fig.add_axes([0.5,0.1,0.8,0.8,'r'])
axis.plot()