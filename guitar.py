class Note:
    def __init__(self, note_name):
        self.note_name = note_name
        self.root = False

    def __repr__(self):
        return 'The note is ' + self.note_name


C = Note('C')
Cs = Note('C#')
D = Note('D')
Ds = Note('D#')
E = Note('E')
F = Note('F')
Fs = Note('F#')
G = Note('G')
Gs = Note('G#')
A = Note('A')
As = Note('A#')
B = Note('B')
X = Note('-')

chromatic_scale = [C, Cs, D, Ds, E, F, Fs, G, Gs, A, As, B]


class String:
    def __init__(self, string_note, number):
        self.string_note = string_note
        self.number = number
        self.chrom_index = chromatic_scale.index(string_note)
        self.fret_number_chosen = -1
        self.fret_note_chosen = None
        self.notes = []
        semitone = self.chrom_index
        for fret in range(0, 24):
            self.notes.append(chromatic_scale[semitone])
            semitone += 1 if semitone < 11 else -11
        # self.bar12 = self.notes[:12]

    def __repr__(self):
        result = str(self.number) + '# string is ' + self.string_note.note_name + '\n'
        for note in self.notes:
            result += note.note_name + ' '
        result += "\n Chosen fret is " + str(self.fret_number_chosen)
        return result

    def choose_fret(self, fret):
        self.fret_number_chosen = fret
        self.fret_note_chosen = self.notes[fret] if fret != -1 else None


e_string = String(E, 1)
B_string = String(B, 2)
G_string = String(G, 3)
D_string = String(D, 4)
A_string = String(A, 5)
E_string = String(E, 6)

# degrees for chromatic scale
d1 = 0
d2b = 1
d2 = 2
d3b = 3
d3 = 4
d4 = 5
d5b = 6
d5 = 7
d5s = 8
d6 = 9
d7b = 10
d7 = 11
d8 = 12
d9b = d2b
d9 = d2
d9s = d3b
d11 = d4
d13 = d6


class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def __repr__(self):
        result = 'Guitar tuning is: '
        for string in self.strings:
            result += string.string_note.note_name
        return result

