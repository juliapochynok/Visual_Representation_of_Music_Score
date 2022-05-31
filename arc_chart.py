import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from score_information import rgb_to_one, get_all_durations, get_colour_palette, note_sorting_function, get_colour_of_note, get_midi, add_background, get_text_font
from bar_chart import get_all_score_data, get_all_score_data2, add_text
from matplotlib.patches import Arc


def get_visualization_arc_duration(score, text_list, style_data):
    '''
    This function creates Arc chart visualization focusing on duration.
    '''
    pitches, times, volumes, colours = get_all_score_data(score, False)
    palette = get_colour_palette(score)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]
    
    cm = 1/2.54 
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=20)
    max_y_value = max(times)
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value + 10)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    transformed_volumes = transform_volumes(volumes, [0, 127], [0, 6])

    for i in range(len(pitches) - 1):
        x1, y1 = pitches[i], times[i]
        x2, y2 = pitches[i + 1], times[i + 1]

        mxmy = mx, my = [(x1 + x2) / 2, (y1 + y2) / 2]
        r = np.sqrt((x1 - mx)**2 + (y1 - my)**2)
        width = 2 * r
        height = 2 * r
        start_angle = np.arctan2(y1 - my, x1 - mx) 
        end_angle = np.arctan2(my - y2, mx - x2) 

        ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
                    edgecolor=colours[i],
                     lw=transformed_volumes[i], zorder=0
                     ))

    plt.scatter(pitches, times, color = colours, s = volumes, zorder=2)
    plt.axis('off')

    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/results/" 
    # + text_list[0] + text_list[1] +  "/"   //uncomment if seperate fonder for score exists
    + text_list[0] + text_list[1] +
    str( style_data['colour']) + str( style_data['font']) + str( style_data['placement']) 
    + "arc_duration.png", 
    bbox_inches = 'tight',pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour)
    plt.show()


def get_visualization_arc_volume(score, text_list, style_data):
    '''
    This function creates Arc chart visualization focusing on volume.
    '''
    pitches, times, volumes, colours = get_all_score_data2(score, False)
    palette = get_colour_palette(score)

    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    cm = 1/2.54 
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=20)
    max_y_value = max(times)
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value + 10)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    transformed_volumes = transform_volumes(volumes, [0, max(volumes)], [0, 6])

    for i in range(len(pitches) - 1):
        x1, y1 = pitches[i], times[i]
        x2, y2 = pitches[i + 1], times[i + 1]

        mxmy = mx, my = [(x1 + x2) / 2, (y1 + y2) / 2]
        r = np.sqrt((x1 - mx)**2 + (y1 - my)**2)
        width = 2 * r
        height = 2 * r
        start_angle = np.arctan2(y1 - my, x1 - mx) 
        end_angle = np.arctan2(my - y2, mx - x2) 
       
        try:
            ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
                        edgecolor=colours[i],
                        lw=transformed_volumes[i], zorder=0
                        ))
        except:
            print("tried")
    plt.scatter(pitches, times, color = colours, s = volumes, zorder=2)
    plt.axis('off')

    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/results/" 
    # + text_list[0] + text_list[1] + "/"  //uncomment if seperate fonder for score exists
    + text_list[0] + text_list[1] +
    str( style_data['colour']) + str( style_data['font']) + str( style_data['placement']) 
    + "arc_volume.png", 
    bbox_inches = 'tight', pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour
     )
    plt.show()


def transform_volumes(volumes, old_range, new_range):
    '''
    This function transforms volume values from one range to another
    '''
    old_range_val = (old_range[1] - old_range[0])  
    new_range_val = (new_range[1] - new_range[0])  
    new_volumes = []

    for el in volumes:
        new_el = (((el - old_range[0]) * new_range_val) / old_range_val) + new_range[0]
        new_volumes.append(new_el)
    return new_volumes



if __name__ == '__main__':
    bach_air = get_midi('Air/J.-S.-Bach_Air.mid')
    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor.mid')

    bach_andante = get_midi('Prelude/J.-S.-Bach_Andante.mid')
    
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

    figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')
    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

    style_data = {'colour': 5, 'font': 2, 'placement':4}
    get_visualization_arc_volume(bach_air[0], bach_air[1], style_data)
