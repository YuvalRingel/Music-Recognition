from chords import *
from guitar import *
from tabs_process import *
from printer import *

# new_tabs = file_to_tabs(path=''./sounds/'Bmaj7.wav', guitar = standard_guitar)
new_tabs = file_to_tabs(link='https://www.youtube.com/watch?v=MRknyvTEI7Q', guitar = standard_guitar)
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