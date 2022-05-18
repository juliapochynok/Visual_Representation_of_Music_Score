from cmath import pi
from re import I
from time import time
from turtle import color
from mido import MidiFile
import pretty_midi

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from colour_palettes import CoolPalette, WarmPalette
from score_information import rgb_to_one, get_all_durations, get_colour_palette, note_sorting_function, get_colour_of_note, get_midi
from bar_chart import get_all_score_data, get_all_score_data2, add_text
from matplotlib.patches import Arc


def get_visualization_arc_duration(score, text_list):
    
    pitches, times, volumes, colours = get_all_score_data(score)
        
    plt.style.use('dark_background')
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    fig, ax = plt.subplots(1,1)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    # ax.set_ylim(-10, max_y_value)
    ax.set_ylim(-100, max_y_value)

    transformed_volumes = transform_volumes(volumes, [0, 127], [0, 6])

    for i in range(len(pitches) - 1):
        x1, y1 = pitches[i], times[i]
        x2, y2 = pitches[i + 1], times[i + 1]

        mxmy = mx, my = [(x1 + x2) / 2, (y1 + y2) / 2]
        r = np.sqrt((x1 - mx)**2 + (y1 - my)**2)
        width = 2 * r
        height = 2 * r
        start_angle = np.arctan2(y1 - my, x1 - mx) * 180 / np.pi
        end_angle = np.arctan2(my - y2, mx - x2) * 180 / np.pi

        ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
        # color = colours[-1], 
        # angle = 20,
        #             theta1=0,
                    #  theta2=120, 
                    edgecolor=colours[i],
                     lw=transformed_volumes[i]
                     ))
    plt.scatter(pitches, times, color = colours, s = volumes)
    plt.axis('off')

    add_text(plt, ax, score, text_list)
    # plt.savefig('pictures/22.png')
    plt.show()


def get_visualization_arc_volume(score, text_list):
    pitches, times, volumes, colours = get_all_score_data2(score)
        
    plt.style.use('dark_background')
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    fig, ax = plt.subplots(1,1)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value)

    transformed_volumes = transform_volumes(volumes, [0, max(volumes)], [0, 6])

    for i in range(len(pitches) - 1):
        x1, y1 = pitches[i], times[i]
        x2, y2 = pitches[i + 1], times[i + 1]

        mxmy = mx, my = [(x1 + x2) / 2, (y1 + y2) / 2]
        r = np.sqrt((x1 - mx)**2 + (y1 - my)**2)
        width = 2 * r
        height = 2 * r
        start_angle = np.arctan2(y1 - my, x1 - mx) 
        # * 180 / np.pi
        end_angle = np.arctan2(my - y2, mx - x2) 
        # * 180 / np.pi

        ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
        # color = colours[-1], 
        # angle = 20,
        #             theta1=0,
                    #  theta2=120, 
                    edgecolor=colours[i],
                     lw=transformed_volumes[i]
                    # lw = 1.1
                     ))
    plt.scatter(pitches, times, color = colours, s = volumes)
    plt.axis('off')

    add_text(plt, ax, score, text_list)
    # plt.savefig('pictures/33.png')
    plt.show()


def get_visualization_arc_volume2222(score, text_list):
    pitches, times, volumes, colours = get_all_score_data2(score)
    pitches = [50,50,50]
    times = [1,2,3]
    colours = colours[:3]

    plt.style.use('dark_background')
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    fig, ax = plt.subplots(1,1)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value)

    transformed_volumes = transform_volumes(volumes, [0, max(volumes)], [0, 6])

    for i in range(len(pitches) - 1):
        x1, y1 = pitches[i], times[i]
        x2, y2 = pitches[i + 1], times[i + 1]

        mxmy = mx, my = [(x1 + x2) / 2, (y1 + y2) / 2]
        r = np.sqrt((x1 - mx)**2 + (y1 - my)**2)
        width = 2 * r
        height = 2 * r
        start_angle = np.arctan2(y1 - my, x1 - mx) * 180 / np.pi
        end_angle = np.arctan2(my - y2, mx - x2) * 180 / np.pi
        # end_angle = np.arctan2(y2 - my, x2 - mx)  * 180 / np.pi

        ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
        # color = colours[-1], 
        # angle = 20,
        #             theta1=0,
                    #  theta2=120, 
                    edgecolor=colours[i],
                     lw=transformed_volumes[i]
                    # lw = 1.1
                     ))
    plt.scatter(pitches, times, color = colours, s = volumes)
    plt.axis('off')

    add_text(plt, ax, score, text_list)
    # plt.savefig('pictures/33.png')
    plt.show()

# def lalala():
    # pitches, times, volumes, colours = get_all_score_data2(score)
    # pitches = [2, 5, 20, 50, 60, 50, 50, 2, 20, 20, 20, 20]
    # times = [1, 1, 1, 1, 1, 2, 3, 2, 2, 3, 4, 5]
    # colours = colours[:12]

    # # Calculate the xy coords for each point on the circle
    # s = 2 * np.pi / npoints
    # verts = np.zeros((npoints, 2))
    # for i in np.arange(npoints):
    #     angle = s * i
    #     x = npoints * np.cos(angle)
    #     y = npoints * np.sin(angle)
    #     verts[i] = [x, y]

    # # Plot the Bezier curves
    # numbers = [i for i in xrange(npoints)]
    # bezier_path = np.arange(0, 1.01, 0.01)
    # for a, b in itertools.product(numbers, repeat=2):
    #     if a == b:
    #         continue

    #     x1y1 = x1, y1 = verts[a]
    #     x2y2 = x2, y2 = verts[b]

    #     xbyb = xb, yb = [0, 0]

    #     # Compute and store the Bezier curve points
    #     x = (1 - bezier_path)** 2 * x1 + 2 * (1 - bezier_path) * bezier_path * xb + bezier_path** 2 * x2
    #     y = (1 - bezier_path)** 2 * y1 + 2 * (1 - bezier_path) * bezier_path * yb + bezier_path** 2 * y2

    #     ax.plot(x, y, 'k-')

    # x, y = verts.T
    # ax.scatter(x, y, marker='o', s=50, c='r')

    # ax.set_xlim(-npoints - 5, npoints + 6)
    # ax.set_ylim(-npoints - 5, npoints + 6)
    # ax.set(aspect=1)

def transform_volumes(volumes, old_range, new_range):
    old_range_val = (old_range[1] - old_range[0])  
    new_range_val = (new_range[1] - new_range[0])  
    new_volumes = []

    for el in volumes:
        new_el = (((el - old_range[0]) * new_range_val) / old_range_val) + new_range[0]
        new_volumes.append(new_el)
    return new_volumes



# def arc(dot1, dot2, ax):
    
#     return arc

if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')
    
    bach_air = get_midi('Air/Johann-Sebastian-Bach_Air.mid')

    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor-BWV-565.mid')
    bach_andante = get_midi('Prelude/J.-S.-Bach_Andante.mid')

    vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

    oi_u_luzi = get_midi('oi_u_luzi/nation_oi2.mid')

    happy_birthday = get_midi('Happy_Birthday/Happy_Birthday.mid')
    test = get_midi('Happy_Birthday/2_2.mid')
    # visualize_bcd_2d(symphony_40)
    # visualize_bcd(symphony_40)
    # spiral(bolero_data)

    # get_visualization_arc_duration(test[0], test[1])
    get_visualization_arc_volume2222(bolero_data[0], bolero_data[1])