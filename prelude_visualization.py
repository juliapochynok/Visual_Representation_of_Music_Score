import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv
from line_chart import get_visualization_durations
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    bach_air = get_midi('Air/Johann-Sebastian-Bach_Air.mid')

    bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor-BWV-565.mid')
    bach_andante = get_midi('Prelude/J.-S.-Bach_Andante.mid')

    vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

    symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

    oi_u_luzi = get_midi('oi_u_luzi/oi2.mid')
    # visualize_bcd(symphony_40)
    # get_visualization_durations(symphony_40)
    get_visualization_polar_piano_roll(symphony_40)
