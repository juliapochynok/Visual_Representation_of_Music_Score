import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv, visualize_bcdav_2d
from line_chart import get_visualization_durations
from arc_chart import get_visualization_arc_volume
from triplot_chart import get_visualization_arc_duration_triangle, get_visualization_arc_volume_triangle
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    style_data = {'colour': 5, 'font': 1, 'placement': 1}

    get_visualization_polar_piano_roll(bolero_data[0], bolero_data[1], style_data)
    get_visualization_arc_volume(bolero_data[0], bolero_data[1], style_data)
    get_visualization_arc_volume_triangle(bolero_data[0], bolero_data[1], True, style_data)
    get_visualization_arc_duration_triangle(bolero_data[0], bolero_data[1], False, style_data)
    visualize_bcdav_2d(bolero_data[0], bolero_data[1], style_data)

