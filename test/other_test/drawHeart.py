'''
极坐标方程
水平方向： r=a(1-cosθ) 或 r=a(1+cosθ) (a>0)
垂直方向： r=a(1-sinθ) 或 r=a(1+sinθ) (a>0)
直角坐标方程
心形线的平面直角坐标系方程表达式分别为 x^2+y^2+a*x=a*sqrt(x^2+y^2) 和 x^2+y^2-a*x=a*sqrt(x^2+y^2）
参数方程
x=a*(2*cos(t)-cos(2*t))
y=a*(2*sin(t)-sin(2*t))
所围面积为3/2*PI*a^2，形成的弧长为8a
————————————————
版权声明：本文为CSDN博主「MyHuster」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/thao6626/article/details/46639749
'''


import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math


def drawHeart():
    t = np.linspace(0, math.pi, 1000)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 2)
    plt.plot(x, y, color='red', linewidth=2, label='h')
    plt.plot(-x, y, color='red', linewidth=2, label='-h')
    plt.xlabel('t')
    plt.ylabel('h')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

    plt.legend()
    plt.show()

def drawHeart_animation():
    figure = plt.figure()
    axes = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    line1, = axes.plot([], [], color='red', linewidth=2, label='1')
    line2, = axes.plot([], [], color='red', linewidth=2, label='2')


    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2


    def animate(i):
        t = np.linspace(0, i / math.pi, 1000)
        x = 2*(np.sin(t))
        y = 2*(np.cos(t) + np.power(x, 2.0 / 3))

        # t = np.linspace(0, i, 1000)
        # y = 2 * (2 * np.cos(t) - np.cos(2 * t))
        # x = 2 * (2 * np.sin(t) - np.sin(2 * t))

        line1.set_data(x, y)
        line2.set_data(-x, y)
        return line1,line2


    ani = animation.FuncAnimation(figure, animate, init_func=init, frames=14, interval=200)
    # ani.save('Heart.mp4')  save as mp4 but need to install video-encoder. i did not install it, so this line makes exeception
    plt.show()


# drawHeart()
drawHeart_animation()