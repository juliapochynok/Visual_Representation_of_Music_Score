from score_information import get_midi
from polar_chart import get_visualization_polar_piano_roll
from arc_chart import get_visualization_arc_volume, get_visualization_arc_duration
from triplot_chart import get_visualization_arc_volume_triangle, get_visualization_arc_duration_triangle
from bar_chart import visualize_bcdav_2d

bach_air = get_midi('Air/J.-S.-Bach_Air.mid')
bach_fugue = get_midi('Tocatta_Fugue/J.-S.-Bach_Tocatta-and-Fugue-D-minor.mid')

bolero_data = get_midi('Bolero/Alfredo-Casella_Bolero.mid')
vivaldi_summer = get_midi('Summer/Vivaldi_Summer.mid')

figaro_data = get_midi('Figaro/W.-A.-Mozart_The-Marriage-of-Figaro.mid')
symphony_40 = get_midi('Symphony_40/W.-A.-Mozart_Symphony-No-40.mid')

all_scores = [bach_air, bach_fugue, bolero_data, vivaldi_summer, figaro_data, symphony_40]

def visualize_all():
    '''
    This function creates all the visualizations
    for all the socres in all_scores list.
    '''
    for score in all_scores:
        
        for colour_ind in range(6):
            for font_ind in range(1, 5):
                for place_ind in range(1, 4):
                    # 1,2,3
                    if (place_ind != 4):
                        style_data = {'colour': colour_ind, 'font': font_ind, 'placement':place_ind}
                        get_visualization_polar_piano_roll(score[0], score[1], style_data)

                    # 1,2,3,4
                    style_data = {'colour': colour_ind, 'font': font_ind, 'placement':place_ind}
                    get_visualization_arc_volume(score[0], score[1], style_data)

                    # 1,3,4
                    if (place_ind != 2):
                        style_data = {'colour': colour_ind, 'font': font_ind, 'placement':place_ind}
                        get_visualization_arc_volume_triangle(score[0], score[1], True, style_data)
                        style_data = {'colour': colour_ind, 'font': font_ind, 'placement':place_ind}
                        get_visualization_arc_duration_triangle(score[0], score[1], False, style_data)

                        style_data = {'colour': colour_ind, 'font': font_ind, 'placement':place_ind}
                        visualize_bcdav_2d(score[0], score[1], style_data)



if __name__ == '__main__':
    visualize_all()
