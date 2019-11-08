from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
X, Y = np.meshgrid(x, y) # 网格的创建，生成二维数组
#X=np.array(x)
#Y=np.array(y)
print(type(X),X)
#Z = np.sin(X) * np.cos(Y)
#Z=X4+Y2
#Z=-X2-Y2
#Z=2X+2Y
Z=4*np.sin(X)+Y**2
#print(type(Z),Z)
plt.xlabel('x')
plt.ylabel('y')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
