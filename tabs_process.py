from a_file_to_segmants import *
from b_segments_to_fft import *
from c_fft_to_notes import *
from d_notes_to_tabs import *
from e_printer import *




def file_to_tabs(guitar, link = False, path = False, simplify = False):
    samplerate, data = get_data(link, path)  # arg # fetching data from file/youtube
    datas_list, full_stops = divide_data(data, samplerate)  # dividing fetched data into bits of notes
    freq_list = get_freqs(datas_list, samplerate)
    batches_list, correct_freqs_list = get_notes(freq_list)
    tabs = get_tabs(batches_list, correct_freqs_list, guitar)
    printed_tabs = visualize_tabs(tabs, full_stops, simplify)
    return printed_tabs
