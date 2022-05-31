import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv, visualize_bcdav_2d
from line_chart import get_visualization_durations
from arc_chart import get_visualization_arc_volume
from triplot_chart import get_visualization_arc_duration_triangle, get_visualization_arc_volume_triangle
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor.mid')
    style_data = {'colour': 4, 'font': 1, 'placement': 1}

    get_visualization_polar_piano_roll(bach_fugue[0], bach_fugue[1], style_data)
    get_visualization_arc_volume(bach_fugue[0], bach_fugue[1], style_data)
    get_visualization_arc_volume_triangle(bach_fugue[0], bach_fugue[1], True, style_data)
    get_visualization_arc_duration_triangle(bach_fugue[0], bach_fugue[1], False, style_data)
    visualize_bcdav_2d(bach_fugue[0], bach_fugue[1], style_data)