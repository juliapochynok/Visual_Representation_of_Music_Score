import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv
from line_chart import get_visualization_durations
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    bach_air = get_midi('Air/bach_air.mid')

    bach_fugue = get_midi('Tocatta_Fugue/bach_tocatta_fugue_d_minor.mid')
    bach_andante = get_midi('Prelude/bach_andante.mid')

    vivaldi_summer = get_midi('Summer/Vivaldi_summer_3_STRE.mid')

    symphony_40 = get_midi('Symphony_40/Mozart_Symphony_No-40.mid')
    # visualize_bcd(symphony_40)
    # get_visualization_durations(symphony_40)
    get_visualization_polar_piano_roll(symphony_40)
