from re import I
from mido import MidiFile
import pretty_midi

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from colour_palettes import CoolPalette, WarmPalette
from score_information import get_all_durations, get_colour_palette, note_sorting_function, get_colour_of_note, get_midi


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


def get_visualization_bar_chart_duration(xpos, ypos, zpos, dx, dy, dz, colours):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    max_y_value = max(ypos) + 10
    ax.set_xlim3d(0, 127)
    ax.set_ylim3d(0, max_y_value)
    ax.set_zlim3d(0, 127)

    # ax.set_axis_off()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colours)
    plt.savefig('pictures/symphony_40_1.png')
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
        ins_name = instrument.name
        instruments_dict[ins_name] = index
        for note in instrument.notes:
            note_info = [note, ins_name]
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
        ins_name = instrument.name
        instruments_dict[ins_name] = index
        for note in instrument.notes:
            note_info = [note, ins_name]
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


if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Bolero_FLVLC.mid')
    bach_andante = get_midi('Prelude/bach_andante.mid')
    figaro_data = get_midi('Figaro/marriage_of_figaro_overture_ORCH.mid')
    vivaldi_summer = get_midi('Summer/Vivaldi_summer_3_STRE.mid')
    visualize_bcd(bolero_data)