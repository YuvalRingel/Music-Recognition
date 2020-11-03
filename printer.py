spc = 4
dob_spc = 2*spc

def visualize_tabs(tabs):
    printed_tabs = starter()
    for i in range(len(tabs[1])):
        printed_tabs = chord_printing(printed_tabs, tabs, i)
    printed_tabs = ending(printed_tabs)
    return printed_tabs


def starter():
    starter = [''.ljust(2, ' '), ''.ljust(2+spc, ' '), 'e|', 'B|', 'G|', 'D|', 'A|', 'E|']
    return starter

def chord_printing(printed_tabs, tabs, step):
    if step % 2 == 0:
        printed_tabs[0] += tabs[0][step].ljust(dob_spc, ' ')
    elif step % 2 == 1:
        printed_tabs[1] += tabs[0][step].ljust(dob_spc, ' ')
    for i in range(6):
        printed_tabs[i + 2] += tabs[i + 1][step].ljust(spc, '-')
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
