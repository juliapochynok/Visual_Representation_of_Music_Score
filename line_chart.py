import copy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from math import pi
import pretty_midi

from visualizations import rgb_to_one
from score_information import get_colour_palette, get_midi


def get_visualization_durations(score):

    fig, ax = plt.subplots()
    
    durations_amount = {}

    palette = get_colour_palette(score)
    all_colours = palette.all_colours()

    max_duration = 0
    index = 0
    for instrument in score.instruments:
        for note in instrument.notes:
            duration = note.duration
            if duration in durations_amount:
                durations_amount[duration] += 1
            else:
                durations_amount[duration] = 1
    
        sorted_durations_amount = dict(sorted(durations_amount.items()))
        
        current_colour = all_colours[index]
        current_colour_rgb = [rgb_to_one(current_colour[0]), rgb_to_one(current_colour[1]), rgb_to_one(current_colour[2])]
        
        durations = list(sorted_durations_amount.keys())
        amounts = list(sorted_durations_amount.values())
        # plt.plot(durations, amounts, color=current_colour_rgb, marker='o')
        plt.plot(durations, amounts, color=current_colour_rgb)
        plt.fill_between(durations, amounts, color=current_colour_rgb, alpha=.3)
        index += 1
        if max(durations) > max_duration:
            max_duration = max(durations)

    
    # ax.set_yticks([0.2, 0.6, 0.8], minor=False)
    # ynew = 0.3
    # ax.axhline(ynew)

    beats = score.get_beats()
    time_signatures = score.time_signature_changes
    numerator = time_signatures[0].numerator

    ticks = []
    for i in range(numerator + 1):
        ticks.append(beats[i])
    

    ax.set_xticks(ticks, minor=False)
    ax.xaxis.grid(True, which='major')
    plt.xlim(0, max_duration)
    plt.savefig('pictures/symphony_40_2.png')
    plt.show()


if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Bolero_FLVLC.mid')
    bach_andante = get_midi('Prelude/bach_andante.mid')
    figaro_data = get_midi('Figaro/marriage_of_figaro_overture_ORCH.mid')
    vivaldi_summer = get_midi('Summer/Vivaldi_summer_3_STRE.mid')
    get_visualization_durations(bach_andante)
    