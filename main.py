from chords import *

guitar1 = [e_string, B_string, G_string, D_string, A_string, E_string]
chord1 = Chord(guitar1)

Chord.add_note(chord1, 6, 5)
Chord.add_note(chord1, 5, 3)
Chord.add_note(chord1, 4, 2)
Chord.add_note(chord1, 3, 0)
Chord.add_note(chord1, 2, 1)
Chord.add_note(chord1, 1, 0)

Chord.change_root(chord1,5)
Chord.print_chord(chord1)