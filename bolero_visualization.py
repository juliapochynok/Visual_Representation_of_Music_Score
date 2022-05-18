import pretty_midi
from bar_chart import visualize_bcd, visualize_bcv
from line_chart import get_visualization_durations
from polar_chart import get_visualization_polar_piano_roll
from score_information import get_midi

if __name__ == '__main__':
    bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
    
    # visualize_bcd(bolero_data)
    # get_visualization_durations(bolero_data)
    get_visualization_polar_piano_roll(bolero_data)

