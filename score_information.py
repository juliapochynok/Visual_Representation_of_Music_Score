from re import I
from mido import MidiFile

import pretty_midi
from colour_palettes import CoolPalette, WarmPalette


def get_midi(filename):
    mid = pretty_midi.PrettyMIDI(filename)
    return mid

def get_colour_of_note(instruments_dict, all_colours, value, max_value, name):
    colour_index = instruments_dict[name]
    rgb_colour = all_colours[colour_index]

    opacity = get_alpha(value, max_value)
    full_colour = [rgb_to_one(rgb_colour[0]), 
    rgb_to_one(rgb_colour[1]), rgb_to_one(rgb_colour[2]), opacity]
    return full_colour


def note_sorting_function(el):
    return el[0].start 


def rgb_to_one(rgb):
    return rgb/255


def get_colour_palette(score):
    keys = score.key_signature_changes
    print(keys[0])
    if keys[0].key_number <= 11:
        return WarmPalette
    else:
        return CoolPalette

    
def get_alpha(duration, max_duration):
    return duration/max_duration


def get_all_durations(score):
    durations = []
    for instrument in score.instruments:
        for note in instrument.notes:
            durations.append(note.duration)
    return durations


