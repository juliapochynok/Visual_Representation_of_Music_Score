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

from matplotlib.pyplot import *
from numpy import *
import math
from matplotlib import patches
from matplotlib.patches import Arc

csfont = {'fontname':'Comic Sans MS'}
hfont = {'fontname':'Helvetica'}

# xpos - note number
# ypos - time(first,second)
# zpos - [0,0,0,0,0]
# dx, dy - [1,1,1,1,1]
# dz - note volume
# colours - [1, 0, 0, alpha]
# alpha - note duration

# z - volume, opacity - duration
def visualize_bcd(score):
    pitches, times, volumes, colours = get_all_score_data(score)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]
    get_visualization_bar_chart_duration(pitches, times, zpos, dx, dy, volumes, colours)


# z - duration, opacity - volume
def visualize_bcv(score):
    pitches, times, volumes, colours = get_all_score_data2(score)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    get_visualization_bar_chart_volume(pitches, times, zpos, dx, dy, volumes, colours, score)


def visualize_bcd_2d(score, text_list):
    # duration
    pitches, times, volumes, colours = get_all_score_data(score)
    # volume
    # pitches, times, volumes, colours = get_all_score_data2(score)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]
    get_visualization_bar_chart_duration_2d(pitches, times, zpos, dx, dy, volumes, colours, score, text_list)


def get_visualization_bar_chart_duration_2d(xpos, ypos, zpos, dx, dy, dz, colours, score, text_list):

    print("pitches")
    print(xpos)
    print("times")
    print(ypos)
    print("volumes")
    print(dz)
    print("colours")
    print(colours)
    all_durations = get_all_durations(score)
    print("durations")
    print(all_durations)

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1,1)
    plt.scatter(xpos, ypos, color = colours, s = dz)

    plt.xlim([0, 127])
    plt.axis('off')
    add_text(plt, ax, score, text_list)
    # plt.savefig('pictures/2.png')
    plt.show()
    

# def spiral(score):
#     pitches, times, volumes, colours = get_all_score_data(score)
#     # volume
#     # pitches, times, volumes, colours = get_all_score_data2(score)
        
#     dx = np.ones(len(pitches)) 
#     dy = np.ones(len(pitches)) 
#     zpos = [0 for x in range(len(pitches))]

#     # r = linspace(0,20,360)
#     # t = linspace(0,2000,360)
#     # for i in range(len(times)):
#     #     x = pitches[i]*math.cos(math.radians(times[i]))
#     #     y = pitches[i]*math.sin(math.radians(times[i]))

#     r = linspace(0,20,360)
#     t = linspace(0,2000,360)
#     x = r*math.cos(math.radians(t))
#     y = r*math.sin(math.radians(t))

#     plot(x,y)
#     plt.show()


def get_visualization_bar_chart_duration(xpos, ypos, zpos, dx, dy, dz, colours):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    max_y_value = max(ypos) + 10
    ax.set_xlim3d(0, 127)
    ax.set_ylim3d(0, max_y_value)
    ax.set_zlim3d(0, 127)

    ax.set_axis_off()
    ax.azim = -90
    ax.dist = 5
    ax.elev = 84
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colours)
    # plt.savefig('pictures/symphony_40_1.png')
    plt.show()
    
def get_visualization_bar_chart_volume(xpos, ypos, zpos, dx, dy, dz, colours, score):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    max_y_value = max(ypos) + 10
    ax.set_xlim3d(0, 127)
    ax.set_ylim3d(0, max_y_value)
    all_durations = get_all_durations(score)
    max_duration = max(all_durations)
    ax.set_zlim3d(0, max_duration)
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colours)
    plt.show()

def get_all_score_data(score):
    pitches = []
    times = []
    volumes = []
    colours = []

    all_durations = get_all_durations(score)
    max_duration = max(all_durations)

    palette = get_colour_palette(score)
    all_colours = palette.all_colours()
    instruments_dict = {}
    sorted_notes = []
    index = 0
    for instrument in score.instruments:
        ins_code = instrument.program
        instruments_dict[ins_code] = index
        for note in instrument.notes:
            note_info = [note, ins_code]
            sorted_notes.append(note_info)
        index += 1

    sorted_notes.sort(key=note_sorting_function)   

    for current_note in sorted_notes:
        pitches.append(current_note[0].pitch)
        volumes.append(current_note[0].velocity)

        full_colour = get_colour_of_note(instruments_dict, all_colours,
        current_note[0].duration, max_duration, current_note[1])

        colours.append(full_colour)
        amount = pitches.count(current_note[0].pitch)
        times.append(amount + 1)

    return pitches, times, volumes, colours


def get_all_score_data2(score):
    pitches = []
    times = []
    durations = []
    colours = []

    palette = get_colour_palette(score)
    all_colours = palette.all_colours()
    instruments_dict = {}
    sorted_notes = []
    index = 0
    for instrument in score.instruments:
        ins_code = instrument.program
        instruments_dict[ins_code] = index
        for note in instrument.notes:
            note_info = [note, ins_code]
            sorted_notes.append(note_info)
        index += 1

    sorted_notes.sort(key=note_sorting_function)   

    for current_note in sorted_notes:
        pitches.append(current_note[0].pitch)
        durations.append(current_note[0].duration)

        full_colour = get_colour_of_note(instruments_dict, all_colours,
        current_note[0].velocity, 127, current_note[1])

        colours.append(full_colour)
        amount = pitches.count(current_note[0].pitch)
        times.append(amount + 1)

    return pitches, times, durations, colours


def add_text(curr_plt, ax, score, text_list):
    palette = get_colour_palette(score)
    all_colours = palette.all_colours()

    curr_plt.text(0.05, 0.95, text_list[0],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        color=[rgb_to_one(all_colours[-1][0]),rgb_to_one(all_colours[-1][1]), rgb_to_one(all_colours[-1][2])],
        **csfont)

    curr_plt.text(0.05, 0.90, text_list[1],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        color=[rgb_to_one(all_colours[-1][0]),rgb_to_one(all_colours[-1][1]), rgb_to_one(all_colours[-1][2])],
        **csfont)
    return curr_plt

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

    visualize_bcd_2d(happy_birthday[0], happy_birthday[1])
    # visualize_bcd(bolero_data[0])
    # spiral(bolero_data)