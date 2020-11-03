from file_to_segmants import *
from segments_to_fft import *
from fft_to_notes import *
from notes_to_tabs import *
from guitar import *
from printer import *


# TDL
# guitar input

def file_to_tabs(guitar, link = False, path = False):
    samplerate, data = get_data(link, path)  # arg # fetching data from file/youtube
    datas_list = divide_data(data, samplerate)  # dividing fetched data into bits of notes
    freq_list = get_freqs(datas_list, samplerate)
    batches_list, correct_freqs_list = get_notes(freq_list)
    tabs = get_tabs(batches_list, correct_freqs_list, guitar)
    printed_tabs = visualize_tabs(tabs)
    return printed_tabs
