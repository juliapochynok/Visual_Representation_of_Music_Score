import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from score_information import rgb_to_one, get_all_durations, get_colour_palette, note_sorting_function, get_colour_of_note, get_midi, add_background, get_text_font
from bar_chart import get_all_score_data, get_all_score_data2, add_text
from matplotlib.patches import Arc


def get_visualization_arc_duration(score, text_list, style_data):
    
    pitches, times, volumes, colours = get_all_score_data(score, False)
    palette = get_colour_palette(score)
        
    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]
    
    cm = 1/2.54  # centimeters in inches
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=4)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value)
    # ax.set_ylim(-100, max_y_value)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    # a = get_multiplier(score)
    transformed_volumes = transform_volumes(volumes, [0, 127], [0, 6])

    for i in range(len(pitches) - 1):
        x1, y1 = pitches[i], times[i]
        x2, y2 = pitches[i + 1], times[i + 1]

        mxmy = mx, my = [(x1 + x2) / 2, (y1 + y2) / 2]
        r = np.sqrt((x1 - mx)**2 + (y1 - my)**2)
        width = 2 * r
        height = 2 * r
        start_angle = np.arctan2(y1 - my, x1 - mx) 
        # * 180 
        # / np.pi
        end_angle = np.arctan2(my - y2, mx - x2) 
        # * 180 
        # / np.pi

        ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
        # color = colours[-1], 
        # angle = 20,
        #             theta1=0,
                    #  theta2=120, 
                    edgecolor=colours[i],
                     lw=transformed_volumes[i], zorder=0
                     ))

    plt.scatter(pitches, times, color = colours, s = volumes, zorder=2)
    plt.axis('off')

    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/" + text_list[0] + text_list[1] + "arc_duration.png", 
    bbox_inches = 'tight',pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour)
    # plt.savefig('pictures/22.png')
    plt.show()


# def get_multiplier(score):
#     tempos = score.get_tempo_changes()
#     print(tempos)
#     if len(tempos) > 1:
#         tempo = tempos[1][0]
#     else:
#         tempo = tempo[0][0]    
#     if tempo < 80:
#         return 0.5
#     elif 80 < tempo < 100:
#         return 1
#     elif 100 < tempo < 120:
#         return 1.5
#     elif 120 < tempo < 150:
#         return 2
#     else:
#         return 2.5

def get_visualization_arc_volume(score, text_list, style_data):
    pitches, times, volumes, colours = get_all_score_data2(score, False)
    palette = get_colour_palette(score)

    dx = np.ones(len(pitches)) 
    dy = np.ones(len(pitches)) 
    zpos = [0 for x in range(len(pitches))]

    cm = 1/2.54  # centimeters in inches
    fig, ax = plt.subplots(1,1, figsize=(25*cm, 25*cm), linewidth=4)
    max_y_value = max(times) + 10
    ax.set_xlim(0, 127) 
    ax.set_ylim(-10, max_y_value)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    transformed_volumes = transform_volumes(volumes, [0, max(volumes)], [0, 6])
    # transformed_volumes = transform_volumes(volumes, [0, max(volumes)], [0, 20])

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
        try:
            ax.add_patch(Arc(mxmy, width, height, start_angle, end_angle, 
            # color = colours[-1], 
            # angle = 20,
            #             theta1=0,
                        #  theta2=120, 
                        edgecolor=colours[i],
                        lw=transformed_volumes[i], zorder=0
                        # lw = 1.1
                        ))
        except:
            print("tried")
    plt.scatter(pitches, times, color = colours, s = volumes, zorder=2)
    plt.axis('off')

    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])

    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/" + text_list[0] + text_list[1] + "arc_volume.png", 
    bbox_inches = 'tight', pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour
     )
    plt.show()


def transform_volumes(volumes, old_range, new_range):
    old_range_val = (old_range[1] - old_range[0])  
    new_range_val = (new_range[1] - new_range[0])  
    new_volumes = []

    for el in volumes:
        new_el = (((el - old_range[0]) * new_range_val) / old_range_val) + new_range[0]
        new_volumes.append(new_el)
    return new_volumes



if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')
    
    bach_air = get_midi('Air/J.-S.-Bach_Air.mid')
    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-Dmin.mid')

    bach_andante = get_midi('Prelude/J.-S.-Bach_Andante.mid')

    vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

    oi_u_luzi = get_midi('oi_u_luzi/nation_oi2.mid')

    happy_birthday = get_midi('Happy_Birthday/Happy_Birthday.mid')
    test = get_midi('Happy_Birthday/2_2.mid')
    ddang = get_midi('Happy_Birthday/Stray-Kids_땡-(FREEZE).mid')

    style_data = {'colour': 0, 'font': 1, 'placement':1}
    get_visualization_arc_duration(symphony_40[0], symphony_40[1], style_data)
    get_visualization_arc_volume(symphony_40[0], symphony_40[1], style_data)