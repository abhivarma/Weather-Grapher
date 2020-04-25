from numpy import *
from math import *
import matplotlib.pyplot as plt


xvals = linspace(-10,10,200)  //function_from_numpy

yvals = []
for x in xvals:
    y = cos(x)    //math
    yvals.append(y)

plt.plot(xvals,yvals)
plt.xticks([-4*pi -3*pi -2*pi -pi 0 pi 2*pi 3*pi 4*pi])
plt.show()
