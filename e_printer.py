spc = 4
dob_spc = 2*spc

def visualize_tabs(tabs, full_stops, simplify):
    printed_tabs = starter()
    for i in range(len(tabs[1])):
        printed_tabs = chord_printing(printed_tabs, tabs, i, full_stops, simplify)
    printed_tabs = ending(printed_tabs)
    return printed_tabs


def starter():
    starter = [''.ljust(2, ' '), ''.ljust(2+spc, ' '), 'e|', 'B|', 'G|', 'D|', 'A|', 'E|']
    return starter

def chord_printing(printed_tabs, tabs, step, full_stops, simplify):
    # deleting all extra data leaving just root note, #, m
    if simplify:
        i=0
        chord_name = tabs[0][step][i]
        i+=1
        if tabs[0][step][i] == '#':
            chord_name += tabs[0][step][i]
            i+=1
        if tabs[0][step][i] == 'm' and tabs[0][step][i+1] != 'a':
            chord_name += tabs[0][step][i]
    else:
        chord_name = tabs[0][step]

    # making steps so the name is readable
    if step % 2 == 0:
        printed_tabs[0] += chord_name.ljust(dob_spc, ' ')
    elif step % 2 == 1:
        printed_tabs[1] += chord_name.ljust(dob_spc, ' ')
    for i in range(6):
        printed_tabs[i + 2] += tabs[i + 1][step].ljust(spc, '-')

    # adding stops between big chunks to better understand the chords
    if step in full_stops:
        printed_tabs[0] += '  '
        printed_tabs[1] += '  '
        for i in range(6):
            printed_tabs[i + 2] += '|-'

    return printed_tabs


def ending(printed_tabs):
    printed_tabs[0] += ' '
    printed_tabs[1] += ' '
    printed_tabs[2:] = [row + '|' for row in printed_tabs[2:]]
    return printed_tabs


def print_tabs(tabs):
    for row in tabs:
        print(row)
    return
