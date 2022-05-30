
from time import time
from turtle import color

import matplotlib.pyplot as plt

from score_information import get_all_durations, get_colour_palette, get_midi, add_background, get_text_font
from bar_chart import get_all_score_data, get_all_score_data2, add_text
from matplotlib.patches import Arc

from scipy.spatial import Delaunay

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def get_visualization_arc_duration_triangle(score, text_list, with_time, style_data):
    '''
    This function creates Triangular chart visualization focusing on duration.
    '''
    pitches, times, volumes, colours = get_all_score_data(score, with_time)
    palette = get_colour_palette(score)

    cm = 1/2.54  
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=20)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    points = []
    length = len(pitches)
    for i in range(length):
        x1, y1 = pitches[i], times[i]
        point = [x1, y1]
        points.append(point)
        

    plt.scatter(pitches, times, s = 7, color = colours[:])

    patches = []
    start = 0
    end = 3

    a = len(points)//2
    for i in range(a):
        t1 = Polygon(points[start:end], color=colours[start])
        patches.append(t1)
        plt.gca().add_patch(t1)
        start += 2
        end += 2

    plt.axis('off')

    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/results/" + text_list[0] + text_list[1] + "/" + text_list[0] + text_list[1] + str(with_time) +
    str( style_data['colour']) + str( style_data['font']) + str( style_data['placement']) 
    + "triplot_duration.png", 
    bbox_inches = 'tight', pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour
     )
    plt.show()


def get_visualization_arc_volume_triangle(score, text_list, with_time, style_data):
    '''
    This function creates Triangular chart visualization focusing on volume.
    '''
    pitches, times, volumes, colours = get_all_score_data2(score, with_time)
    palette = get_colour_palette(score)

    cm = 1/2.54 
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=20)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    points = []
    length = len(pitches)
    for i in range(length):
        x1, y1 = pitches[i], times[i]
        point = [x1, y1]
        points.append(point)
        

    plt.scatter(pitches, times, s = 7, color = colours[:])

    patches = []
    start = 0
    end = 3

    a = len(points)//3
    for i in range(a):
        t1 = Polygon(points[start:end], color=colours[start])
        patches.append(t1)
        plt.gca().add_patch(t1)
        start += 3
        end += 3

    plt.axis('off')

    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/results/" + text_list[0] + text_list[1] + "/" + text_list[0] + text_list[1] + str(with_time) + 
    str( style_data['colour']) + str( style_data['font']) + str( style_data['placement']) 
    + "triplot_volume.png", 
    bbox_inches = 'tight', pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour
     )
    plt.show()



if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')
    
    bach_air = get_midi('Air/J.-S.-Bach_Air.mid')
    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor.mid')

    bach_andante = get_midi('Prelude/J.-S.-Bach_Andante.mid')

    vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

    oi_u_luzi = get_midi('oi_u_luzi/nation_oi2.mid')

    happy_birthday = get_midi('Happy_Birthday/Happy_Birthday.mid')
    test = get_midi('Happy_Birthday/2_2.mid')
    ddang = get_midi('Happy_Birthday/Stray-Kids_땡-(FREEZE).mid')

    # style_data = {'colour': 5, 'font': 1, 'placement':4}
    # get_visualization_arc_duration_triangle(bolero_data[0], bolero_data[1], False, style_data)
    style_data = {'colour': 2, 'font': 3, 'placement':4}
    get_visualization_arc_volume_triangle(figaro_data[0], figaro_data[1], True, style_data)