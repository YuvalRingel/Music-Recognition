from guitar_classes.chords import *
from guitar_classes.guitar import *


def get_tabs(batches_list, freq_list, guitar):
    tabs_list = []
    for i in range(len(batches_list)):
        new_step = get_chord(batches_list[i], freq_list[i], guitar)
        tabs_list.append(new_step)
    grid = chords_and_tabs_to_cols(tabs_list)
    return grid


def get_chord(notes, freqs, guitar):
    # call chords functions
    chord_frets = []

    # this is for the meantime... very general layout, not the most accurate fingers
    i = 5
    while i >= 0:
        for note in notes:
            string = guitar.strings[i]
            fret = string.notes.index(note.unpitched)
            chord_frets.append([i+1, fret])
            i-=1
        break

    # # one note -> not a chord
    if len(notes) == 1:
        is_chord = False
    else:
        is_chord = True
    new_chord = Chord(guitar)
    new_chord.add_chord(chord_frets)
    chord_name = new_chord.chord
    tabs = get_tabs_layout(new_chord)
    return [chord_name, tabs]


def get_tabs_layout(chord):
    tabs = chord.chord_frets
    for i in range(len(tabs)):
        if tabs[i] == -1:
            tabs[i] = '-'
    return tabs


def chords_and_tabs_to_cols(tabs_list):
    grid = []
    for chord in tabs_list:
        new_col = [chord[0],chord[1][0], chord[1][1], chord[1][2],chord[1][3],chord[1][4],chord[1][5]]
        grid.append(new_col)
    grid = np.asarray(grid)
    grid = np.transpose(grid)
    return grid
