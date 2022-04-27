import copy
import matplotlib.pyplot as plt
from math import pi
from mpl_toolkits import mplot3d
import pretty_midi

from visualizations import rgb_to_one
from score_information import get_midi, get_colour_palette

# times: [times in seconds from smallest to biggest]
# pitches: for instr [1,2,3,4]
#  
def get_visualization_polar_piano_roll(score):

    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, polar=True)
    ax.set_theta_direction(-1)
    ax.set_theta_offset(pi)

    times = []

    palette = get_colour_palette(score)
    all_colours = palette.all_colours()
    # instruments_dict = {}
    
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

        # instruments_dict[ins_name] = index
        for note in instrument.notes:
            current_index = current_times.index(note.start)
            current_pitches[current_index] = note.pitch

        angles = [n / float(len(current_times)) * 2 * pi for n in range(len(current_times))]
        angles += angles[:1]

        # part 1
        current_pitches += current_pitches[:1] 
        current_colour = all_colours[index]
        current_colour_rgb = [rgb_to_one(current_colour[0]), rgb_to_one(current_colour[1]), rgb_to_one(current_colour[2])]
        ax.plot(angles, current_pitches, linewidth=1,
                linestyle='solid',c = current_colour_rgb, label=ins_name)
        # ax.fill(angles, current_pitches, c = current_colour_rgb, alpha=0.4)
        index += 1
       
    ax.set_ylim(0, 127)
    ax.set_yticks([0])
    ax.set_xticks([0])
    plt.savefig('pictures/symphony_40_3.png')
    plt.show()


if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Bolero_FLVLC.mid')
    bach_andante = get_midi('Prelude/bach_andante.mid')
    figaro_data = get_midi('Figaro/marriage_of_figaro_overture_ORCH.mid')
    vivaldi_summer = get_midi('Summer/Vivaldi_summer_3_STRE.mid')
    get_visualization_polar_piano_roll(figaro_data)