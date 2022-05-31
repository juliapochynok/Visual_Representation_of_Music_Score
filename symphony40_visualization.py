import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv, visualize_bcdav_2d
from line_chart import get_visualization_durations
from arc_chart import get_visualization_arc_volume
from triplot_chart import get_visualization_arc_duration_triangle, get_visualization_arc_volume_triangle
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')
    style_data = {'colour': 4, 'font': 1, 'placement': 1}

    get_visualization_polar_piano_roll(symphony_40[0], symphony_40[1], style_data)
    get_visualization_arc_volume(symphony_40[0], symphony_40[1], style_data)
    get_visualization_arc_volume_triangle(symphony_40[0], symphony_40[1], True, style_data)
    get_visualization_arc_duration_triangle(symphony_40[0], symphony_40[1], False, style_data)
    visualize_bcdav_2d(symphony_40[0], symphony_40[1], style_data)

