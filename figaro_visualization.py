import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv
from line_chart import get_visualization_durations
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')

    # visualize_bcd(figaro_data)
    # get_visualization_durations(figaro_data)
    get_visualization_polar_piano_roll(figaro_data)
