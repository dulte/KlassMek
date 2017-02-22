import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import seaborn


xa = 0
xb = 25.
ya = 10.
yb= 0

m = 1
g = 9.81



R = float((xb-xa))/((yb-ya))

f = lambda t: R - (t-np.sin(t))/(np.cos(t) - 1)

theta = fsolve(f,np.pi)
print theta
 

k = (xb-xa)/(theta - np.sin(theta))

# k = 1
# theta = np.pi

t = np.linspace(0,theta,10000)
x = k*(t - np.sin(t))
y = k*(np.cos(t) - 1)


plt.plot(x,ya+y)
plt.plot(xa,ya,"go")
plt.plot(xb,yb,"ro")
plt.title("Brachistochrone")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Brachistochrone","Start","Finish"])
plt.show()
