import matplotlib.pyplot as plt
import numpy as np


def plot_show():
    img = plt.imread("../report/floorplan.png")
    plt.scatter(1, 1, marker='*', c='r')
    plt.imshow(img, zorder=0, extent=[0,42,0,5])
    plt.show()


plot_show()