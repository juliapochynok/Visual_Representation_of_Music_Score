from re import I
from mido import MidiFile
import matplotlib.font_manager

import pretty_midi
from colour_palettes import CoolPalette, WarmPalette

from matplotlib import font_manager
font_manager.findSystemFonts(fontpaths=None, fontext="ttf")

dvfont = {'fontname':'DejaVu Sans'}
ofont = {'fontname':'Oswald'}
afont = {'fontname':'Alata'}
smfont = {'fontname':'Smooch'}
zfont = {'fontname':'Zen Loop'}

def get_text_font(number):
    '''
    This function returns text font depending on number 
    '''
    if number == 1:
        return dvfont
    elif number == 2:
        return ofont
    elif number == 3:
        return afont
    elif number == 4:
        return smfont
    else:
        return zfont             


def get_midi(filename):
    '''
    This function returns data from midi file
    '''
    mid = pretty_midi.PrettyMIDI(filename)
    text_list = filename_to_strings(filename)
    return [mid, text_list]

def filename_to_strings(filename):
    '''
    This function returns author name and title of the score
    '''
    index_start = filename.index("/")
    filename_strip = filename[index_start+1:]
    index_end = filename_strip.index(".mid")
    index_center = filename_strip.index("_")
    author = filename_strip[:index_center]
    name = filename_strip[index_center + 1:index_end]
    author = author.replace("-", " ")
    name = name.replace("-", " ")
    return [author, name]

def get_colour_of_note(instruments_dict, all_colours, value, max_value, name):
    '''
    This function calculates the colour of the note depending on
    the key of the score
    '''
    colour_index = instruments_dict[name]
    rgb_colour = all_colours[colour_index]

    opacity = get_alpha(value, max_value)
    full_colour = [rgb_to_one(rgb_colour[0]), 
    rgb_to_one(rgb_colour[1]), rgb_to_one(rgb_colour[2]), opacity]
    return full_colour


def note_sorting_function(el):
    '''
    This function sorts notes
    '''
    return el[0].start 


def rgb_to_one(rgb):
    '''
    This function transforms rgb values to 0-1 range
    '''
    return rgb/255


def get_colour_palette(score):
    '''
    This function returns colour palette for the score
    '''
    keys = score.key_signature_changes
    if len(keys) != 0 and keys[0].key_number <= 11:
        return WarmPalette
    else:
        return CoolPalette

    
def get_alpha(duration, max_duration):
    '''
    This function calculates the alpha value
    '''
    return duration/max_duration


def get_all_durations(score):
    '''
    This function returns list of notes duration
    '''
    durations = []
    for instrument in score.instruments:
        for note in instrument.notes:
            durations.append(note.duration)
    return durations

warm_colours_back = [
    [rgb_to_one(255), rgb_to_one(224), rgb_to_one(214)],
    [rgb_to_one(244), rgb_to_one(255), rgb_to_one(145)],
    [rgb_to_one(211), rgb_to_one(221), rgb_to_one(187)],
    [rgb_to_one(22), rgb_to_one(1), rgb_to_one(1)],
    [rgb_to_one(89), rgb_to_one(13), rgb_to_one(34)],
    [rgb_to_one(0), rgb_to_one(0), rgb_to_one(0)],
]


warm_colour_edges = [
    [rgb_to_one(164), rgb_to_one(19), rgb_to_one(60)],
    [rgb_to_one(255), rgb_to_one(123), rgb_to_one(0)],
    [rgb_to_one(49), rgb_to_one(87), rgb_to_one(44)],
    [rgb_to_one(255), rgb_to_one(204), rgb_to_one(213)],
    [rgb_to_one(255), rgb_to_one(179), rgb_to_one(193)],
    [rgb_to_one(255), rgb_to_one(255), rgb_to_one(255)],
]

cool_colours_back = [
    [rgb_to_one(127), rgb_to_one(99), rgb_to_one(110)],
    [rgb_to_one(132), rgb_to_one(165), rgb_to_one(157)],
    [rgb_to_one(70), rgb_to_one(32), rgb_to_one(50)],
    [rgb_to_one(64), rgb_to_one(145), rgb_to_one(108)],
    [rgb_to_one(0), rgb_to_one(0), rgb_to_one(0)],
    [rgb_to_one(233), rgb_to_one(236), rgb_to_one(239)]
]

cool_colour_edges = [
    [rgb_to_one(245), rgb_to_one(202), rgb_to_one(195)],
    [rgb_to_one(171), rgb_to_one(245), rgb_to_one(236)],
    [rgb_to_one(252), rgb_to_one(177), rgb_to_one(166)],
    [rgb_to_one(183), rgb_to_one(228), rgb_to_one(199)],
    [rgb_to_one(255), rgb_to_one(255), rgb_to_one(255)],
    [rgb_to_one(73), rgb_to_one(80), rgb_to_one(87)]
]

def add_background(palette, number):
    '''
    This function chooses background depending on number
    '''
    if palette is WarmPalette:
        return [warm_colours_back[number], warm_colour_edges[number]]
    else:
        return [cool_colours_back[number], cool_colour_edges[number]]
