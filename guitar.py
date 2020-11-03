import numpy as np
#from fft_to_notes import *


# TDL
# better way to classify notes with hz.

class Note:
    def __init__(self, note_name, hz_octaves):
        self.note_name = note_name
        self.root = False
        self.hz_octaves = np.sort(hz_octaves)
        self.pitches = []
        for i in range(len(self.hz_octaves)):
            name = self.note_name + str(i)
            var = PitchedNote(name, self.hz_octaves[i], self)
            globals()[self.note_name +str(i)] = var
            self.pitches.append(var)

    def __repr__(self):
        return self.note_name


class PitchedNote():
    def __init__(self, pitched_note_name, hz, unpitched):
        self.name = pitched_note_name
        self.hz = hz
        self.unpitched = unpitched

    def __repr__(self):
        return self.name


# make with numpy with header and side collumn
all_herz = np.array([16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87,  # 0
                     32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74,  # 1
                     65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5,  # 2
                     130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.7, 220.0, 233.1, 246.9,  # 3
                     261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0, 466.2, 493.9,  # 4
                     523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0, 932.3, 987.8,  # 5
                     1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976,  # 6
                     2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951,  # 7
                     4186, 4435, 4699, 4978, 5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902])  # 8

C = Note('C', all_herz[0::12])
Cs = Note('C#', all_herz[1::12])
D = Note('D', all_herz[2::12])
Ds = Note('D#', all_herz[3::12])
E = Note('E', all_herz[4::12])
F = Note('F', all_herz[5::12])
Fs = Note('F#', all_herz[6::12])
G = Note('G', all_herz[7::12])
Gs = Note('G#', all_herz[8::12])
A = Note('A', all_herz[9::12])
As = Note('A#', all_herz[11::12])
B = Note('B', all_herz[-1::-12])
X = Note('-', ())

chromatic_scale = [C, Cs, D, Ds, E, F, Fs, G, Gs, A, As, B]

all_pitches = []
for i in range (9):
    for unpitched_note in chromatic_scale:
        all_pitches.append(unpitched_note.pitches[i])

class String:
    def __init__(self, string_note, number, open_pitch):
        self.string_note = string_note
        self.number = number
        self.chrom_index = chromatic_scale.index(string_note)
        self.fret_number_chosen = -1
        self.fret_note_chosen = None
        idx = chromatic_scale.index(string_note) + open_pitch * 12
        self.pitches = all_pitches[idx : idx + 24]
        self.notes = [pitch.unpitched for pitch in self.pitches]

    def __repr__(self):
        result = str(self.number) + '# string is ' + self.string_note.note_name + '\n'
        for note in self.notes:
            result += note.note_name + ' '
        result += "\n Chosen fret is " + str(self.fret_number_chosen)
        return result

    def choose_fret(self, fret):
        self.fret_number_chosen = fret
        self.fret_note_chosen = self.notes[fret] if fret != -1 else None


e_string = String(E, 1, 4)
B_string = String(B, 2, 3)
G_string = String(G, 3, 3)
D_string = String(D, 4, 3)
A_string = String(A, 5, 2)
E_string = String(E, 6, 2)

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
        #self.herzs_list = Guitar.get_hz_list(self)  # from 6th string to 1st string

    def __repr__(self):
        result = 'Guitar tuning is: '
        for string in self.strings:
            result += string.string_note.note_name
        return result

    # def get_hz_list(self):
    #     herzs_list = []
    #     for string in self.strings:
    #         herzs_list.append(string.open_hz)
    #     return herzs_list

guitar_string = e_string, B_string, G_string, D_string, A_string, E_string
standard_guitar = Guitar(guitar_string)
