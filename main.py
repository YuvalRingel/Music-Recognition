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


class Chord(Guitar):
    def __init__(self, strings):
        Guitar.__init__(self, strings)
        self.chord_frets = [-1, -1, -1, -1, -1, -1]
        self.chord_notes = [X, X, X, X, X, X]
        self.degrees = []
        self.root = [-1, None]
        self.root_string = -1
        self.root_scale = None
        self.chord = ''
        self.notes_used = set()
        self.slash = None
        self.slash_chord = ''

    def __repr__(self):
        result = 'Chord is '
        for i in range(6):
            result += "\n string: " + str(self.strings[i].number) + self.strings[i].string_note.note_name
            result += "\n fret is: " + str(self.chord_frets[i]) + ' ' + str(self.chord_notes[i])
        return result

    def print_root(self):
        result = 'root is on string: ' + str(self.root_string) + '\n'
        result += 'root fret: ' + str(self.root[0]) + ' ' + str(self.root[1])
        print(result)

    def add_note(self, string_num, fret):
        Chord.choose_note(self, string_num, fret)         #adding note and erasing slash chord
        Chord.decide_root(self)
        Chord.produce_chrom_scale(self)  #starting from root
        Chord.decide_chord(self, self.notes_used)

    def choose_note(self, string_num, fret):
        String.choose_fret(self.strings[string_num - 1], fret)
        self.chord_frets[string_num - 1] = fret
        self.chord_notes[string_num - 1] = self.strings[string_num - 1].fret_note_chosen
        self.slash_chord = ''
        self.slash = None

    def decide_root(self, on_demand=False):

        if sum(self.chord_frets) == -6:
            self.root = [-1, None]
            self.root_string = -1
            self.root_scale = None
            self.chord = None
        else:
            for i in range(5, 0, -1):
                if self.chord_frets[i] == -1:
                    continue
                else:
                    self.notes_used = set(self.chord_notes)
                    if X in self.notes_used:
                        self.notes_used.remove(X)
                    Chord.first(self, self.notes_used, i)
                    break

    def first(self, notes, string):
        self.root = [self.chord_frets[string], self.chord_notes[string]]
        self.root_string = string + 1
        self.notes_used.remove(self.root[1])

    def produce_chrom_scale(self):
        chrom_start = chromatic_scale.index(self.root[1])
        root_chrom = chromatic_scale[chrom_start:] + chromatic_scale[:chrom_start]
        self.root_scale = root_chrom

    def decide_chord(self, notes, slash=False):
        degrees = {'3': '', '5': '', '7': '', '9': '', '11': '', '13': ''}
        listed_degrees = list(degrees.keys())
        while len(notes) > 0:
            for key in listed_degrees:
                degrees[key] = Chord.degrees_identifier(self, notes, key, degrees)          #which degree are in the chord
        if slash == True:                                                                           #slash chord have an extension i.e \E
            self.slash_chord = Chord.chord_naming(self, self.root[1].note_name, degrees, True)
        else:
            self.chord = Chord.chord_naming(self, self.root[1].note_name, degrees)

    def degrees_identifier(self, notes, number, degrees):
        if number == '3':
            return self.third(notes)

        elif number == '5':
            temp = self.rest(notes, number, d5)
            if temp == '5' and len(notes) == 0 and list(degrees.values())[0] == 'no3':
                return temp
            else:
                return ''

        elif number == '7':
            temp = self.rest(notes, number, d7b)
            if temp == 'b7':
                return '6'
            else:
                return temp

        elif number == '9':
            temp = self.rest(notes, number, d9)
            if temp == '9' and sorted(degrees.keys())[2] == '':
                return 'add' + temp
            else:
                return temp

        elif number == '11':
            temp = self.rest(notes, number, d11)
            if temp == '11' and sorted(degrees.keys())[2] == '':
                return 'add' + temp
            else:
                return temp

        elif number == '13':
            return self.rest(notes, number, d13)

    def third(self, notes):
        if self.chord_analysis(notes, d3b):
            return 'm'
        elif self.chord_analysis(notes, d3):
            return ''
        elif self.chord_analysis(notes, d4):
            return 'sus4'
        elif self.chord_analysis(notes, d2):
            return 'sus2'
        else:
            return 'no3'

    def rest(self, notes, number, deg):
        name = ''
        if Chord.chord_analysis(self, notes, deg - 1):
            name = 'b' + number
        elif Chord.chord_analysis(self, notes, deg):
            name = number
        elif Chord.chord_analysis(self, notes, deg + 1):
            if number == '7':
                return 'maj' + number
            else:
                name = '#' + number
        return name

    def chord_analysis(self, notes, degree):
        if self.root_scale[degree] in notes:
            notes.remove(self.root_scale[degree])
            return True
        return False

    def chord_naming(self, root, degrees, slash=False):
        name = ''
        degs = list(degrees.values())
        for deg in degs:
            name += deg
        Chord.special_names(self, name)
        name = root + name
        if slash == True:
            name += '/'+self.slash.note_name
        return name

    def special_names(self, name):
        if name == 'no35':
            name = '5'
        elif name[:3] == 'no3':
            name = name[3:] + name[:3]
        elif name == '3':
            name = ''
        elif name == 'mb5' or name == 'b5':
            name = 'dim'
        elif name == '#5':
            name = 'aug'
        elif name == 'm5':
            name = 'm'
        return name

    def print_chord(self):
        result = 'Notes are: \n'
        for i in range(5, -1, -1):
            if self.chord_frets[i] != -1:
                result += str(i+1) + ':' + str(self.chord_frets[i]) + self.chord_notes[i].note_name + ' '
            else:
                result += str(i+1) + ':X' + ' '
        result += '\nChord is: \n'
        result += self.chord
        if self.slash != None:
            result += ' or ' + self.slash_chord
        print(result)

    def change_root(self, new_string):
        new_string -= 1
        for string in range(5, new_string, -1):
            if self.chord_frets[string] != -1:
                self.old_string = string
                self.slash = self.chord_notes[string]
                break
        # chord
        self.notes_used = set(self.chord_notes)
        if X in self.notes_used:
            self.notes_used.remove(X)
        Chord.first(self, self.notes_used, new_string)
        Chord.produce_chrom_scale(self)
        Chord.decide_chord(self, self.notes_used)
        #slash chord
        temp_chords = self.chord_notes
        temp_chords[self.old_string] = X
        self.notes_used = set(temp_chords)
        if X in self.notes_used:
            self.notes_used.remove(X)
        Chord.first(self, self.notes_used, new_string)
        Chord.decide_chord(self, self.notes_used, True)


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