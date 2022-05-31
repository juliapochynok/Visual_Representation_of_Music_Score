import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from score_information import rgb_to_one, get_all_durations, get_colour_palette, note_sorting_function, get_colour_of_note, get_midi, add_background, get_text_font

from matplotlib.pyplot import *
from numpy import *
import matplotlib.patheffects as path_effects


# build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

# z - volume, opacity - duration
def visualize_bcd(score):
    '''
    This function creates Bar chart visualization focusing on duration.
    '''
    pitches, times, volumes, colours = get_all_score_data(score, True)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]
    get_visualization_bar_chart_duration(pitches, times, zpos, dx, dy, volumes, colours)


# z - duration, opacity - volume
def visualize_bcv(score):
    '''
    This function creates Bar chart visualization focusing on volume.
    '''
    pitches, times, volumes, colours = get_all_score_data2(score, True)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    get_visualization_bar_chart_volume(pitches, times, zpos, dx, dy, volumes, colours, score)


def visualize_bcdv_2d(score, text_list, focus_string, style_data, temporality):
    '''
    This function creates Bar chart visualization focusing on duration or volume.
    '''
    if focus_string == 'duration':
        pitches, times, volumes, colours = get_all_score_data(score, temporality)
    else:
        pitches, times, volumes, colours = get_all_score_data2(score, temporality)

    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]
    get_visualization_bar_chart_duration_2d(pitches, times, zpos, dx, dy, volumes, colours, score, text_list, style_data, focus_string)

def visualize_bcdav_2d(score, text_list, style_data):
    '''
    This function creates Bar chart visualization focusing
    on both duration or volume.
    '''
    pitches, times, volumes, colours = get_all_score_data(score, True)
    pitches1, times1, volumes1, colours1 = get_all_score_data2(score, True)
    
    cm = 1/2.54 
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=20)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    ax.scatter(pitches, times, color = colours, s = volumes, zorder=1)

    ax.scatter(pitches1, times1, color = colours1, s = volumes1, zorder=2)

    plt.xlim([0, 127])
    plt.ylim([-10, max(times) + 10])
    plt.axis('off')

    palette = get_colour_palette(score)
    background_colour, edge_colour = add_background(palette, style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font(style_data['font'])

    add_text(plt, ax, score, text_list, style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/results/" 
    # + text_list[0] + text_list[1] +  "/"   //uncomment if seperate fonder for score exists
    + text_list[0] + text_list[1] +
    str( style_data['colour']) + str( style_data['font']) + str( style_data['placement']) 
     + "visualize_bcdav_2d.png", 
    bbox_inches = 'tight', pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour
     )
    plt.show()



def get_visualization_bar_chart_duration_2d(xpos, ypos, zpos, dx, dy, dz, colours, score, text_list, style_data, focus_string):
    '''
    This function gets input data about score and plots
    Bar chart visualization focusing on duration in 2D.
    '''
    cm = 1/2.54 
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=20)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())


    plt.scatter(xpos, ypos, color = colours, s = dz)
    plt.xlim([0, 127])
    plt.ylim([-5, max(ypos) + 10])
    plt.axis('off')

    palette = get_colour_palette(score)
    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/results/" + text_list[0] + text_list[1] +  "/" + text_list[0] + text_list[1] + focus_string + 
    str( style_data['colour']) + str( style_data['font']) + str( style_data['placement']) 
    + "_get_visualization_bar_chart_duration_2d.png", 
    bbox_inches = 'tight', pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour
     )
    plt.show()
    


def get_visualization_bar_chart_duration(xpos, ypos, zpos, dx, dy, dz, colours):
    '''
    This function gets input data about score and plots
    Bar chart visualization focusing on duration in 3D.
    '''
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
    plt.show()
    
def get_visualization_bar_chart_volume(xpos, ypos, zpos, dx, dy, dz, colours, score):
    '''
    This function gets input data about score and plots
    Bar chart visualization focusing on volume in 3D.
    '''
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

def get_all_score_data(score, with_time):
    '''
    This function collects and processes data about score
    and returns lists of pitches, times, volumes and colours
    '''
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
        if with_time:
            times.append(current_note[0].start)
        else:
            times.append(amount + 1)

    return pitches, times, volumes, colours


def get_all_score_data2(score, with_time):
    '''
    This function collects and processes data about score
    and returns lists of pitches, times, volumes and colours
    '''
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
        durations.append(current_note[0].duration * 10)

        full_colour = get_colour_of_note(instruments_dict, all_colours,
        current_note[0].velocity, 127, current_note[1])

        colours.append(full_colour)
        amount = pitches.count(current_note[0].pitch)
        if with_time:
            times.append(current_note[0].start)
        else:
            times.append(amount + 1)

    return pitches, times, durations, colours


def add_text(curr_plt, ax, score, text_list, number, colour, sel_font):
    '''
    This function adds title in one of the placements 
    '''
    if number == 1:
        add_text1(curr_plt, ax, score, text_list, colour, sel_font)
    elif number == 2:
        add_text2(curr_plt, ax, score, text_list, colour, sel_font)
    elif number == 3:
        add_text3(curr_plt, ax, score, text_list, colour, sel_font)
    else:
        add_text4(curr_plt, ax, score, text_list, colour, sel_font)
        

def add_text1(curr_plt, ax, score, text_list, colour, sel_font):
    '''
    This function adds title in first possible placement 
    '''
    palette = get_colour_palette(score)
    all_colours = palette.all_colours()

    curr_plt.text(0.07*(left+right), 0.95*(bottom+top), text_list[0],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontweight=900,
        fontsize='xx-large',
        color=colour,
        **sel_font)

    curr_plt.text(0.07*(left+right), 0.9*(bottom+top), text_list[1],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontweight=900,
        fontsize='xx-large',
        color=colour,
        **sel_font)
    return curr_plt

def add_text2(curr_plt, ax, score, text_list, colour, sel_font):
    '''
    This function adds title in second possible placement 
    '''
    text = curr_plt.text(0.5*(left+right), 0.517*(bottom+top), text_list[0] + " | " + text_list[1],
        horizontalalignment='center',
        verticalalignment='top',
        fontweight=900,
        fontsize='xx-large',
        transform=ax.transAxes,
        color = colour,
        **sel_font)
    text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                       path_effects.Normal()])
    return curr_plt


def add_text3(curr_plt, ax, score, text_list, colour, sel_font):
    '''
    This function adds title in third possible placement 
    '''
    palette = get_colour_palette(score)
    all_colours = palette.all_colours()

    curr_plt.text(0.07*(left+right), 0.93*(bottom+top), text_list[0],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontweight=900,
        fontsize='xx-large',
        color=colour,
        **sel_font)

    curr_plt.text((0.93-(len(text_list[1])/100))*(left+right), 0.93*(bottom+top), text_list[1],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontweight=900,
        fontsize='xx-large',
        color=colour,
        **sel_font)
    return curr_plt


def add_text4(curr_plt, ax, score, text_list, colour, sel_font):
    '''
    This function adds title in fourth possible placement 
    '''
    palette = get_colour_palette(score)
    all_colours = palette.all_colours()

    curr_plt.text(0.07*(left+right), 0.07*(bottom+top), text_list[0],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontweight=900,
        fontsize='xx-large',
        color=colour,
        **sel_font)

    curr_plt.text((0.93-(len(text_list[1])/100))*(left+right), 0.07*(bottom+top), text_list[1],
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes,
        fontweight=900,
        fontsize='xx-large',
        color=colour,
        **sel_font)
    return curr_plt

if __name__ == '__main__':
    bach_air = get_midi('Air/J.-S.-Bach_Air.mid')
    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor.mid')

    bach_andante = get_midi('Prelude/J.-S.-Bach_Andante.mid')
    
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

    figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')
    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

    style_data = {'colour': 2, 'font': 3, 'placement':4}
    visualize_bcdav_2d(figaro_data[0], figaro_data[1], style_data)