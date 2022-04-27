import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
from score_information import rgb_to_one, rgb_to_one
from colour_palettes import CoolPalette, WarmPalette

from math import pi

def colour_visualization(palette):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [1,2,3,4,5,6,7,8,9,10,11,12]
    z = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    colours = []

    all_colours = palette.all_colours()
    for colour in all_colours:
        colours.append([rgb_to_one(colour[0]), rgb_to_one(colour[1]), rgb_to_one(colour[2])])

    dx = np.ones(len(x)) 
    dy = np.ones(len(x)) 
    zpos = [0 for x in range(len(x))]
    ax.set_xlim3d(0, 13)
    ax.set_ylim3d(0, 13)
    ax.set_zlim3d(0, 13)
    ax.bar3d(x, y, zpos, dx, dy, z, color=colours)
    plt.show()


if __name__ == '__main__':
    colour_visualization(WarmPalette)
    colour_visualization(CoolPalette)