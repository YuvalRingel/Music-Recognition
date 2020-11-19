from guitar_classes.guitar import *

# TDL
# function to determine if its a single note or a chord

def get_notes(freq_list):
    batches_list = []
    correct_freqs_list = []
    for batch in freq_list:
        new_notes_batch = []
        new_freqs_batch = []
        for freq in batch:
            note, correct_freq = freq_to_note(freq)
            new_notes_batch.append(note)
            new_freqs_batch.append(correct_freq)
        batches_list.append(new_notes_batch)
        correct_freqs_list.append(new_freqs_batch)
    return batches_list, correct_freqs_list

def freq_to_note(freq):
    correct_freq, freq_index = closest(all_herz, freq)
    note = all_pitches[freq_index]
    print_validation(freq, freq_index, correct_freq, note)
    return note, correct_freq

def closest(lst, K):
    idx = (np.abs(lst - K)).argmin()
    return lst[idx], idx

def print_validation(freq, freq_index, correct_freq, note):
    print(freq)
    print('index is: ', freq_index)
    print('correct freq is: ', correct_freq)
    print(note)
    print('\n\n')