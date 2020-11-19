from tabs_process import *
from e_printer import *
###############################################
# link='https://www.youtube.com/watch?v=qAlyjGrThGo',
# A B C D E F G
# major and than minor
# strum, one note t a time, strum
###############################################

new_tabs = file_to_tabs(link='https://www.youtube.com/watch?v=qAlyjGrThGo',
                        guitar = standard_guitar,
                        simplify = False)
print_tabs(new_tabs)


















#
# chord1 = Chord(standard_guitar)
#
# notes = [[6, 5],[5, 3],[4, 2],[3, 0],[2, 1],[1, 0]]
# chord1.add_chord(notes)
# Chord.add_note(chord1, 6, 5)
# Chord.add_note(chord1, 5, 3)
# Chord.add_note(chord1, 4, 2)
# Chord.add_note(chord1, 3, 0)
# Chord.add_note(chord1, 2, 1)
# Chord.add_note(chord1, 1, 0)
#
# Chord.change_root(chord1,5)
# Chord.print_chord(chord1)