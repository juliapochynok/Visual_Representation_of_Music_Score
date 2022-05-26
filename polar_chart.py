import copy
from tkinter import font
from turtle import color
import matplotlib.pyplot as plt
from math import pi
from mpl_toolkits import mplot3d
import pretty_midi
import matplotlib.patheffects as path_effects

from visualizations import rgb_to_one
from score_information import get_midi, get_colour_palette, add_background, get_text_font


# build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height

# times: [times in seconds from smallest to biggest]
# pitches: for instr [1,2,3,4]
def get_visualization_polar_piano_roll(score, text_list, style_data):

    cm = 1/2.54  # centimeters in inches
    fig = plt.figure(figsize=(25*cm, 25*cm), linewidth=4)

    ax = fig.add_subplot(111, polar=True)
    ax.set_theta_direction(-1)
    ax.set_theta_offset(pi)
    
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    times = []

    palette = get_colour_palette(score)
    all_colours = palette.all_colours()
    
    amount_of_instrumnets = len(score.instruments)

    for instrument in score.instruments:
        for note in instrument.notes:
            if note.start not in times:
                times.append(note.start)
                times.sort()

    index = 0
    for instrument in score.instruments:
        ins_name = instrument.name
        current_times = copy.deepcopy(times)
        current_pitches = [0 for i in range(len(current_times))]

        for note in instrument.notes:
            current_index = current_times.index(note.start)
            current_pitches[current_index] = note.pitch

        angles = [n / float(len(current_times)) * 2 * pi for n in range(len(current_times))]
        angles += angles[:1]

        current_pitches += current_pitches[:1] 
        current_colour = all_colours[index]
        current_colour_rgb = [rgb_to_one(current_colour[0]), rgb_to_one(current_colour[1]), rgb_to_one(current_colour[2])]
        ax.plot(angles, current_pitches, linewidth=1,
                linestyle='solid',c = current_colour_rgb, label=ins_name)
        
        if amount_of_instrumnets < 3:
            ax.fill(angles, current_pitches, c = current_colour_rgb, alpha=0.4)
        index += 1
       
    ax.set_ylim(0, 127)
    plt.axis('off')
    ax.set_yticks([])
    ax.set_xticks([])

    palette = get_colour_palette(score)
    background_colour, edge_colour = add_background(palette,  style_data['colour'])
    fig.patch.set_facecolor(background_colour)
    
    sel_font = get_text_font( style_data['font'])
   
    add_text(plt, ax, score, text_list,  style_data['placement'], edge_colour, sel_font)
    plt.savefig("pictures/" + text_list[0] + text_list[1] + "polar.png", 
    bbox_inches = 'tight',pad_inches = 0, 
     facecolor=fig.get_facecolor(), edgecolor=edge_colour)
    plt.show()


def add_text(curr_plt, ax, score, text_list, number, colour, sel_font):
    if number == 1:
        ax.set_thetamin(1)
        ax.set_thetamax(359)
        add_text1(curr_plt, ax, score, text_list, colour, sel_font)
    elif number == 2:
        ax.set_theta_zero_location('W')
        ax.set_thetamin(1)
        ax.set_thetamax(359)
        add_text2(curr_plt, ax, score, text_list, colour, sel_font)
    else:
        ax.set_thetamin(10)
        ax.set_thetamax(349)
        add_text3(curr_plt, ax, score, text_list, colour, sel_font)
        


def add_text1(curr_plt, ax, score, text_list, colour, sel_font):

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


def add_text2(curr_plt, ax, score, text_list, colour, sel_font):
    if len(text_list[0]) + len(text_list[1]) > 27:
        ax.set_rorigin(-40)
    elif len(text_list[0]) + len(text_list[1]) > 20:
        ax.set_rorigin(-32)
    else:
        ax.set_rorigin(-20)

    text = curr_plt.text(0.5*(left+right), 0.515*(bottom+top), text_list[0] + "\n" + text_list[1],
        horizontalalignment='center',
        verticalalignment='top',
        fontweight=900,
        fontsize='large',
        transform=ax.transAxes,
        color = colour,
        **sel_font)

    return curr_plt


def add_text3(curr_plt, ax, score, text_list, colour, sel_font):

    if len(text_list[0]) + len(text_list[1]) < 24:
        text = curr_plt.text(0.3 * (left + right), 0.510*(bottom+top), text_list[0] + " | " + text_list[1],
            horizontalalignment='center',
            verticalalignment='top',
            fontweight=900,
            fontsize='x-large',
            transform=ax.transAxes,
            color = colour,
            **sel_font)
    else:
        if len(text_list[0]) < len(text_list[1]):
            first = text_list[0]
            second = text_list[1]
        else:
            first = text_list[1]
            second = text_list[0]
        text = curr_plt.text(0.15 * (left + right), 0.525*(bottom+top), first + " \n" + second,
            horizontalalignment='left',
            verticalalignment='top',
            fontweight=800,
            fontsize='x-large',
            transform=ax.transAxes,
            color = colour,
            **sel_font)

    return curr_plt



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

    ddang = get_midi('Happy_Birthday/Stray-Kids_땡-(FREEZE).mid')

    style_data = {'colour': 3, 'font': 2, 'placement':3}
    get_visualization_polar_piano_roll(bach_andante[0], bach_andante[1], style_data)
    