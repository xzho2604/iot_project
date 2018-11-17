import matplotlib.pyplot as plt
import numpy as np


def plot_show(x,y,m,n):
    img = plt.imread("../report/floorplan.png")
    plt.scatter(x, y, marker='*', c='r')
    plt.scatter(m, n, marker='+', c='b')
    plt.imshow(img, zorder=0, extent=[0,42,0,5])
    plt.show()


